import uuid

import attr


@attr.s(auto_attribs=True)
class Room(object):
    id: uuid.uuid4()
    name: str
    position: int
    description: str
