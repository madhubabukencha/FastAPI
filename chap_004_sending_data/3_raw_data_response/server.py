"""
In this script, we will learn how to read data from the request body and
send a image as a response instead of a json response.
"""
from http import HTTPStatus
from fastapi import FastAPI, Request, Response, HTTPException
from io import BytesIO
from PIL import Image


app = FastAPI()
max_image_size = 5 * 1024 * 1024  # 5 MB


@app.post("/resize-image")
async def resize_image(width: int, height: int, request: Request):
    """
    Resize an image to the given width and height.
    """
    size = int(request.headers.get("Content-Length", 0))
    if size > max_image_size:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Image size exceeds the limit of 5 MB",
        )
    
    if not size:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="File is not provided in the request body",
        )
    
    # Reading the image from the request body
    image_data = await request.body()
    image = Image.open(BytesIO(image_data))
    image = image.resize((width, height))
    image_io = BytesIO()
    image.save(image_io, format="JPEG")
    image_io.seek(0)
    return Response(
        content=image_io.getvalue(),
        media_type="image/jpeg",
        headers={"Content-Disposition": "inline; filename=image.jpg"},
    )
