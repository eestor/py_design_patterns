
from abs_command import AbsCommand
from abs_update_command import AbsUpdateCommand

class UpdateDc(AbsCommand, AbsUpdateCommand):
    name = 'UpdateDc'
    description = 'Update objects DC membership'

