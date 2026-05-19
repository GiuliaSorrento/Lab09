
from database.DB_connect import DBConnect
from model.areoporto import Areoporto


class areoporto_DAO:

    @staticmethod
    def getAllNodes():
            conn = DBConnect.get_connection()
            cursor = conn.cursor(dictionary=True)

            res = []  # lista di oggetti di tipo areoporto
            query = """select *
                    from airports a"""

            cursor.execute(query)
                                              #unpack si può fare quando ti selezioni tutti gli attributi e ti crei l'oggetto intero
            for row in cursor:
                res.append(Areoporto(**row))  # (**row) UNPACK significa:  res.append(ArtObject(object_id=row["object_id], ....)

            cursor.close()
            conn.close()
            return res  #lista di oggetti di tipo areoporto