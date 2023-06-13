import pytest

from urzadzenia.mlynek import Mlynek


def test_czy_mlynek_jest_pusty_przed_uzyciem():
    assert Mlynek().ziarna_kawy == 0;
    assert Mlynek().zmielona_kawa == 0;


def test_napelnianie_mlynka_typ():
    with pytest.raises(TypeError):
        Mlynek().wypelnianie(None, 1);
    with pytest.raises(TypeError):
        Mlynek().wypelnianie('zmielona_kawa', 1);
    with pytest.raises(TypeError):
        Mlynek().wypelnianie(1, 1);


def test_napelnianie_mlynka_wartosc():
    with pytest.raises(ValueError):
        Mlynek().wypelnianie('ziarna_kawy', 0)
    with pytest.raises(ValueError):
        Mlynek().wypelnianie('ziarna_kawy', -0.1)
    with pytest.raises(ValueError):
        Mlynek().wypelnianie('ziarna_kawy', -10)


def test_czy_pusty_mlynek_dziala():
    with pytest.raises(ValueError):
        Mlynek().dzialanie();


def test_czy_pusty_mlynek_zwraca_none():
    assert Mlynek().oproznianie() is None;
