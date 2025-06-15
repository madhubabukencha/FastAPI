"""
Configurations usually comes in several layers:
- Default: These are the ones that you set in your code.
           Once the server is starting without any changes,
           these will be used.
- Configuration file: This will be used to override the default
- Environment variables: These will override the configuration file
- Command line arguments: These will override the environment variables

There are several libraries for handling configurations in Python. we are
going to use dynaconf library. It supports environment variables, configuration
files and secrets management.
"""
from argparse import ArgumentParser
import uvicorn
from config import settings
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify if the server is running.
    """
    return {"status": "ok"}
 

if __name__ == "__main__":
    # Parse command line arguments
    parser = ArgumentParser(description="Run the FastAPI server with specified configurations.")
    parser.add_argument("--host", type=str, default=settings.HOST, help="Host to run the server on")
    parser.add_argument("--port", type=int, default=settings.PORT, help="Port to run the server on")
    args = parser.parse_args()

    settings.update({"HOST": args.host, "PORT": args.port})

    if settings.PORT < 0 and settings.HOST > 65_535:
        raise SystemExit(f"Port invalid - Port: {settings.PORT}")

    # Start the server with the specified host and port
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
