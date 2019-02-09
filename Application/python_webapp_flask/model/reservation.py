import uuid

import attr
import pendulum


@attr.s(auto_attribs=True)
class Reservation(object):
    id = uuid.uuid4()
    interval = pendulum.duration()
