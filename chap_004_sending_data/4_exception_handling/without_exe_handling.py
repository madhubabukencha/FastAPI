"""
If you don't handle error properly will get message like

{
  'detail': 'Not Found'
}
"""
from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn


app = FastAPI()

class FreqError(Exception):
    """
    Custom exception for frequency errors.
    """
    pass


def char_freq(text: str) -> dict:
    if not text:
        raise FreqError("Input text cannot be empty.")
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Don't worry we can even send data in get requests to the server but with limitation
@app.get("/char_freq")
def frequency(text: str):
    return char_freq(text)
