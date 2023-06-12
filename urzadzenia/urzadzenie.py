from abc import ABC, abstractmethod


class Urzadzenie(ABC):
    @abstractmethod
    def __init__(self):
        pass;

    @abstractmethod
    def wypelnianie(self, rodzaj_substancji, ilosc):
        pass;

    @abstractmethod
    def dzialanie(self):
        pass;

    @abstractmethod
    def oproznianie(self):
       pass;

    @abstractmethod
    def zidentyfikuj(self):
        pass;