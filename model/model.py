import networkx as nx

from database.areoporto_DAO import areoporto_DAO
from database.tratta_DAO import tratta_DAO

class Model:
    def __init__(self):
        self._graph=nx.Graph()   #grafo non orientato e pesato
        self._idMapAreoporti = {}  #creo id map per gli areoporti


    def buildGraph(self, xmedio):
        #popolare con i nodi che mi prendo dal DAO degli areoporti
        #chiamare un metodo che mi popola di archi pesati, che a sua volta chiama un metodo del DAO
        self._graph.clear() #RICORDATI DI PULIRE IL GRAFO SEMPRE ALL'INIZIO DI BUILDGRAPH
        nodes = areoporto_DAO.getAllNodes()
        self._graph.add_nodes_from(nodes)  #popolo il grafo con i nodi
        self._idMapAreoporti = {aeroporto.ID: aeroporto for aeroporto in nodes}  #riempo idmap areoporti
        self.addEdgePesati(xmedio)  #popolo il grafo con i nodi

    def addEdgePesati(self,xmedio):
        #chiama metodo del DAO che restituisce tutti gli archi e popola il grafo
        allEdgesPesati = tratta_DAO.getAllEdgesPesati(xmedio)
        for tratta in allEdgesPesati:
           areoportoA = self._idMapAreoporti.get(tratta.areoportoA_ID)
           areoportoP = self._idMapAreoporti.get(tratta.areoportoP_ID)
           # Controllo di sicurezza: verifichiamo che entrambi gli aeroporti esistano nella mappa
           if areoportoA and areoportoP:
               # NetworkX gestisce da solo la creazione e l'eventuale sovrascrittura.
               # Usiamo i nomi corretti: .add_edge() e l'attributo tratta.peso_medio
               self._graph.add_edge(areoportoA, areoportoP, weight=tratta.peso)

    def getNumNodes(self):
        return self._graph.number_of_nodes() #ti ritorna il numero di nodi nel grafo
    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getAllEdges(self,xmedio):
        #restituire elenco di tutti gli archi con relativa distanza
        return tratta_DAO.getAllEdgesPesati(xmedio)
