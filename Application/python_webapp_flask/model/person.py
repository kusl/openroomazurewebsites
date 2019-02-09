import uuid
from enum import Enum, auto

import attr


class LoginType(Enum):
    PASSWORD = auto()
    LDAP = auto()


@attr.s(auto_attribs=True)
class Person(object):
    id: uuid.uuid4()
    name: str
    email: str
    password: str
    login_type: LoginType
