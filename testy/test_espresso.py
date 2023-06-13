from _pytest.python_api import raises

from przepisy.espresso import Espresso


def test_czy_typ_rozmiaru_espresso_jest_poprawny():
    with raises(TypeError):
        Espresso(1)
    with raises(TypeError):
        Espresso(None)
    with raises(TypeError):
        Espresso(dict(m='m', l='l'));

def test_czy_wartosc_rozmiaru_espresso_jest_poprawna():
    with raises(ValueError):
        Espresso('małe');
    with raises(ValueError):
        Espresso('d');
    with raises(ValueError):
        Espresso('');

def test_czy_espresso_definiuje_wymagania_jako_string():
    assert isinstance(Espresso('m').zdefiniuj_wymagania(), str);
def test_czy_espresso_definiuje_wymagania():
    assert Espresso('m').zdefiniuj_wymagania() == 'mlynek komora_cisnieniowa';

def test_czy_krok_pierwszy_espresso_to_dict():
    assert isinstance(Espresso('m').wykonaj_pierwszy_krok(1), dict)
def test_czy_krok_drugi_espresso_to_dict():
    assert isinstance(Espresso('m').wykonaj_drugi_krok(1), dict)

def test_czy_krok_trzeci_espresso_to_None():
    assert Espresso('m').wykonaj_trzeci_krok(1) is None

def test_czy_nazwa_to_string():
    assert isinstance(Espresso('m').nazwa(), str)

def test_czy_rodzaj_to_string():
    assert isinstance(Espresso('m').rodzaj(), str);

def test_czy_podaj_rozmiar_to_int():
    assert isinstance(Espresso('m').podaj_rozmiar(), int);