import sys
from sshb.api import SSHB
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def main(args: list = None) -> int:
    """ The main sshb routine. """
    instance = SSHB()
    return instance(
        prompt(
            'Please start typing hostname or press \'tab\' to auto-complete: ',
            completer=WordCompleter(
                instance.hosts
            )
        )
    )


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
