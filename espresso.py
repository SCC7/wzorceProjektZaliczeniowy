from napoj import napojPrzepis


class espresso(napojPrzepis):
    def zdefiniuj_wymagania(self):
        return 'mlynek komora_cisnieniowa';

    def wykonaj_pierwszy_krok(self, rozmiarKawy):
        rozkaz = dict(urzadzenie='mlynek', dzialanie='mielenie', ilosc=50 * rozmiarKawy);
        return rozkaz;

    def wykonaj_drugi_krok(self, ilosc):
        rozkaz = dict(urzadzenie='komora_cisnieniowa', dzialanie='parzenie');
        return rozkaz;

    def wykonaj_trzeci_krok(self, ilosc):
        return;

    def podaj_nazwe(self):
        return 'espresso';

    def podaj_rodzaj(self):
        return 'n';