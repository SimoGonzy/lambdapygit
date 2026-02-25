from random import randint

class Die:
    """
    Docstring per Die
    Classe che rappresenza un singolo dado
    """

    def __init__(self, num_sides=6) -> None:
        """
        Docstring per __init__
        
        :param num_sides: numero facce del dado, default 6
        """
        self.num_sides = num_sides
    
    def roll(self) -> int:
        """
        Docstring per roll
        
        restituisce un valore tra 1 ed il numero delle facce
        """
        return randint(1,self.num_sides)