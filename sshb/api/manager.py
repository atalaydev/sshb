class Manager():

    def __init__(self, command):
        commands = {
            'add': (lambda: self.add()),
            'update': (lambda: print('update')),
            'delete': (lambda: print('delete')),
        }

        func = commands.get(command, lambda: print('Invalid action requested!'))
        func()
        
    def add(self):
        print('add')
