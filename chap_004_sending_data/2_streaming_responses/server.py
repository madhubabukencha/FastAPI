"""
Streaming Responses in FastAPI:
Streaming responses allow your FastAPI server to send data to the
client incrementally, rather than waiting to prepare the entire 
response before sending it.

Run the get.sh script to see how how streaming responses work.
"""
import time
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uvicorn


app = FastAPI()


data = [["Alice", 25, "Engineer"],
        ["Bob", 30, "Designer"],
        ["Charlie", 35, "Teacher"],
        ["David", 40, "Doctor"],
        ["Eve", 45, "Nurse"]]


class User(BaseModel):
    """
    User attribute class
    """
    name: str
    age: int
    occupation: str


def generate_data():
    """
    Generator function to yield user data.
    """
    for item in data:
        yield User(name=item[0],
                   age=item[1],
                   occupation=item[2]).model_dump_json() + "\n"
        time.sleep(1)


@app.get("/get_users")
async def get_users():
    """
    Endpoint to stream user data.
    """
    return StreamingResponse(generate_data(),
                             media_type="application/json",
                             status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
