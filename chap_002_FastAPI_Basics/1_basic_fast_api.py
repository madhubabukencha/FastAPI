"""
Simple API implementation
"""
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/health")
def health():
    # FastAPI automatically converts it into the JSON object
    return {"errors": None}


if __name__ == '__main__':
    # you have to pass module name to use reload or workers option
    uvicorn.run("1_basic_fast_api:app",
                host="0.0.0.0", port=8000, reload=True)
