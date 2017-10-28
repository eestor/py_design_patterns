

from abs_observer import AbsObserver

class EventAlarms(AbsObserver):

    open_alarms = -1
    closed_alarms = -1

    def __init__(self, alarm):
        self._alarm = alarm
        alarm.attach(self)

    def update(self):
        self.open_alarms = self._alarm.open_alarms
        self.closed_alarms = self._alarm.closed_alarms
        self.display()


    def display(self):
        print('Open Alarms: {}'.format(self.open_alarms))
        print('Closed Alarms: {}'.format(self.closed_alarms))


    def __exit__(self, exc_type, exc_val, exc_tb):
        self._alarm.detach(self)
