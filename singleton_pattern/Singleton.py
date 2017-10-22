class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s_instance1 = Singleton()
s_instance1.name = "Singleton1"

s_instance2 = Singleton()
s_instance2.name

print("Printing class instance 1 \"name\" attibute %s" % s_instance1.name)
print("Printing class instance 2 \"name\" attibute %s" % s_instance2.name)

# notes: limitation of Singleton - when used as a  subclass , the subclass will not follow as singleton (solution is to use BorgSingleton pattern)
