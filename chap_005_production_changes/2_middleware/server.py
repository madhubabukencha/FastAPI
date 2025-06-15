"""
What is middleware?
Middleware is software that acts as an intermediary between
different applications or services, allowing them to communicate
and share data. It can handle tasks such as authentication, logging,
and request/response processing, enabling developers to build scalable
and maintainable systems by separating concerns.
Middleware is often used in web applications to process requests
and responses, manage sessions, and perform other cross-cutting concerns.
"""
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse


# Defining simple token for authentication
VALID_TOKEN = "MY_SECRET_TOKEN"


app = FastAPI()

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    """
    Middleware to authenticate requests using a token.
    If the token is valid, the request is processed; 
    otherwise, an error response is returned.
    """
    # By passing root directory
    if request.url.path == "/":
        return await call_next(request)

    token = request.headers.get("Authorization")

    if token != VALID_TOKEN:
        return JSONResponse(
            status_code=401,
            content={"message": "Unauthorized"}
        )

    response: Response = await call_next(request)
    return response


@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI server with middleware!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Endpoint to retrieve an item by its ID.
    """
    return {"item_id": item_id, "message": "Item retrieved successfully!"}

