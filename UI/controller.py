import flet as ft


class Controller:
    def __init__(self, view, model):

        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza_areoporti(self, e):
        #ricavo il valore dell'inserimento dell'utente
        xmedio = self._view._txtInDistMin.value #mi restituisce una stringa
        #NB QUANDO PROVI A TRASFORMARE IN INTERO UN INPUT UTENTE FAI TRY EXCEPT
        try:
            x=int(xmedio)
        except:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, devi inserire un numero intero positivo per le miglia"))
            self._view.update_page()
        #chiamare la costruzione del grafo
        self._model.buildGraph(x)
        #chiamare i due metodi per ottenere i numeri di nodi e di archi
        n=self._model.getNumNodes()
        a=self._model.getNumEdges()
        #restituire elenco di tutti gli archi con la relativa distanza
        alledges = self._model.getAllEdges(x)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttanente!"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {n} nodi e {a} archi"))
        self._view.update_page()
        for t in alledges:
            self._view.txt_result.controls.append(ft.Text(t))
            self._view.update_page()