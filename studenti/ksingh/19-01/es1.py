class Tamagotchi:
    def __init__(self, nome: str):
        self.nome = nome
        self.fame = 50
        self.felicita = 50
        self.stanchezza = 50

    def nutri(self):
        self.fame -= 10
        self.stanchezza += 5
        self._limita_valori()

    def gioca(self):
        self.felicita += 10
        self.stanchezza += 10
        self._limita_valori()

    def dormi(self):
        self.stanchezza -= 15
        self.felicita -= 5
        self.fame += 10
        self._limita_valori()

    def stato(self):
        return (
            f"Nome: {self.nome}\n"
            f"Fame: {self.fame}\n"
            f"Felicità: {self.felicita}\n"
            f"Stanchezza: {self.stanchezza}"
        )

    def _limita_valori(self):
        self.fame = max(0, min(100, self.fame))
        self.felicita = max(0, min(100, self.felicita))
        self.stanchezza = max(0, min(100, self.stanchezza))



t = Tamagotchi("Puffi")
