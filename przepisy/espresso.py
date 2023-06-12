from przepisy.napoj import napojPrzepis


class Espresso(napojPrzepis):
    # def __init__(self):
    #     print('DEBUG: espresso init');
    #     return;

    def zdefiniuj_wymagania(self):
        return 'mlynek komora_cisnieniowa';

    def wykonaj_pierwszy_krok(self, rozmiar_kawy):
        rozkaz = dict(urzadzenie='mlynek', substancja='ziarna_kawy', ilosc=rozmiar_kawy);
        return rozkaz;

    def wykonaj_drugi_krok(self, ilosc):
        rozkaz = dict(urzadzenie='komora_cisnieniowa', substancja='zmielona_kawa');
        return rozkaz;

    def wykonaj_trzeci_krok(self, ilosc):
        return;

    def nazwa(self):
        return 'espresso';

    def rodzaj(self):
        return 'n';

    def rozmiar(self, rozmiar):
        if rozmiar == 'm':
            return 50;
        if rozmiar == 'l':
            return 100;
