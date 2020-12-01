from pathlib import Path
from .exceptions import UnsupportedAttributeException
from .exceptions import ImproperlyConfiguredException


class Host():
    __attributes__ = ('host', 'user', 'port', 'identity')

    def __init__(self, attributes: dict, _globals: dict) -> None:
        for attribute in list(attributes.keys()):
            if attribute not in self.__attributes__:
                raise UnsupportedAttributeException(
                    f'Host attribute \'{attribute}\' is not supported.'
                )

        for attribute in self.__attributes__:
            if attribute in list(attributes.keys()):
                setattr(self, attribute, attributes.get(attribute))
            elif hasattr(_globals, attribute):
                setattr(self, attribute, _globals.__dict__.get(attribute))
            else:
                raise ImproperlyConfiguredException(
                    f'Host attribute \'{attribute}\' is required.'
                )

    def __repr__(self) -> str:
        return f'<Host({self.__dict__})>'

    def __setattr__(self, key: str, value: str) -> None:
        if key == 'identity':
            value = Path.home() / value

        super().__setattr__(key, value)
