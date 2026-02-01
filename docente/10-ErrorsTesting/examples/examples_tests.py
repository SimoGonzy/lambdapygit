# 10 - Gestione degli Errori e Testing
# Esempi tratti dalla dispensa

# Esempio 5: Scrittura di Unit Test
# In questo esempio, scriviamo unit test per verificare il corretto funzionamento
# della classe Studente e della gestione della Custom Exception NessunVotoError.


import pytest
from examples04 import Studente, NessunVotoError


def test_media_con_voti():
    studente = Studente("Mario Rossi")
    studente.aggiungi_voto(8)
    studente.aggiungi_voto(6)
    studente.aggiungi_voto(7)
    assert studente.media() == 7

def test_media_senza_voti():
    studente = Studente("Luigi Bianchi")
    with pytest.raises(NessunVotoError):
        studente.media()

def test_verifica_promozione_promosso():
    studente = Studente("Anna Verdi")
    studente.aggiungi_voto(7)
    studente.aggiungi_voto(8)
    assert studente.verifica_promozione() == "Promosso"

def test_verifica_promozione_bocciato():
    studente = Studente("Carlo Neri")
    studente.aggiungi_voto(4)
    studente.aggiungi_voto(5)
    assert studente.verifica_promozione() == "Bocciato"

def test_verifica_promozione_senza_voti():
    studente = Studente("Elena Gialli")
    assert studente.verifica_promozione() == "Impossibile verificare la promozione: Elena Gialli non ha voti registrati."
