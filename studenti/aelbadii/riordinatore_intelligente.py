from pathlib import Path



def organizza_file(percorso_file):
    file = Path(percorso_file)
    
    destinazioni = {
        '.jpg': 'Mie_Immagini',
        '.png': 'Mie_Immagini',
        '.pdf': 'Miei_Documenti',
        '.zip': 'Miei_Archivi'
    }

    

    estensione = file.suffix.lower()

    if estensione in destinazioni:
        cartella_dest = Path(destinazioni[estensione])
        cartella_dest.mkdir(exist_ok=True)
        return cartella_dest
    else:
        return(f"Estensione {estensione} non gestita")




dest = organizza_file("test.zip")
print(f"Cartella pronta: {dest}")

