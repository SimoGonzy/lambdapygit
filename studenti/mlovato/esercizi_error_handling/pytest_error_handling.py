import pytest
from esercizi_error_handling import Studente, NessunVotoError

def test_media_con_voti():
    studente = Studente("Mario Rossi")
    studente.aggiungi_voto(8)
    studente.aggiungi_voto(7)
    studente.aggiungi_voto(6)
    assert studente.media() == 7

def test_media_senza_voti():
    studente = Studente("Luigi Bianchi")
    with pytest.raises(NessunVotoError):
        studente.media()
def test_verfica_promozione_promosso():
    studente = Studente("Anna Neri")
    studente.aggiungi_voto(9)
    assert studente.verifica_promozione() == "Promosso"