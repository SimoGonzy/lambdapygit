import os
from datetime import datetime
from pathlib import Path

#OPERAZIONI SUI FILE E SULLE CARTELLE

def crea_cartella(cartella_path):
    #"Crea una cartella al percorso specificato se non esiste già"
    Path(cartella_path).mkdir(parents=True, exist_ok=True)

def sposta_file(file_path, destinazione_path):
    #"Sposta il file da file_path a destinazione_path"
    os.rename(file_path, destinazione_path)

cartella: Path = Path("/home/samuel/Downloads")

try:

    for f in cartella.iterdir():
        suffix = f.suffix
        name = f.name
        try:
            if suffix == ".mp4" or suffix == ".mp3":
                crea_cartella("/home/samuel/Downloads/media")
                print(datetime.now(),"Creata cartella media")
                try:
                    sposta_file(f,f"/home/samuel/Downloads/media/{name}")
                    print(datetime.now(), f"Spostato il file  {name}")
                except:
                    print("Impossibile spostare il file")
        except Exception as e:
            print("Impossibile creare la cartella", e)
        
        try:
            if suffix == ".pdf" or suffix == ".docx":
                crea_cartella("/home/samuel/Downloads/documents")
                print(datetime.now(),"Creata cartella documents")
                try:
                    sposta_file(f,f"/home/samuel/Downloads/documents/{name}")
                    print(datetime.now(), f"Spostato il file  {name}")
                except Exception as e:
                    print("Impossibile spostare il file", e)
        except Exception as e:
            print("Impossibile creare la cartella", e)

        try:
            if suffix == ".png" or suffix == ".jpg" or suffix == ".jpeg" or suffix == ".raw" or suffix == ".arw":
                crea_cartella("/home/samuel/Downloads/photo")
                print(datetime.now(),"Creata cartella photo")
                try:
                    sposta_file(f,f"/home/samuel/Downloads/photo/{name}")
                    print(datetime.now(), f"Spostato il file  {name}")
                except Exception as e:
                    print("Impossibile spostare il file", e)
        except Exception as e:
            print("Impossibile creare la cartella", e)

        try:
            if os.path.isfile(f):
                crea_cartella("/home/samuel/Downloads/dumpster")
                print(datetime.now(),"Creata cartella dumpster")
                try:
                    sposta_file(f,f"/home/samuel/Downloads/dumpster/{name}")
                    print(datetime.now(), f"Spostato il file  {name}")
                except:
                    print("Impossibile spostare il file")
        except Exception as e:
            print("Impossibile creare la cartella", e)

except:
    print("Couldn't resolve path or suffix")

