"""
Lifespan:
It will handle initialization and cleanup of resources before app starts
and after it shuts down. Helps in handling database connections, External
Service connections (like Redis, RabbitMQ, etc.), and loading ml models.
Runs once when the app starts/stops (not per request).

Depends:
To reuse code across routes and manage dependencies (like DB connections,
auth, etc.) per request and runs for each request and also Automatically
handles cleanup.
"""
import logging
from contextlib import asynccontextmanager
import os
from fastapi import FastAPI, Depends, HTTPException
import aiosqlite


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DB_NAME = "example.db"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager to handle app startup and shutdown events.
    """
    logger.info("App is starting up...")
    # Initialize database
    db = await aiosqlite.connect(DB_NAME)
    await db.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL UNIQUE
                     )
                     """)
    await db.commit()
    logger.info("Database initialized.")
    yield  # APP runs here

    # Cleanup
    logger.info("Closing the database connection...")
    await db.close()
    logger.info("App is shutting down...")


app = FastAPI(lifespan=lifespan)


# Async dependency to get the database connection
async def get_db():
    """
    Dependency to get the database connection.
    """
    async with aiosqlite.connect(DB_NAME) as db:
        yield db


# Routes
@app.post("/users/")
async def create_user(name: str, email: str,
                      db: aiosqlite.Connection = Depends(get_db)):
    """
    Create a new user in the database.
    """
    try:
        await db.execute("INSERT INTO USERS (name, email) VALUES (?, ?)",
                         (name, email))
        await db.commit()
        return {"message": "User created successfully",
                "name": name,
                "email": email}
    except aiosqlite.IntegrityError:
        logger.error(f"User with email {email} already exists.")
        raise HTTPException(status_code=400,
                            detail="User with this email already exists.")
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=500,
                            detail="Internal Server Error")


@app.get("/users/{user_id}")
async def get_user(user_id: int, db: aiosqlite.Connection = Depends(get_db)):
    """
    Get a user by ID from the database.
    """
    async with db.execute("SELECT * FROM USERS WHERE id = ?", (user_id,)) as cursor:
        user = await cursor.fetchone()
    if user:
        return {"id": user[0], "name": user[1], "email": user[2]}
    raise HTTPException(status_code=404,
                       detail="User not found")

if __name__ == "__main__":
    import uvicorn
    # Run the app with uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True,
                log_level="info")
