from event_alarms import EventAlarms
from alarm import Alarm



with Alarm() as a:
    with EventAlarms(a):
        a.set_alarms(25, 10)
        a.set_alarms(20, 11)

print("exited context manager...")
a.set_alarms(10, 20)