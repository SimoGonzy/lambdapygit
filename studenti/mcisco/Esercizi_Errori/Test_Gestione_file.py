import pytest
from pathlib import Path

from GEstione_File_Scaricati import sposta_file, trova_estensione_file

def test_sposta_file():

    assert True

    lista_file_destinazione : list = [
        Path("/home/matteo/Immagini"),
        Path("/home/matteo/Documenti/Cartella_pdf"),
        Path("/home/matteo/Musica"),
        Path("/home/matteo/Documenti/Roba_Cestino")
    ]

    lista_file_da_spostare : list = []
    file_prova = Path("/home/matteo/Scaricati/Prova.txt")
    with file_prova.open("w", encoding="utf-8") as f:
        f.write("Prova")

    lista_file_da_spostare.append(file_prova)

    sposta_file(lista_file_da_spostare, lista_file_destinazione)

    if Path("/home/matteo/Documenti/Roba_Cestino/Prova.txt").exists():
        assert True
        Path("/home/matteo/Documenti/Roba_Cestino/Prova.txt").unlink()
    else:
        assert False


def test_trova_estensione_file():
    file_prova = Path("/home/matteo/Scaricati/Prova.txt")
    estensione = trova_estensione_file(file_prova)
    assert estensione == ".txt"

