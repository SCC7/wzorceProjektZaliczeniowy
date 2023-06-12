from przepisy.napoj import napojPrzepis


class Americano(napojPrzepis):
    rozmiar = {'m':150, 'l':300}
    # def __init__(self):
    #     print('DEBUG: espresso init');
    #     return;

    def zdefiniuj_wymagania(self):
        return 'mlynek komora_cisnieniowa';

    def wykonaj_pierwszy_krok(self, rozmiar_kawy):
        rozkaz = dict(urzadzenie='mlynek', ilosc=rozmiar_kawy);
        return rozkaz;

    def wykonaj_drugi_krok(self, ilosc):
        rozkaz = dict(urzadzenie='komora_cisnieniowa', rodzaj='zmielona_kawa');
        return rozkaz;

    def wykonaj_trzeci_krok(self, ilosc):
        rozkaz = dict(urzadzenie='komora_cisnieniowa', rodzaj='woda');
        return rozkaz;

    def nazwa(self):
        return 'americano';

    def rodzaj(self):
        return 'n';

    def rozmiar(self, rozmiar):
        if rozmiar == 'm':
            return 150;
        if rozmiar == 'l':
            return 300;
