from pathlib import Path

# Eccezioni personalizzate
class UnsupportedExtensionError(Exception):
    """Filetype non supportato."""
    pass

# Livello 1

class FileClassifier:
    """
    Livello 1: Il classificatore
    """
    def __init__(self):
        self.mapping = {
            'Immagini': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff'],
            'Documenti': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.csv', '.md'],
            'Video': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
            'Musica': ['.mp3', '.wav', '.flac', '.aac', '.m4a'],
            'Archivi': ['.zip', '.rar', '.tar', '.gz', '.7z', '.iso', '.dmg', '.exe']
        }
        self.ext_map = {}
        for folder, exts in self.mapping.items():
            for ext in exts:
                self.ext_map[ext.lower()] = folder

    def classify(self, file_path: Path) -> Path:
        """
        Scelta cartella in base alla estensione.
        
        Args:
            file_path (Path): indirizzo del file.
            
        Returns:
            Path: indirizzo della cartella di destinazione.
            
        Raises:
            UnsupportedExtensionError: Se l'estensione non è supportata.
        """
        if not isinstance(file_path, Path):
            file_path = Path(file_path)

        ext = file_path.suffix.lower()
        if not ext:
             # Per ora, trattiamo come non supportato come da requisiti per gestire "formato non supportato"
             raise UnsupportedExtensionError(f"File '{file_path.name}' ha un'estensione non valida")
        
        folder_name = self.ext_map.get(ext)
        if not folder_name:
            raise UnsupportedExtensionError(f"Estensione '{ext}' non supportata")
        
        # Restituisce l'indirizzo della cartella di destinazione.
        return file_path.parent / folder_name

# Livello 2

class SmartOrganizer:
    """
    Livello 2: Il motore di smistamento
    """
    def __init__(self):
        self.classifier = FileClassifier()

    def organize(self, target_folder: Path):
        """
        Organizza i file nella cartella di destinazione in sottocartelle.
        """
        target_folder = Path(target_folder)
        if not target_folder.exists() or not target_folder.is_dir():
            raise FileNotFoundError(f"La cartella '{target_folder}' non esiste o non è una directory")

        # Controlla tutti i file nella cartella
        for item in target_folder.iterdir():
            # Salta directory e file nascosti/log
            if item.is_file() and not item.name.startswith('.'):
                self._process_file(item)

    def _process_file(self, file_path: Path):
        try:
            # Livello 1: Classifica
            dest_folder = self.classifier.classify(file_path)
            
            # Crea destinazione se necessario
            dest_folder.mkdir(exist_ok=True)
            
            dest_file_path = dest_folder / file_path.name
            
            # Livello 2: Sposta file
            file_path.rename(dest_file_path)
            
        except UnsupportedExtensionError:
            # Salta file non supportati
            pass
        except (PermissionError, OSError):
            # Salta in caso di errori di sistema
            pass
        except Exception:
            # Salta in caso di errori imprevisti
            pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print(f"Organizzando {path}...")
        organizer = SmartOrganizer()
        organizer.organize(path)
        print("Finito.")
    else:
        print("Scrivi: python smart_organizer.py <cartella_da_organizzare>")
