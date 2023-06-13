from _pytest.python_api import raises

from rozne.kubek import Kubek


def testuj_za_duzy_kubek():
    with raises(ValueError):
        Kubek(400);
    with raises(ValueError):
        Kubek(500);
    with raises(ValueError):
        Kubek(401);
    with raises(ValueError):
        Kubek(400.2);


def testuj_za_maly_kubek():
    with raises(ValueError):
        Kubek(0);
    with raises(ValueError):
        Kubek(-1);
    with raises(ValueError):
        Kubek(-300)

def testuj_rozmiar_kubka_w_przedziale():
    assert 0 < Kubek.rozmiar < 400;
    assert 0 < Kubek(10).rozmiar < 400;
    assert 0 < Kubek(399).rozmiar < 400;
    assert 0 < Kubek(1).rozmiar < 400;
    assert 0 < Kubek(123.456).rozmiar < 400;
    assert 0 < Kubek(200.1111111111111111111111111).rozmiar < 400;


def testuj_zly_typ_rozmiaru_kubka():
    with raises(TypeError):
        Kubek('lol');
    with raises(TypeError):
        Kubek('MIROWNOGURIN0iojn190847523h957')
    with raises(TypeError):
        Kubek(dict(value=1,this='that'))

def przelej_kubek():
    with raises(ValueError):
        Kubek(100).dodaj_zawartosc('cokolwiek', 200)
    with raises(ValueError):
        Kubek(100).dodaj_zawartosc('cokolwiek', 100.1)

def wprowadz_niestring_jako_rodzaj_skladnika():
    with raises(TypeError):
        Kubek().dodaj_zawartosc(1,1);
    with raises(TypeError):
        Kubek().dodaj_zawartosc(None,1);