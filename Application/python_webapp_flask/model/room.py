import attr


@attr.s(auto_attribs=True)
class Room(object):
    id: str
    name: str
    position: int
    description: str
