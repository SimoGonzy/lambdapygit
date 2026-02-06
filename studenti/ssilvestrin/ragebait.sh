#!/bin/bash

# OPERAZIONI SUI FILE E SULLE CARTELLE
crea_cartella() {
    # "Crea una cartella al percorso specificato se non esiste già"
    mkdir -p "$1"
}

sposta_file() {
    # "Sposta il file da file_path a destinazione_path"
    mv "$1" "$2"
}

cartella="/home/samuel/Downloads"

for f in "$cartella"/*; do
    suffix="${f##*.}"
    name=$(basename "$f")
    
    if [[ "$suffix" == "mp4" ]] || [[ "$suffix" == "mp3" ]]; then
        crea_cartella "/home/samuel/Downloads/media" 2>/dev/null || echo "Impossibile creare la cartella"
        echo "$(date) Creata cartella media"
        sposta_file "$f" "/home/samuel/Downloads/media/$name" 2>/dev/null || echo "Impossibile spostare il file"
        echo "$(date) Spostato il file $name"
    fi
    
    if [[ "$suffix" == "pdf" ]] || [[ "$suffix" == "docx" ]]; then
        crea_cartella "/home/samuel/Downloads/documents" 2>/dev/null || echo "Impossibile creare la cartella"
        echo "$(date) Creata cartella documents"
        sposta_file "$f" "/home/samuel/Downloads/documents/$name" 2>/dev/null || echo "Impossibile spostare il file"
        echo "$(date) Spostato il file $name"
    fi
    
    if [[ "$suffix" == "png" ]] || [[ "$suffix" == "jpg" ]] || [[ "$suffix" == "jpeg" ]] || [[ "$suffix" == "raw" ]] || [[ "$suffix" == "arw" ]]; then
        crea_cartella "/home/samuel/Downloads/photo" 2>/dev/null || echo "Impossibile creare la cartella"
        echo "$(date) Creata cartella photo"
        sposta_file "$f" "/home/samuel/Downloads/photo/$name" 2>/dev/null || echo "Impossibile spostare il file"
        echo "$(date) Spostato il file $name"
    fi
    
    if [[ -f "$f" ]]; then
        crea_cartella "/home/samuel/Downloads/dumpster" 2>/dev/null || echo "Impossibile creare la cartella"
        echo "$(date) Creata cartella dumpster"
        sposta_file "$f" "/home/samuel/Downloads/dumpster/$name" 2>/dev/null || echo "Impossibile spostare il file"
        echo "$(date) Spostato il file $name"
    fi
    
done 2>/dev/null || echo "Couldn't resolve path or suffix"

echo "Ragebait completed"