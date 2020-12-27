import sys
from sshb.api import SSHB, Manager
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def main(args: list = None) -> int:
    """ The main sshb routine. """
    if len(args) > 0:
        if args[0] == 'manager':
            return Manager(
                prompt(
                    'Yes, sir! Tell me the action (\'add\', \'delete\', \'update\'): ',
                    completer=WordCompleter(
                        ('add', 'update', 'delete')
                    )
                )
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
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit(0)
