from pathlib import Path
import time

class Tamagotchi:
    def __init__(self, nome: str, fame: int = 50, felicta: int = 50, stanchezza: int = 50, vivo: bool = True):
        self.nome = nome
        self.fame = fame
        self.felicita = felicta
        self.stanchezza = stanchezza
        self.vivo = vivo

    def nutri(self):
        #diminuisce fame, aumenta stanchezza
        self.fame = self.fame - 10
        self.stanchezza = self.stanchezza + 5

    def gioca(self):
        #aumenta stanchezza, aumenta felicita
        self.stanchezza = self.stanchezza + 10
        self.felicita = self.felicita + 15

    def dormi(self):
        #diminuisce stanchezza, aumenta fame
        self.stanchezza = self.stanchezza - 30
        self.fame = self.fame + 20
    
    def morte(self):
        self.vivo = False
    
    def is_alive(self):
        return all(0 < v <= 100 for v in [self.stanchezza, self.felicita, self.fame])

    def __eq__(self, nuovo):
        return self.nome == nuovo.nome
    
    def __str__(self) -> str:
        #scriviamo in stringa lo stato del mostro
        return f"STANCHEZZA: {self.stanchezza} FELICITA: {self.felicita} FAME: {self.fame}"
    
    def __repr__(self):
        return self.nome
    
    def to_csv(self):
        return f"{self.nome},{self.fame},{self.felicita},{self.stanchezza},{self.vivo}"
    
    @classmethod
    def load_from_csv(cls, csv_string):
        campi = csv_string.strip().split(",")
        nome = str(campi[0])
        fame = int(campi[1])
        felicita = int(campi[2])
        stanchezza = int(campi[3])
        vivo = campi[4]
        return (nome, fame, felicita, stanchezza, vivo)
    

lista_tamagotchi = []

#carica da file
file = Path(__file__).with_name("Tamagotchi.csv")

with file.open("r", encoding="utf-8") as leggo:
    righe = leggo.read().strip().split("\n")

    for riga in righe[1:]:
        nome, fame, felicita, stanchezza, vivo = riga.split(",")

        t = Tamagotchi(nome, int(fame), int(felicita), int(stanchezza), vivo = vivo == "True")

        lista_tamagotchi.append(t)



#menu
while True:
    print("Ciao, scegli il tuo Tamagotchi!")
    print("Scrivi 5 per uscire")
    print("Scrivi 7 per cancellare un Tamagotchi")
    print(lista_tamagotchi)
    scelta_mostro = input ("Scrivi il nome del Tamagotchi con cui vuoi giocare o che vuoi aggiungere \n")
    if scelta_mostro == "5":
        with file.open("w", encoding = "utf-8") as t:
            righe = ["nome,fame,felicita,stanchezza,vivo\n"]
            for tamagotchi in lista_tamagotchi:
                righe.append(tamagotchi.to_csv())
                righe += "\n"
            stampa_su_file = "".join(righe)
            t.write(stampa_su_file)
        break
    if scelta_mostro == "7":
        elimina_tamagotchi = input("Scrivi il nome del Tamagotchi che vuoi eliminare \n")
        for tamagotchi in lista_tamagotchi:
            if elimina_tamagotchi == tamagotchi.nome:
                lista_tamagotchi.remove(tamagotchi)
        continue
    tamagotchi_trovato = False
    for tamagotchi in lista_tamagotchi:
        if scelta_mostro == tamagotchi.nome:
            scelta_mostro = tamagotchi
            if scelta_mostro.vivo:
                tamagotchi_trovato = True
                break
            else:
                tamagotchi_trovato = True
                break
    if not tamagotchi_trovato:
        nome_mostro = "" + str(scelta_mostro)
        scelta_mostro = Tamagotchi(nome_mostro)
        lista_tamagotchi.append(scelta_mostro)

    print("Seleziona l'azione premendo il tasto corrispondente:")
    print("1 per vedere lo stato del Tamagotchi")
    print("2 per nutrirlo")
    print("3 per farlo giocare")
    print("4 per farlo dormire")
    print("5 per uscire dal gioco \n")

    if not scelta_mostro.vivo:
        print(f"Non puoi interagire con {tamagotchi.nome}, lo hai fatto morire...")

    time.sleep(2)

    while scelta_mostro.vivo:
        scelta = input("")
        match scelta:
            case "1":
                print(scelta_mostro)
            case "2":
                scelta_mostro.nutri()
                print(scelta_mostro)
                if not scelta_mostro.is_alive():
                    print(f"{scelta_mostro.nome} è morto!")
                    scelta_mostro.morte()
                    break
            case "3":
                scelta_mostro.gioca()
                print(scelta_mostro)
                if not scelta_mostro.is_alive():
                    print(f"{scelta_mostro.nome} è morto!")
                    scelta_mostro.morte()
                    break
            case "4":
                scelta_mostro.dormi()
                print(scelta_mostro)
                if not scelta_mostro.is_alive():
                    print(f"{scelta_mostro.nome} è morto!")
                    scelta_mostro.morte()
                    break
            case "5":
                print(scelta_mostro)
                break