"""
If you don't handle error properly will get message like

{
  'detail': 'Not Found'
}
"""
from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


class FreqError(Exception):
    """
    Custom exception for frequency errors.
    """


@app.exception_handler(FreqError)
async def freq_error_handler(request, exc):
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content={"message": str(exc)},  # This need to be handled carefully in prod
        headers={"X-Error": request.query_params.get("text")},  # Usually custom headers start with X-
    )


def char_freq(text: str) -> dict:
    print("Length of text:", len(text))
    if not text:
        raise FreqError("Input text cannot be empty.")
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


# Don't worry we can even send data in get requests
# to the server but with limitation
@app.get("/char_freq")
def frequency(text: str):
    return char_freq(text)
