from enum import Enum;
from abc import ABCMeta, abstractmethod;

State = Enum('State', 'new running sleeping restart zombie');

class User:
    pass;

class Process:
    pass;

class File:
    pass;

class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass;

    def __str__(self):
        return self.name;

    @abstractmethod
    def boot(self):
        pass;

    @abstractmethod
    def kill(self, restart=True):
        pass;

class FileServer(Server):
    def __init__(self):
        self.name='FileServer';
        self.state=State.new;

    def boot(self):
        print(f"Bootowanie {self}");
        self.state=State.running;

    def kill(self, restart=True):
        print(f"Usuwanie {self}");
        self.state = State.restart if restart else State.zombie;

    def create_file(self,user,name,permission):
        print(f"proba utworzenia pliku '{name}' dla uzytkownika '{user}' z uprawnieniami '{permission}'.");

class ProcessServer(Server):
    def __init__(self):
        self.name='ProcessServer';
        self.state=State.new;

    def boot(self):
        print(f"Bootowanie {self}");
        self.state=State.running;

    def kill(self, restart=True):
        print(f"Usuwanie {self}");
        self.state = State.restart if restart else State.zombie;

    def create_process(self,user,name,):
        print(f"proba utworzenia procesu '{name}' dla uzytkownika '{user}'.");

class WindowServer:
    pass;

class NetworkServer:
    pass;

class OperatingSystem:
    def __init__(self):
        self.fs = FileServer();
        self.ps = ProcessServer();

    def start(self):
        [i.boot() for i in (self.fs, self.ps)];

    def createFile(self, name, user, permission):
        return self.fs.create_file(name, user, permission);

    def createProcess(self, name, user):
        return self.ps.create_process(name, user);

def main():
    os = OperatingSystem();
    os.start();
    os.createFile('foo','Kuba','-rw-r-r');
    os.createProcess('bar','Kubba');

if __name__ == '__main__':
    main();