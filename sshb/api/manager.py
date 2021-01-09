from prompt_toolkit.shortcuts import input_dialog
from .core import Host


class Manager():

    def __init__(self, command):
        commands = {
            'add': self.add,
            'update': (lambda: print('update')),
            'delete': (lambda: print('delete')),
        }

        func = commands.get(command, lambda: print('Invalid action requested!'))
        func()
        
    def add(self):
        for attribute in Host.__attributes__:
            input_dialog(
                title=Host.__prompts__.get(attribute)
            ).run()