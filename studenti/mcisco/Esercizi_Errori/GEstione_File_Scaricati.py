#Riordinamento file scaricati

import os
from pathlib import Path
class Loging:
    def __init__(self, file_name: str, cartella_destinazione: Path, esito: bool):
        self.nome = file_name
        self.cartella_destinazione = cartella_destinazione
        self.esito = esito


    def logga(self):
        file_log = Path(f"/home/matteo/Documenti/Cartella_log/{self.nome}.txt")
        with file_log.open("w", encoding="utf-8") as f:
            f.write(f"{self.nome};{self.cartella_destinazione};{self.esito}")





def trova_estensione_file(f_p: Path):
    return f_p.suffix

"""
organizzazione file 
.png -> Immagini
.pdf -> Documenti/Cartella_pdf
.mp3 -> Musica

il resto -> Documenti/Roba_Cestino
"""
def sposta_file(file_da_spostare: list[Path], destinazione: list[Path]):
    try:
        for file in file_da_spostare:
            estensione = trova_estensione_file(file)
            try:
                if(estensione == ".png"):
                    file.rename(destinazione[0].joinpath(file.name))
                    l = Loging(file.name, destinazione[0], True)
                    l.logga()
                elif(estensione == ".pdf"):
                    file.rename(destinazione[1].joinpath(file.name))
                    l = Loging(file.name, destinazione[1], True)
                    l.logga()
                elif(estensione == ".mp3"):
                    file.rename(destinazione[2].joinpath(file.name))
                    l = Loging(file.name, destinazione[2], True)
                    l.logga()
                else:
                    file.rename(destinazione[3].joinpath(file.name))
                    l = Loging(file.name, destinazione[3], True)
                    l.logga()
            except:
                print(f"Impossibile spostare il file {file}")
                l = Loging(file.name, Path("/home/matteo/Documenti/Cartella_log"), False)
                l.logga()
    except:
        print("Impossibile spostare i file")



lista_file_destinazione : list = [
    Path("/home/matteo/Immagini"),
    Path("/home/matteo/Documenti/Cartella_pdf"),
    Path("/home/matteo/Musica"),
    Path("/home/matteo/Documenti/Roba_Cestino")
]

lista_file_da_spostare : list = []

Cartella_file = Path("/home/matteo/Scaricati")
for file in Cartella_file.iterdir():
    if file.is_file():
        lista_file_da_spostare.append(file)

#print(lista_file_da_spostare)

sposta_file(lista_file_da_spostare, lista_file_destinazione)
