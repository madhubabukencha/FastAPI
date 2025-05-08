"""
Serialization:
Serialization is the process of converting an object into a format that can be easily stored or transmitted and then reconstructed later.
In FastAPI, serialization is the process of converting Python objects into JSON format for sending as a response to the client.

Pydantic V2 serializes dates into ISO 8601 format by default. example: P120DT1H, P120D, P1Y2M3DT4H5M6S.
We have to use the field_serializer decorator to serialize the timedelta object into a string format.
"""
from datetime import datetime, timedelta
from fastapi import FastAPI
from pydantic import BaseModel, field_serializer    


app = FastAPI()


class TimeResponse(BaseModel):
    """
    TimeResponse data model
    """
    delta: timedelta
    country: str

    @field_serializer("delta")
    def serialize_timedelta(self, value: timedelta) -> str:
        """
        Serialize the timedelta object into a string format.
        """
        return str(value)



@app.get("/time_delta")
def get_time_delta(start: datetime, end: datetime) -> TimeResponse:
    """
    Returns the time delta between two datetime objects.
    """
    delta = end - start
    print(f"Delta: {delta}")
    country = "India"
    return TimeResponse(delta=delta, country=country)
