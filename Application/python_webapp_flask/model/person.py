import uuid
from enum import Enum, auto

import attr
import bcrypt


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

    def __attrs_post_init__(self):
        self.password = bcrypt.hashpw(self.password, bcrypt.gensalt())
