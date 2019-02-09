import uuid

import bcrypt

from python_webapp_flask.model.person import Person, LoginType


def create_person():
    person = Person(
        id=str(uuid.uuid4()),
        name="Katy Perry",
        email="katy@perry.love",
        password="hunter2",
        login_type=LoginType.PASSWORD
    )
    return person


def test_person_name():
    katy_perry = create_person()
    assert katy_perry.name == "Katy Perry"


def test_person_password():
    katy_perry = create_person()
    print(katy_perry.password)
    assert bcrypt.checkpw("hunter2".encode("utf-8"), katy_perry.password)
