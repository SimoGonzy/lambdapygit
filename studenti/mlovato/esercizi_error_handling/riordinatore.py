from datetime import datetime
from pathlib import Path

class FileNotSupported(Exception):
    pass
class PathNotFound(Exception):
    pass

def dove_mettere_file(path):
    home_path = path.parent
    suffix = path.suffix.lower()
    if suffix == ".doc" or suffix ==".docx":
        return home_path / "Docs"
    elif suffix == ".mp4":
        return home_path / "Video"
    elif suffix == ".pdf":
        return home_path / "PDF"
    elif suffix == ".png" or suffix == ".jpg":
        return home_path / "Immagini"
    else:
        raise FileNotSupported(f"File non supportato {path.name}")

def ordina_cartella(path: Path):
    for file in path.iterdir():
        if file.is_file() and file.suffix != ".py" and file.name != ".gitignore" and file.suffix != ".log":
            path_destinazione = dove_mettere_file(file)
            if path_destinazione:
                path_destinazione.mkdir(exist_ok=True)
                file.copy(path_destinazione / file.name)
                with (path / "movimenti_file.log").open("a", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} - {file.name} è stato spostato in {path_destinazione}\n")


def quale_cartella (path: Path):
    if path.exists():
        ordina_cartella(path)
    else:
        raise PathNotFound(f"Questa cartella non esiste {path.name}")
if __name__ == "__main__":
    dir = input("Che cartella devo riordinare?")
    path_da_ordinare = Path(__file__).parent
    if dir != "this":
        path_da_ordinare = Path(dir)
    try:
        quale_cartella(path_da_ordinare)
    except (PathNotFound, FileNotSupported) as e:
        print(e)
    
