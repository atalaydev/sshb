import os
import sys
from sshb.api import SSHB, Manager
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import radiolist_dialog


def main(args: list = None) -> int:
    """ The main sshb routine. """
    if len(args) > 0:
        if args[0] == 'manager':
            return Manager(
                radiolist_dialog(
                    title='SSHB Manager',
                    text='Yes, sir! Tell me the action:',
                    values=[
                        ('add', 'Add new host.'),
                        ('update', 'Update an existing host.'),
                        ('delete', 'Delete an existing host.')
                    ]
                ).run()
            )
        else:
            print('Invalid command supplied!')
        return 0

    instance = SSHB()
    return instance(
        prompt(
            'Please start typing hostname or press \'tab\' to activate auto-complete: ',
            completer=WordCompleter(
                instance.hosts
            )
        )
    )


if __name__ == "__main__":
    os.system('cls||clear')
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit(0)
