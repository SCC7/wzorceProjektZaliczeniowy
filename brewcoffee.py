import time

import mlynek
from wyborUrzadzenia import wybierz_urzadzenie
from ekspres import Ekspres
from napoj import napoj;
from progressbar import printProgressBar
from wybierzPrzymiotnik import wybierzPrzymiotnik;


def tworzNapoj(coffee):
    ten_napoj = napoj(coffee)
    print(f"{wybierzPrzymiotnik(ten_napoj.podaj_rodzaj())} {ten_napoj.podaj_nazwe()} jest przygotowywane");

    wymagane_urzadzenia = list(ten_napoj.zdefiniuj_wymagania());

    ekspres = Ekspres();
    urzadzenie = wybierz_urzadzenie(wymagane_urzadzenia[0]);
    ekspres.builder = urzadzenie;


    print(f'{wybierzPrzymiotnik(ten_napoj.podaj_rodzaj())} {coffee} jest gotowe! Smacznego!');
