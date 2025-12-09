from random import choice

class RandomWalk:
    def __init__(self, num_passi=5000) -> None:
        self.x_values = [0]
        self.y_values = [0]
        self.num_passi = num_passi
        self.fill_walk()
    
    def fill_walk(self):
        while len(self.x_values) < self.num_passi:
            distanza = [0,1,2,3,4]
            x_passi = choice([1,-1]) * choice(distanza)
            y_passi = choice([1,-1]) * choice(distanza)
            if x_passi == 0 and y_passi == 0:
                continue
            # calcolo la nuova posizione da inserire
            new_x = self.x_values[-1] + x_passi
            new_y = self.y_values[-1] + y_passi
            self.x_values.append(new_x)
            self.y_values.append(new_y)