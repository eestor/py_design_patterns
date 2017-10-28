

from importlib import import_module
from inspect import getmembers, isabstract, isclass
from abs_factory import AbsFactory


def load_factory(factory_name):

    try:
        factory_module = import_module(factory_name, 'full')
        #print("FACTORY_MODULE: {}".format(factory_module))
        #FACTORY_MODULE: <module 'esx_factory' from 'full/esx_factory.py'>
    except ImportError:
        factory_module = import_module('null_factory', 'full')

    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))
    #print(classes)
    #('Esx', <class 'esx.Esx'>), ('EsxFactory', <class 'esx_factory.EsxFactory'>)]
    for name, _class in classes:
        #print(name, _class)
        # loop1=Esx <class 'esx.Esx'>
        # loop2=sxFactory <class 'esx_factory.EsxFactory'>
        if issubclass(_class, AbsFactory):
            #print("RETURNED CLASS: {}".format(_class))
            #RETURNED CLASS: <class 'esx_factory.EsxFactory'>
            return _class()
