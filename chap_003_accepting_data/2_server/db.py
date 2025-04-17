from dataclasses import dataclass
from datetime import datetime
from threading import Lock
from uuid import uuid4


# The Lock() ensures that the operations on the
# shared _records dictionary are atomic and synchronized.
_lock = Lock()
_records = {}


@dataclass
class Student:
    joining_data: datetime
    name: str
    age: int
    fee: float


def insert(student: Student):
    """Insert the data into record"""
    key = uuid4().hex
    with _lock:
        _records[key] = student
    return key


def get(key) -> Student:
    """Gets student data from the database."""
    with _lock:
        return _records.get(key)
