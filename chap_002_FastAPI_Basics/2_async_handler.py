"""
A simple demo of how Async works in FastAPI

ABOUT ASYNCHRONOUS:
Async (asynchronous) programming in Python allows you to write
concurrent code that can handle multiple tasks seemingly at the
same time, without using multiple threads. It's particularly useful
for I/O-bound tasks (like network requests, file operations) where 
your program often waits for external resources.

TESTING:
Use 3_test_async_results.py script to test your results of each API.
"""

from time import sleep
import asyncio
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/sleep/sys")
def nsys_sleep():
    """
    A function without Asynchronous
    """
    sleep(1)
    return {"error": None}


@app.get("/sleep/async-sys")
async def sys_sleep():
    """
    You should never do like this, if you pass 10 current request
    then it will wait 10 seconds to complete all of them.
    """
    sleep(1)
    return {"error": None}


@app.get("/sleep/async-aio")
async def aio_sleep():
    """
    While one task is waiting for something other task will be picked up.
    """
    await asyncio.sleep(1)
    return {"error": None}

if __name__ == "__main__":
    uvicorn.run(app)