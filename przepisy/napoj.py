import abc


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

    def podaj_rozmiar(self, rozmiar_napoju):
        return self._imp.rozmiar(rozmiar_napoju);


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
    def nazwa(self):
        pass

    @abc.abstractmethod
    def rodzaj(self):
        pass

    @abc.abstractmethod
    def rozmiar(self, rozmiar):
        pass