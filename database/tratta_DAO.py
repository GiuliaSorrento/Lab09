from database.DB_connect import DBConnect
from model.tratta import Tratta


class tratta_DAO:

    @staticmethod
    def getAllEdgesPesati(xmedio):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []  # lista di oggetti di tipo areoporto
        #uso least e greatest perchè ci sono voli avanti e indietro, lo usi per raggruppare entrambi nella stessa rotta nei grafi non orientati
        # Rinominiamo gli alias (AS) usando EXACTMENTE i nomi della tua dataclass
        query = """SELECT 
                    LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) AS areoportoP_ID,   
                    GREATEST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) AS areoportoA_ID,
                    AVG(f.DISTANCE) AS peso
                    FROM flights f
                    GROUP BY areoportoP_ID, areoportoA_ID
                    HAVING peso >= %s"""

        cursor.execute(query, (xmedio,))
        # unpack si può fare quando ti selezioni tutti gli attributi e ti crei l'oggetto intero
        for row in cursor:
            res.append(
                Tratta(**row))  # (**row) UNPACK significa:  res.append(ArtObject(object_id=row["object_id], ....)

        cursor.close()
        conn.close()
        return res  # lista di oggetti di tipo areoporto, NB PERO DEVI FARE L'ID MAP NEL MODEL