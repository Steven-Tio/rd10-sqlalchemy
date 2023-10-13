from datetime import datetime
from typing import Self, Type

from .models import User, Checkin

# TODO: Uncomment once UserDetails and CheckinDetails are implemented.
# from .models import UserDetails, CheckinDetails

from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import (
    sessionmaker,
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session,
    relationship,
)


class Base(DeclarativeBase):
    ...


class UserEntity(Base):
    __tablename__ = "users"

    pid: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)

    checkins: Mapped[list["CheckinEntity"]] = relationship(back_populates="user")

    @classmethod
    def from_model(cls: Type[Self], user: User) -> Self:
        return UserEntity(
            pid=user.pid, first_name=user.first_name, last_name=user.last_name
        )

    def to_model(self) -> User:
        return User(pid=self.pid, first_name=self.first_name, last_name=self.last_name)

    # TODO: Uncomment once UserDetails is implemented
    # def to_model_details(self) -> UserDetails:
    #     checkins = map(lambda checkin_entity: checkin_entity.to_model(), self.checkins)
    #     return UserDetails(
    #         pid=self.pid,
    #         first_name=self.first_name,
    #         last_name=self.last_name,
    #         checkins=checkins,
    #     )


class CheckinEntity(Base):
    __tablename__ = "checkins"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime)
    user_pid: Mapped[int] = mapped_column(ForeignKey("users.pid"))
    user: Mapped["UserEntity"] = relationship(back_populates="checkins")

    @classmethod
    def from_model(cls: Type[Self], checkin: Checkin) -> Self:
        return CheckinEntity(
            id=checkin.id, user_id=checkin.user.id, timestamp=checkin.timestamp
        )

    def to_model(self) -> Checkin:
        return Checkin(id=self.id, user=self.user.to_model(), timestamp=self.timestamp)

    # TODO: Uncomment after implementing CheckinDetails
    # def to_model_details(self) -> CheckinDetails:
    #     return CheckinDetails(
    #         id=self.id, timestamp=self.timestamp, user=self.user.to_model()
    #     )
