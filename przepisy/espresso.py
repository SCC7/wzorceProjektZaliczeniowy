from przepisy.napoj import napojPrzepis


class Espresso(napojPrzepis):

    def __init__(self, rozmiar):
        # print('DEBUG: espresso init');
        # print(f'DEBUG typ wartości rozmiar to {rozmiar}')
        if not isinstance(rozmiar, str):
            raise TypeError('Rozmiar kubka musi być podany jako litera!');
        if not rozmiar == 'm' and not rozmiar == 'l':
            raise ValueError('Rozmiar kubka musi być "m" albo "l"!')
        self.rozmiar = rozmiar;
        return;

    def zdefiniuj_wymagania(self):
        return 'mlynek komora_cisnieniowa';

    def wykonaj_pierwszy_krok(self, ilosc):
        rozkaz = dict(urzadzenie='mlynek', substancja='ziarna_kawy', ilosc=self.podaj_rozmiar());
        return rozkaz;

    def wykonaj_drugi_krok(self, ilosc):
        rozkaz = dict(urzadzenie='komora_cisnieniowa', substancja='zmielona_kawa', ilosc=self.podaj_rozmiar());
        return rozkaz;

    def wykonaj_trzeci_krok(self, ilosc):
        return;

    def nazwa(self):
        return 'espresso';

    def rodzaj(self):
        return 'n';

    def podaj_rozmiar(self):
        if self.rozmiar == 'm':
            return 50;
        if self.rozmiar == 'l':
            return 100;
        raise ValueError('Brak rozmiaru?')

