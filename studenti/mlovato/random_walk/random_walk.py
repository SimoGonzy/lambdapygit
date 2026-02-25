from random import choice

class RandomWalk:
    # classe per generare passeggiate aleatorie
    def __init__(self, num_points=5000) -> None:
        # inizializza attributi di una passeggiata
        self.num_points=num_points
        # tutte le passeggiate iniziano a (0,0)
        self.x_value = [0]
        self.y_value = [0]
    
    def fill_walk(self):
        """
        Docstring per fill_walk
        
        calcola tutti i punti della passeggiata
        """
        # continua a girare finchè non raggiungo la lunghezza
        while len(self.x_value)<self.num_points:
            # decide direzione e distanza per x
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            # direzione e distanza per y
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            # scarta i movimenti che non vanno da nessuna parte
            if x_step == 0 and y_step == 0:
                continue
            # calcola la nuova posizione
            # ultima posizione conosciuta + lo step appena calcolato
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step
            # aggiunge alla lista
            self.x_value.append(x)
            self.y_value.append(y)