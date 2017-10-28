
from object_factory import ObjectFactory

factory = ObjectFactory()

for obj_name in "Esx", "Vm", "Ds":

    obj = factory.create_instance(obj_name)
    obj.start()
    obj.shutdown()