from przepisy.napoj import napojPrzepis


class Americano(napojPrzepis):
    # rozmiar = {'m':150, 'l':300}
    # def __init__(self):
    #     print('DEBUG: espresso init');
    #     return;
    def __init__(self, rozmiar):
        # print('DEBUG: espresso init');
        # print(f'DEBUG typ wartości rozmiar to {rozmiar}')
        if not isinstance(rozmiar, str):
            raise TypeError('Rozmiar kubka musi być podany jako litera');
        self.rozmiar = rozmiar;
        return;

    def zdefiniuj_wymagania(self):
        return 'mlynek komora_cisnieniowa';

    # def wykonaj_pierwszy_krok(self, rozmiar_kawy):
    #     rozkaz = dict(urzadzenie='mlynek', ilosc=rozmiar_kawy);
    #     return rozkaz;
    def wykonaj_pierwszy_krok(self, ilosc):
        rozkaz = dict(urzadzenie='mlynek', substancja='ziarna_kawy', ilosc=self.podaj_rozmiar()/2);
        return rozkaz;

    def wykonaj_drugi_krok(self, ilosc):
        rozkaz = dict(urzadzenie='komora_cisnieniowa', substancja='zmielona_kawa', ilosc=self.podaj_rozmiar()/2);
        return rozkaz;

    def wykonaj_trzeci_krok(self, ilosc):
        rozkaz = dict(urzadzenie='komora_cisnieniowa', substancja='woda', ilosc=self.podaj_rozmiar()/2);
        return rozkaz;

    def nazwa(self):
        return 'americano';

    def rodzaj(self):
        return 'n';

    def podaj_rozmiar(self):
        if self.rozmiar == 'm':
            return 150;
        if self.rozmiar == 'l':
            return 300;
