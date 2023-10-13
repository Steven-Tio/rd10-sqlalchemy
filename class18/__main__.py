from .entities import Base, create_engine, sessionmaker
from .models import User, Checkin
from .service import UserService, CheckinService


def main() -> None:
    """Entrypoint of Program"""
    session_factory = establish_database("sqlite+pysqlite:///:memory:")
    session = session_factory()
    user_service = UserService(session)
    checkin_service = CheckinService(session)
    populate_demo_data(user_service, checkin_service)

    # TODO #1: Try changing line below to get Amy Ambassador to print
    user_details = user_service.get(999999999)
    print(user_details.model_dump_json())

    # TODO #3: Get a checkin with id 1 via checkin_service and print its model_dump_json


def establish_database(dsn: str) -> sessionmaker:
    """Connect to the database and create tables based on Entity metadata."""
    engine = create_engine(dsn, echo=False)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


def populate_demo_data(
    user_service: UserService, checkin_service: CheckinService
) -> None:
    """Prepopulate some users and randomized checkins into the system."""
    users: list[User] = [
        User(pid=111111111, first_name="Sally", last_name="Student"),
        User(pid=777777777, first_name="Amy", last_name="Ambassador"),
        User(pid=999999999, first_name="Rhonda", last_name="Root"),
    ]
    for user in users:
        user_service.register(user)

    from random import randint

    # TODO #2: Use the `checkin_service` parameter to make 30 demo Checkins.
    # Each checkin should made at random for one of the three User models above.


if __name__ == "__main__":
    main()
