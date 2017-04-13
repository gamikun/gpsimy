from command import Command

class InputType:
    PANIC_BUTTON = 0
    OTHER = 777


class EventType:

    INPUT_TOO_LOW = 2
    INPUT_TOO_HIGH = 3
    INPUT_TURNED_ON = 4
    INPUT_TURNED_OFF = 5
    DOOR_OPENED = 6
    DOOR_CLOSED = 7


class Event(object):
    __slots__ = ['timestamp', 'position']

    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])


class InputChanged(Event):
    __slots__ = ['status', 'type']

    def __init__(self, **kwargs):
        super(self, InputEvent).__init__(**kwargs)
        self.status = kwargs.get('status', 0)
        self.type = kwargs.get('type', None)

    @property
    def turned_in(self):
        return self.status

    @property
    def turned_off(self):
        return not self.status


class PanicButton(Event):
    pass

