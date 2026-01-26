from pathlib import Path

class EstensioneNonSupportata(Exception):
    pass

class NonUnaCartella(Exception):
    pass

def riordina_per_estensione(percorso_file):
    estensioni_cartelle = {
        '.txt': 'C:/Users/gonza/Documents',
        '.jpg': 'C:/Users/gonza/Immagini',
        '.png': 'C:/Users/gonza/Immagini',
        '.pdf': 'C:/Users/gonza/Documents',
        '.mp3': 'C:/Users/gonza/Musica',
        '.mp4': 'C:/Users/gonza/Video',
        '.zip': 'C:/Users/gonza/Documents/Archivi',
    }

    percorso = Path(percorso_file)
    estensione = percorso.suffix.lower()

    if estensione in estensioni_cartelle:
        print(f"\nRETURN: {estensione} / {estensioni_cartelle[estensione]}")
        return percorso / estensioni_cartelle[estensione]
    else:
        raise EstensioneNonSupportata(f"L'estensione '{estensione}' non è supportata.")
    
def organizza_cartella(percorso_cartella):
    percorso = Path(percorso_cartella)

    if not percorso.is_dir():
        raise NonUnaCartella(f"{percorso} non è una cartella valida.")

    for file in percorso.iterdir():
        if file.is_file():
            try:
                print(f"\nPercorso file: {file}")
                destinazione = riordina_per_estensione(file)

                print(f"Sposto {file.name} in {destinazione}")
                sposta_file(file, destinazione)

            except EstensioneNonSupportata:
                print(f"File non supportato: {file.name}, saltando...")


def sposta_file(file, percorso_dest):
    print(f"\nOPERAZIONI SPOSTA FILE\nNome File: {file}")
    print(f"Cartella di destinazione: {percorso_dest}")
    percorso_dest.mkdir(exist_ok=True)
    file.rename(percorso_dest / file.name)

#MAIN

esempio_cartella = Path("C:\\Users\\gonza\\Documents\\cartella")
try:
    organizza_cartella(esempio_cartella)
except NonUnaCartella as e:
    print(e)