from pydantic import BaseModel, field_validator
from datetime import datetime


class User(BaseModel):
    """Data model for a User without any relations."""

    pid: int
    first_name: str
    last_name: str

    @field_validator("pid")
    def pid_must_be_9_digits(cls, value: int):
        if value < 100000000 or value > 999999999:
            raise ValueError("Invalid PID")
        return value


class Checkin(BaseModel):
    """Data model for a Checkin without relations."""

    id: int
    timestamp: datetime

class UserDetails(User):
    """Adding checkins to the User class."""
    checkins: list[Checkin]

class CheckinDetails(Checkin):
    """Adding user to Checkin Class"""
    user: User
