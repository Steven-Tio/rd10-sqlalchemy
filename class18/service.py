from .entities import Session, UserEntity, CheckinEntity
from .models import User, Checkin
from datetime import datetime


class UserService:
    """Business logic for User registration and user lookup."""

    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def register(self, user: User) -> User:
        user_entity: UserEntity = UserEntity.from_model(user)
        self._session.add(user_entity)
        self._session.commit()
        return user_entity.to_model()

    def get(self, pid: int) -> User:  # TODO: Change to UserDetails
        user_entity = self._session.get(UserEntity, pid)
        if user_entity:
            return user_entity.to_model()  # TODO: Change to model details
        else:
            raise ValueError(f"No user found with PID: {pid}")


class CheckinService:
    """Business logic for creating checkins and getting a single checkin."""

    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def checkin(self, user: User) -> Checkin:  # TODO: Change to return CheckinDetails
        checkin_entity = CheckinEntity(user_pid=user.pid, timestamp=datetime.now())
        self._session.add(checkin_entity)
        self._session.commit()
        return checkin_entity.to_model()  # TODO: Change to model details

    def get(self, id: int) -> Checkin:  # TODO: Change to return CheckinDetails
        user_entity = self._session.get(CheckinEntity, id)
        return user_entity.to_model()  # TODO: Change to model details
