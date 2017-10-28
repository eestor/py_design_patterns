from event_alarms import EventAlarms
from alarm import Alarm

a = Alarm()
event = EventAlarms(a)
a.set_alarms(10, 20)
a.set_alarms(11, 20)
a.set_alarms(10, 25)

print("Detaching alarm observer")
a.detach(event)
a.set_alarms(110,299)

