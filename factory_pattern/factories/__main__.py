from loader import load_factory

for factory_name in 'esx_factory':

    factory = load_factory(factory_name)
    vc_object = factory.create_vc_object()

    vc_object.start()
    vc_object.shutdown()