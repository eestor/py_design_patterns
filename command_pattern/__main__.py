

from update_cluster_membership import UpdateClusterMembership
from update_dc_membership import UpdateDc
from no_command import NoCommand
import sys

def get_commands():
    commands = (UpdateDc, UpdateClusterMembership)
    #print(commands)
    #print(dict([cls.name, cls] for cls in commands))
    #<class 'update_dc_membership.UpdateDc'>, <class 'update_cluster_membership.UpdateClusterMembership'>)
    #{'UpdateDc': <class 'update_dc_membership.UpdateDc'>, 'UpdateCluster': <class 'update_cluster_membership.UpdateClusterMembership'>}
    return dict([cls.name, cls] for cls in commands)

def print_usage(commands):
    print('Usage: python -m Command CommandName [arguments]')
    print('Command: ')
    for command in commands.values():
        print('  {} : {}'.format(command.name, command.description))


def parse_command(commands, args):
    command = commands.setdefault(args[0], NoCommand)
    return command(args)


commands = get_commands()
if len(sys.argv) < 3:
    print_usage(commands)
    exit()


command = parse_command(commands, sys.argv[1:])
command.execute()