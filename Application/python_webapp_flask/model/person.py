import uuid

import attr


@attr.s(auto_attribs=True)
class Person(object):
    id: uuid.uuid4()
