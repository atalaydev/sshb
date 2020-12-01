class _Global():
    __attributes__ = ('host', 'user', 'port', 'identity')

    def __init__(self, attributes):
        for attribute in attributes:
            setattr(self, attribute, attributes.get(attribute))

    def __repr__(self):
        return f'<_Global({self.__dict__})>'
