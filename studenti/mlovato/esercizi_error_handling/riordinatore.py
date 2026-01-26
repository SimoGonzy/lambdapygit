from pathlib import Path

class FileNotSupported(Exception):
    pass
class PathNotFound(Exception):
    pass

def dove_mettere_file(path):
    home_path = path.parent
    match path.suffix.lower():
        case ".doc" | ".docx":
            return home_path / "Docs"
        case ".mp4":
            return home_path / "Video"
        case ".pdf":
            return home_path / "PDF"
        case ".png" | ".jpg":
            return home_path / "Immagini"
    raise FileNotSupported(f"File non supportato {path.suffix}")

def ordina_cartella(path: Path):
    for file in path.iterdir():
        if file.is_file() and file.suffix != ".py":
            try:
                path_destinazione = dove_mettere_file(file)
                if path_destinazione:
                    path_destinazione.mkdir(exist_ok=True)
                    file.copy(path_destinazione / file.name)
            except FileNotSupported as e:
                print(e)

def quale_cartella (path: Path):
    if path.exists():
        ordina_cartella(path)
    else:
        raise PathNotFound(f"Questa cartella non esiste {path.name}")

dir = input("Che cartella devo riordinare?")
path_da_ordinare = Path(__file__).parent
if dir != "this":
    path_da_ordinare = Path(dir)
try:
    quale_cartella(path_da_ordinare)
except PathNotFound as e:
    print(e)
