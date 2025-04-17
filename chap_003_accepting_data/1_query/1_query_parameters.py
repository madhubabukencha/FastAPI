"""
In this document, we will see how we can pass data to the arguments
in our API. Usually we pass arguments after '?'and '&' used to separate
arguments

Example:
/logs?start=2025-04-01&end=2025-04-07&level=Error
"""
from datetime import datetime
from http import HTTPStatus  # Tell status of http response
from fastapi import FastAPI, HTTPException
import pandas as pd


app = FastAPI()
data = pd.read_csv("dummy_data.csv")

@app.get('/logs')
def logs_query(start: datetime, end: datetime):
    if start >= end:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Start date must be less than end data"
        )
    records = data[(data['date'] >= str(start)) & (data['date'] <= str(end))].to_dict(orient="records")
    print(f"Length: {len(records)}")
    print(f"Length: {records}")
    if len(records) < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail="No records found")
    return {
        "count": len(records),
        "records": records
    }
