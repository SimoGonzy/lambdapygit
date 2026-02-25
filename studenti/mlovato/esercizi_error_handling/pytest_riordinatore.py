from riordinatore import dove_mettere_file, quale_cartella, FileNotSupported, PathNotFound
from pathlib import Path
import pytest

home = Path("/Users/matteo/Developer/lambdapygit/studenti/mlovato/esercizi_error_handling")

def test_classificazione_file():
    (home / "prova_pytest.pdf").touch()
    assert dove_mettere_file((home / "prova_pytest.pdf")) == (home / "PDF")
    (home / "prova_pytest.pdf").unlink()

def test_classificazione_file_negativa():
    (home / "prova_pytest.pdf").touch()
    assert dove_mettere_file((home / "prova_pytest.pdf")) != (home / "Video")
    (home / "prova_pytest.pdf").unlink()

def test_spostamento_file():
    (home / "prova_pytest.pdf").touch()
    quale_cartella(home)
    (home / "prova_pytest.pdf").unlink()
    assert (home / "PDF" / "prova_pytest.pdf").exists() == True

def test_file_non_supportato():
    (home / "prova_pytest.shdajk").touch()
    with pytest.raises(FileNotSupported):
        quale_cartella(home)
    (home / "prova_pytest.shdajk").unlink()