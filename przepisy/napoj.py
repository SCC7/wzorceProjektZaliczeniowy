from abc import abstractmethod, ABCMeta


# bridge
class napoj:

    def __init__(self, imp):
        self._imp = imp

    def zdefiniuj_wymagania(self):
        return self._imp.zdefiniuj_wymagania();

    def wykonaj_pierwszy_krok(self, ilosc):
        return self._imp.wykonaj_pierwszy_krok(ilosc);

    def wykonaj_drugi_krok(self, ilosc):
        return self._imp.wykonaj_drugi_krok(ilosc);

    def wykonaj_trzeci_krok(self, ilosc):
        return self._imp.wykonaj_trzeci_krok(ilosc);

    def podaj_nazwe(self):
        return self._imp.nazwa();

    def podaj_rodzaj(self):
        return self._imp.rodzaj();

    def podaj_rozmiar(self):
        return self._imp.podaj_rozmiar();


# implementacja abstrakcyjna
class napojPrzepis(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, rozmiar):
        pass;

    @abstractmethod
    def zdefiniuj_wymagania(self):
        pass

    @abstractmethod
    def wykonaj_pierwszy_krok(self, ilosc):
        pass

    @abstractmethod
    def wykonaj_drugi_krok(self, ilosc):
        pass

    @abstractmethod
    def wykonaj_trzeci_krok(self, ilosc):
        pass

    @abstractmethod
    def nazwa(self):
        pass

    @abstractmethod
    def rodzaj(self):
        pass

    @abstractmethod
    def podaj_rozmiar(self):
        pass