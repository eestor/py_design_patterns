
from inspect import getmembers, isclass, isabstract
import simple_factory

class ObjectFactory(object):

    vc_objects = {}

    def __init__(self):
        self.load_objects()


    def load_objects(self):

        # get class objects
        # [('Esx', <class 'simple_factory_pattern.esx.Esx'>),
        # ('NullObject', <class 'simple_factory_pattern.null_object.NullObject'>),
        # ('Vm', <class 'simple_factory_pattern.vm.Vm'>)]

        classes = getmembers(simple_factory,
                             lambda m: isclass(m) and not isabstract(m))


        for name, _type in classes:
            #print("Name: {},  Type: {}".format(name, _type))
            #Name: Esx, Type: < class 'simple_factory_pattern.esx.Esx'>
            #Name: NullObject, Type: < class 'simple_factory_pattern.null_object.NullObject'>
            #Name: Vm, Type: < class 'simple_factory_pattern.vm.Vm'>
            if isclass(_type) and issubclass(_type, simple_factory.AbsVcObject):
                self.vc_objects.update([[name, _type]])

        # print(self.vc_objects)
        # {'Esx': <class 'simple_factory_pattern.esx.Esx'>,
        # 'NullObject': <class 'simple_factory_pattern.null_object.NullObject'>,
        # 'Vm': <class 'simple_factory_pattern.vm.Vm'>}

    def create_instance(self, obj_name):
        if obj_name in self.vc_objects:
            return self.vc_objects[obj_name]()
        else:
            return simple_factory.NullObject(obj_name)

