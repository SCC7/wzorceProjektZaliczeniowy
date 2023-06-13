from przepisy.napoj import napojPrzepis


class KawaZMlekiem(napojPrzepis):

    def __init__(self, rozmiar):
        if not isinstance(rozmiar, str):
            raise TypeError('Rozmiar kubka musi być podany jako litera');
        self.rozmiar = rozmiar;
        return;

    def zdefiniuj_wymagania(self):
        return 'mlynek komora_cisnieniowa';

    def wykonaj_pierwszy_krok(self, ilosc):
        rozkaz = dict(urzadzenie='mlynek', substancja='ziarna_kawy', ilosc=self.podaj_rozmiar()*2/3);
        return rozkaz;

    def wykonaj_drugi_krok(self, ilosc):
        rozkaz = dict(urzadzenie='komora_cisnieniowa', substancja='zmielona_kawa', ilosc=self.podaj_rozmiar()*2/3);
        return rozkaz;

    def wykonaj_trzeci_krok(self, ilosc):
        rozkaz = dict(urzadzenie='komora_cisnieniowa', substancja='mleko', ilosc=self.podaj_rozmiar() / 3);
        return rozkaz;

    def nazwa(self):
        return 'kawa z mlekiem';

    def rodzaj(self):
        return 'n';

    def podaj_rozmiar(self):
        if self.rozmiar == 'm':
            return 150;
        if self.rozmiar == 'l':
            return 300;
