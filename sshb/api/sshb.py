import os
import yaml
from pathlib import Path
from .core import _Global, Host


class SSHB():

    def __init__(self, config_file: str = 'sshb.yaml') -> None:
        self.__hosts = {}
        with open(Path.home() / config_file, 'r') as stream:
            try:
                data = yaml.load(stream, Loader=yaml.FullLoader)
                if 'globals' in data:
                    self.__build_globals(data.get('globals'))
                else:
                    self.__globals = None
                self.__build_hosts(data.get('hosts'))
            except Exception:
                raise

    def __build_globals(self, globals: _Global) -> None:
        self.__globals = _Global(globals)

    def __build_hosts(self, hosts: dict) -> None:
        for host in hosts:
            self.__hosts[list(host.keys())[0]] = Host(
                host.get(list(host.keys())[0]),
                self.__globals
            )

    def __call__(self, host: str) -> int:
        os.system(f'ssh {self.__hosts.get(host).user}'
                  f'@{self.__hosts.get(host).host}'
                  f' -p {self.__hosts.get(host).port}'
                  f' -i {self.__hosts.get(host).identity}'
                  )
        return 0

    @property
    def hosts(self) -> list:
        return list(self.__hosts.keys())
