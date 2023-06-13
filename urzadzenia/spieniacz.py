from rozne.progressbar import pasek_postepu_instant
from urzadzenia.urzadzenie import Urzadzenie


class Spieniacz(Urzadzenie):

    def __init__(self):
        self.oproznianie();
        self.mleko = 0;
        self.rodzaj_substancji = '';

    def wypelnianie(self, rodzaj_substancji, ilosc):
        if rodzaj_substancji != 'mleko':
            raise TypeError('Nieznana substancja w spieniaczu!')
        if ilosc <= 0:
            raise ValueError('Nie można spienić zerowej ilości mleka');
        self.mleko = ilosc;
        self.rodzaj_substancji = rodzaj_substancji;
        return;

    def dzialanie(self):
        # spieniacz pracuje
        pasek_postepu_instant(dlugosc=self.mleko, prefix_procesu='Postęp spieniania mleka');

        # print('Spieniono mleko');
        self.rodzaj_substancji = 'spienione_mleko';
        return;

    def oproznianie(self):
        # print('Trwa opróżnianie spieniacza');
        return dict(substancja=self.rodzaj_substancji, ilosc=self.mleko);
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
        return 'spieniacz';
