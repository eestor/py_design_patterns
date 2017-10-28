
from abs_command import AbsCommand
from abs_update_command import AbsUpdateCommand

class UpdateClusterMembership(AbsCommand, AbsUpdateCommand):
    name = 'UpdateCluster'
    description = 'Update Objects Cluster Membership'

    def __init__(self, args):
        self._new_cluster_membership = args[1]


    def execute(self):
        old_cluster = 'cluster1'
        print('Updated Cluster Membership')
        print('Updated cluster membership from {} to {}'.format(old_cluster, self._new_cluster_membership))

