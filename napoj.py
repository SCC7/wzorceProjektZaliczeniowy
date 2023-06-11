import abc


# bridge
class napoj:

    def __init__(self, implementation):
        self._implementation = implementation;

    def zdefiniuj_wymagania(self):
        self._implementation.zdefiniuj_wymagania();

    def wykonaj_pierwszy_krok(self, ilosc):
        self._implementation.wykonaj_pierwszy_krok();

    def wykonaj_drugi_krok(self, ilosc):
        self._implementation.wykonaj_drugi_krok();

    def wykonaj_trzeci_krok(self, ilosc):
        self._implementation.wykonaj_trzeci_krok();

    def podaj_nazwe(self):
        self._implementation.podaj_nazwe();

    def podaj_rodzaj(self):
        self._implementation.podaj_rodzaj();

# implementacja abstrakcyjna
class napojPrzepis(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def zdefiniuj_wymagania(self):
        pass

    @abc.abstractmethod
    def wykonaj_pierwszy_krok(self, ilosc):
        pass

    @abc.abstractmethod
    def wykonaj_drugi_krok(self, ilosc):
        pass

    @abc.abstractmethod
    def wykonaj_trzeci_krok(self, ilosc):
        pass

    @abc.abstractmethod
    def podaj_nazwe(self):
        pass

    @abc.abstractmethod
    def podaj_rodzaj(self):
        pass