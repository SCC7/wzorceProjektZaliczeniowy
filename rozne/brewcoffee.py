from rozne.kubek import Kubek
from urzadzenia.komoraCisnieniowa import komoraCisnieniowa
from urzadzenia.mlynek import Mlynek
from urzadzenia.wyborUrzadzenia import WybierzUrzadzenie
from przepisy.napoj import napoj;
from wybierzPrzymiotnik import wybierzPrzymiotnik;


def tworzNapoj(przepis, rozmiar_napoju):
    ten_napoj = napoj(przepis)
    rozmiar = ten_napoj.podaj_rozmiar(rozmiar_napoju)
    print(f"{wybierzPrzymiotnik(ten_napoj.podaj_rodzaj())} {ten_napoj.podaj_nazwe()} jest przygotowywane");

    # print(ten_napoj.wykonaj_pierwszy_krok(1));
    # print(ten_napoj.wykonaj_drugi_krok(1));
    # print(ten_napoj.wykonaj_trzeci_krok(1));
    # wymagane_urzadzenie = rozkaz('urzadzenie')
    # print('DEBUR rozkaz: ')
    # print(rozkaz);

    # print('TEST MLYNKA');
    # zubar = Mlynek()
    # zubar.wypelnianie('ziarna_kawy', 50)
    # zubar.dzialanie();
    # zmielona_kawa = zubar.oproznianie();
    # # print (zmielona_kawa)
    # print('KONIEC TESTU MLYNKA');
    #
    # print('TEST KOMORY');
    # alemania = komoraCisnieniowa();
    # alemania.wypelnianie('kawa', zmielona_kawa);
    # alemania.dzialanie()
    # zawartosc_kubka = alemania.oproznianie()
    # print('KONIEC TESTU KOMORY')

    dostepne_urzadzenia = dict(mlynek=Mlynek, komora_cisnieniowa=komoraCisnieniowa);
    # print(f'Czy rozmiar_napoju to int? {isinstance(rozmiar_napoju, int)}')
    # print(f'Czy rozmiar_napoju to float? {isinstance(rozmiar_napoju, float)}')
    kubek = Kubek(rozmiar);

    # wymagane_urzadzenia = ten_napoj.zdefiniuj_wymagania().split();
    # print(wymagane_urzadzenia)
    # wymagane_urzadzenia = mlynek.Mlynek;

    # ekspres = Ekspres();
    # urzadzenie = WybierzUrzadzenie(wymagane_urzadzenia[0]);

    # print(urzadzenie)
    # print(dostepne_urzadzenia[wymagane_urzadzenia[1]])
    # ekspres.builder = urzadzenie;

    rozkaz = ten_napoj.wykonaj_pierwszy_krok(rozmiar)
    urzadzenie = WybierzUrzadzenie(dostepne_urzadzenia[rozkaz['urzadzenie']]);
    # temp = urzadzenie.build('ziarna_kawy', rozmiar_napoju);
    urzadzenie.build('ziarna_kawy', rozmiar);
    # kubek.dodaj_zawartosc(temp['substancja'], temp['ilosc']);
    # print(kubek.rozmiar);
    # print(kubek.zawartosc);
    if ten_napoj.wykonaj_drugi_krok(1) is not None:
        rozkaz = ten_napoj.wykonaj_drugi_krok(rozmiar)
        urzadzenie = WybierzUrzadzenie(dostepne_urzadzenia[rozkaz['urzadzenie']]);
        temp = urzadzenie.build('kawa', rozmiar);
        print(f'DEBUG temp["ilosc"] = {temp["ilosc"]}');
        kubek.dodaj_zawartosc(temp['substancja'], temp['ilosc']);
        if ten_napoj.wykonaj_trzeci_krok(1) is not None:
            rozkaz = ten_napoj.wykonaj_trzeci_krok(rozmiar);
            urzadzenie = WybierzUrzadzenie(dostepne_urzadzenia[rozkaz['urzadzenie']]);
            temp = urzadzenie.build('woda', rozmiar);
            kubek.dodaj_zawartosc(temp['substancja'], temp['ilosc']);

    print(f'{wybierzPrzymiotnik(ten_napoj.podaj_rodzaj())} {ten_napoj.podaj_nazwe()} jest gotowe! Smacznego!');
