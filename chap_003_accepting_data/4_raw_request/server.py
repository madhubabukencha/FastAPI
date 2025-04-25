"""
Sometimes we have to directly work with raw requests. This
program show to work with raw requests and how to parse them.
"""
from fastapi import FastAPI, Request, HTTPException
from PIL import Image
# BytesIO from the io module is a class that provides a file-like
# interface for in-memory bytes operations.Simulating a file object
# for libraries that expect file-like objects (e.g., Pillow for images, 
# pandas for CSV data).Simulating a file object for libraries that expect
# file-like objects (e.g., Pillow for images, pandas for CSV data).
from io import BytesIO
from http import HTTPStatus


app = FastAPI()

MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 1 MB

@app.post("/upload-image")
async def upload_image(request: Request):
    """
    Upload an image and return its size.
    """
    size = int(request.headers.get("Content-Length", 0))
    if not size:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Missing Content-Length header."
        )
    if size > MAX_IMAGE_SIZE:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Image size exceeds the limit. Maximum size is 5 MB."
        )
    
    # Access request details directly
    headers = request.headers
    client_host = request.client.host
    client_port = request.client.port
    method = request.method
    path = request.url.path

    data = await request.body()
    io = BytesIO(data)
    image = Image.open(io)
    return {
        "size": size,
        "format": image.format,
        "mode": image.mode,
        "headers": headers,
        "client_host": client_host,
        "client_port": client_port,
        "method": method,
        "path": path,
        'width': image.width,
        'height': image.height
    }
