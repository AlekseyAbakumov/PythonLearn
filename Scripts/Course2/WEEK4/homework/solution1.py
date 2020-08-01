class EventGet:
    def __init__(self, kind):
        self.kind = kind
        self.action = 'get'


class EventSet:
    def __init__(self, kind):
        self.kind = kind
        self.action = 'set'


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj_, event):
        if self.__successor is not None:
            return self.__successor.handle(obj_, event)


class IntHandler(NullHandler):
    def handle(self, obj_, event):
        if event.kind == int or type(event.kind) == int:
            if event.action == 'set':
                obj_.integer_field = event.kind
            elif event.action == 'get':
                return obj_.integer_field
        else:
            return super().handle(obj_, event)


class FloatHandler(NullHandler):
    def handle(self, obj_, event):
        if event.kind == float or type(event.kind) == float:
            if event.action == 'set':
                obj_.float_field = event.kind
            elif event.action == 'get':
                return obj_.float_field
        else:
            return super().handle(obj_, event)


class StrHandler(NullHandler):
    def handle(self, obj_, event):
        if event.kind == str or type(event.kind) == str:
            if event.action == 'set':
                obj_.string_field = event.kind
            elif event.action == 'get':
                return obj_.string_field
        else:
            return super().handle(obj_, event)