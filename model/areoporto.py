from dataclasses import dataclass


@dataclass
class Areoporto:  #ANCHE SE SONO MAIUSCOLI I NOMI DELLE PROPRIETà DEVONO ESSERE IDENTICI A QUELLI IN DBEAVER SENNO NON FUNZIONA L'UNPACH **ROW
    ID: int
    IATA_CODE: str
    AIRPORT:str
    CITY:str
    STATE:str
    COUNTRY:str
    LATITUDE:float
    LONGITUDE:float
    TIMEZONE_OFFSET:float

    def __hash__(self):
        return hash(self.ID)
    def __eq__(self, other):
        return self.ID == other.ID
    def __str__(self):
        return f"areoporto {self.AIRPORT} ({self.ID})"