from rozne.progressbar import pasek_postepu_instant
from urzadzenia.urzadzenie import Urzadzenie


class komoraCisnieniowa(Urzadzenie):
    wprowadzona_substancja = 0;
    rodzaj_zawartosci = None;

    def __init__(self):
        self.oproznianie();

    def wypelnianie(self, rodzaj_zawartosci, ilosc):
        if ilosc <= 0:
            raise ValueError('Komora nie została napełniona');
        self.wprowadzona_substancja = ilosc;
        self.rodzaj_zawartosci = rodzaj_zawartosci;
        return;

    def dzialanie(self):
        # tryb działania jest zależny od wprowadzonej substancji
        # w prawdziwym ekspresie działoby się tutaj coś ciekawszego
        # print('WPR SUBT: ')
        # print(self.wprowadzona_substancja)
        timer = 1;
        substancja = int(self.wprowadzona_substancja)
        # print('SUBST: ')
        # print(substancja)
        # print(self.rodzaj_zawartosci);
        if self.rodzaj_zawartosci == 'kawa':
            timer = substancja * 2;
            pasek_postepu_instant(dlugosc=timer, prefixProcesu='Postęp parzenia kawy');
            print('Zaparzono kawę')
            self.rodzaj_zawartosci = 'płynna kawa'
            return;
        elif self.rodzaj_zawartosci == 'czekolada':
            timer = substancja;
            pasek_postepu_instant(dlugosc=timer, prefixProcesu='Postęp parzenia czekolady');
            print('Zaparzono czekoladę')
            self.rodzaj_zawartosci = 'płynna czekolada'
            return;
        elif self.rodzaj_zawartosci == 'woda':
            timer = substancja / 2;
            pasek_postepu_instant(dlugosc=timer, prefixProcesu='Postęp nalewania gorącej wody');
            print('Nalano gorącej wody')
            self.rodzaj_zawartosci = 'gorąca woda'
            return;
        elif self.rodzaj_zawartosci == 'mleko':
            timer = substancja / 2;
            pasek_postepu_instant(dlugosc=timer, prefixProcesu='Postęp nalewania gorącego mleka');
            print('Nalano gorącego mleka')
            self.rodzaj_zawartosci = 'gorące mleko'
            return;

        return;

    def oproznianie(self):
        print('Trwa opróżnianie komory ciśnieniowej');
        # return self.wprowadzona_substancja;
        return dict(substancja=self.rodzaj_zawartosci, ilosc=self.wprowadzona_substancja);
