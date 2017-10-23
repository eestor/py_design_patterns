

from importlib import import_module
from inspect import getmembers, isabstract, isclass
from abs_factory import AbsFactory


def load_factory(factory_name):

    try:
        factory_module = import_module(factory_name, package='factories')
        print("FACTORY_MODULE".format(factory_module))
    except ImportError:
        factory_module = import_module('null_factory', package='factories')

    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))
    print(classes)
    for name, _class in classes:
        print(name, _class)
        if issubclass(_class, AbsFactory):
            return _class
