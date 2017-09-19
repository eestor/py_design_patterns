

class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class Child(Borg):
    # _shared_state = {}  # this will disable inheriting all shared attributes
    pass


borg1 = Borg()
borg1.name = "Borg Singleton Example1"
borg2 = Borg()
print("Printing class instance 1 \"name\" attribute (w/ name set during instantiation) : %s " % borg1.name)
print("Printing class instance 2 \"name\" attribute : %s " % borg2.name)

borg2.name = "Borg Singleton Example2"
print("Printing class instance 2 \"name\" attribute (w/ attribute name set during instantiation) : %s " % borg2.name)
print("Printing class instance 1 \"name\" attribute : %s " % borg1.name)

child = Child()
print("Printing subclass instance \"name\" attribute : %s " % child.name)