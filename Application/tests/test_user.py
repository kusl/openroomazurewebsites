import hashlib
import uuid

from python_webapp_flask.model.person import Person, LoginType


def create_person():
    person = Person(
        id=uuid.uuid4(),
        name="Katy Perry",
        email="katy@perry.love",
        password=hashlib.sha512("hunter2".encode('utf-8') + str(uuid.uuid4()).encode('utf-8')).hexdigest(),
        login_type=LoginType.PASSWORD
    )
    return person


def test_person_name():
    katy_perry = create_person()
    assert katy_perry.name == "Katy Perry"
