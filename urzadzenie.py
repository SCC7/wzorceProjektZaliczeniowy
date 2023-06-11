import time
from abc import ABC, abstractmethod

from progressbar import pasek_postepu_instant


class Urzadzenie(ABC):
    @abstractmethod
    def __init__(self):
        pass;

    @abstractmethod
    def wypelnianie(self, ilosc):
        pass;

    @abstractmethod
    def dzialanie(self):
        pass;

    @abstractmethod
    def oproznianie(self):
       pass;