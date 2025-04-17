from datetime import datetime
from http import HTTPStatus
from fastapi import FastAPI, HTTPException
# Helps in verifying data type and conditions like min_length
from pydantic import BaseModel, Field
import db

app = FastAPI()


class Student(BaseModel):
    """Student Object"""
    joining_data: datetime
    name: str = Field(min_length=4)
    age: int = Field(gt=1, le=120)
    fee: float = Field(gt=1)


@app.post("/new_student/")
def new_student(student: Student):
    """Inserts new student data"""
    record = db.Student(
        joining_data=student.joining_data,
        name=student.name,
        age=student.age,
        fee=student.fee
    )

    key = db.insert(record)
    return {"key": key}


@app.get("/student/{key}")
def get_student(key: str) -> Student:
    "Return student data"
    record = db.get(key)
    if record is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail="Student not found")
    student = Student(
        joining_data=record.joining_data,
        name=record.name,
        age=record.age,
        fee=record.fee
    )
    return student
