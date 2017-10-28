from abs_subject import AbsSubject

class Alarm(AbsSubject):

    _open_alarms = -1
    _closed_alarms = -1

    @property
    def open_alarms(self):
        return self._open_alarms

    @property
    def closed_alarms(self):
        return self._closed_alarms

    def set_alarms(self, open_alarms, closed_alarms):
        self._open_alarms = open_alarms
        self._closed_alarms = closed_alarms
        self.notify()

