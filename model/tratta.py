from dataclasses import dataclass



from model.areoporto import Areoporto


@dataclass
class Tratta:
    areoportoP_ID: int
    areoportoA_ID: int
    peso: int

    def __str__(self):
        return f"arco: {self.areoportoP_ID}-{self.areoportoA_ID}, distanza: {self.peso}"