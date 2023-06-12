from rozne.progressbar import pasek_postepu_instant
from urzadzenia.urzadzenie import Urzadzenie


class Mlynek(Urzadzenie):
    ziarna_kawy = 0;
    zmielona_kawa = 0;

    def __init__(self):
        self.oproznianie();

    def wypelnianie(self, rodzaj_substancji, ilosc):
        if rodzaj_substancji != 'ziarna_kawy':
            raise TypeError('Nieznana substancja w młynku!')
        if ilosc <= 0:
            raise ValueError('Nie można zmielić zerowej ilości ziaren kawy');
        self.ziarna_kawy = ilosc;
        return;

    def dzialanie(self):
        # self.ziarna_kawy = ilosc;
        # if self.ziarna_kawy < 0:
        #     raise ValueError('Nie można zmielić zerowej ilości ziaren kawy');

        # zmiel ziarna
        # w prawdziwym ekspresie działoby się tutaj coś ciekawszego
        self.zmielona_kawa = self.ziarna_kawy;

        pasek_postepu_instant(dlugosc=self.ziarna_kawy, prefixProcesu='Postęp mielenia ziaren kawy');

        # points = list(range(0, self.ziarna_kawy));
        # pointsLength = len(points);
        # nazwaProcesu = 'Postęp mielenia ziaren kawy:'
        # printProgressBar(0, pointsLength, prefix=nazwaProcesu, length=50);
        # for i, points in enumerate(points):
        #     time.sleep(0.1);
        #     printProgressBar(0 + i, pointsLength, prefix=nazwaProcesu, length=50);
        # printProgressBar(pointsLength, pointsLength, prefix=nazwaProcesu, length=50);

        print('Zmielono kawę');
        return;
        # return zmielona_kawa;

    def oproznianie(self):
        print('Trwa opróżnianie młynka');
        return dict(substancja='zmielona_kawa',ilosc=self.zmielona_kawa);
        # zawarte_ziarna = self.ziarna_kawy;
        # zawarte_mielone = self.zmielona_kawa;
        #
        # if (zawarte_ziarna <= 0):
        #     if (zawarte_mielone <= 0):
        #         return;
        #     else:
        #         self.zmielona_kawa = 0;
        #         return zawarte_mielone;
        # else:
        #     if (zawarte_mielone <= 0 ):
        #         self.ziarna_kawy = 0;
        #         return zawarte_ziarna;
        #     else:
        #         self.ziarna_kawy = 0;
        #         self.zmielona_kawa = 0;
        #         return zawarte_ziarna, zawarte_mielone;

    def zidentyfikuj(self):
        return 'młynek';
