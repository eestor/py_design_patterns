
from object_factory import VcObjectFactory


obj = VcObjectFactory.create_task_for_obj('vm2')
obj.get_data('getting data from couchbase DB')