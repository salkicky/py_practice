#encoding: shift-jis

class Event:
    def __init__(self, pid):
        self._pid = pid
        self._setting = [{'a':1, 'b':2}]*10

