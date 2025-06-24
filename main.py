import math
from dataclasses import dataclass

import networkx as nx

@dataclass
class Voto:
    punti: int
    nome:str

    def __hash__(self):
        return hash((self.punti, self.nome))
    def __eq__(self, other):
        return self.nome == other.nome


#ci sono dei grafi notevoli
grafo = nx.Graph() #genera grafo semplice(archi non orientati)
grafo2=nx.DiGraph() #genera grafo diretto

#aggiungere nodi: possono essere di tutto!
grafo.add_node(1)
grafo.add_node("Due")
grafo.add_node(Voto(24,"TdP"))
grafo.add_node(math.cos) #sto aggiungendo una funzione

#aggiungere più nodi insieme
nbunch= [1,2,3,4,5,6,7,8,9]
grafo2.add_nodes_from(nbunch)


#aggiungere archi
grafo.add_edge("Due",1, attributo=1)

#aggiungere più archi insieme
ebunch= [(4,6),(8,1),(2,9)] #attenzione, se aggiungo nodi che non c'erano, questi vengono aggiunti automaticamente!!!
grafo2.add_edges_from(ebunch)


#quali nodi e archi ho nel grafo?
print(grafo2.nodes())
print(grafo2.edges()) #[(u,v),(u2,v2)])...]
list(grafo2.edges(data=True)) #[(u,v,{"weight":3,...}




#ottenere attributi di un arco
print(grafo.get_edge_data("Due",1))

#è come un dizionario che ha come chiavi i nodi
print(grafo["Due"]) #ti trova tutti i nodi connessi con 2, come chiave. e come valori gli attributi dell'arco che li collega in un altro dizionario
print(grafo["Due"][1]) #così prendo solo il dizionario di attributi

#stampa successori e predecessori
print(list(s for s in grafo2.successors(4))) #importantissimo mettere list
print(list(r for r in grafo2.predecessors(6)))

#Il metodo restituisce il grado del nodo, cioè quanti archi sono collegati a quel nodo.
grafo.degree[nodo]

# Modifica del peso di un arco esistente
grafo['A']['B']['weight'] = 10

#archi incidenti al nodo
list(self.grafo.edges(n, data=True)) [[(u,v,{weight:12})]]

#aggiungi metodi guardando ogni tema d'esame

#cammino più breve usando dijkstra
def getPath(self,v0,v1):
    path=nx.dijkstra_path(self._graph,v0,v1, weight=None)
    return path

#numero componenti connesse ad un grafo
def getConnesse(self):
    return len(list(nx.connected_components(self._grafo)))

def getInfoConnessa(self,idInput):
        """
        restituisce la dimensione della componente connessa(a quanti nodi è collegata: cioè a quanti nodi può arrivare(da una fermata, quante fermate della metro posso raggiungere?)
        deepfirst e breath first
        """
        if id not in self.idMapNodes:
            return None
            
        source= self._idMapObjects[idInput]
        #modo 1: conto i successori
        successori= nx.dfs_successors(self._grafo, source).values() #restituisce un dizionario chiave: oggetto, valore: lista di oggetti successori
        res=[]
        for s in successori:
            res.extend(s)
        print("modo 1:", len(res)+1)

        # modo 2: conto i predecessori
        predecessori = nx.dfs_predecessors(self._grafo,source)  # restituisce un dizionario chiave: oggetto, valore: il predecessore
        print("modo 1:", len(predecessori.values())+1)

        #modo3:dfstree, e conto i nodi dell'albero di visita
        dfsTree= nx.dfs_tree(self._grafo, source).values() #e poi faccio len

        #modo 4:medodi connectivity
        conn= nx.node_connected_components(self._graph,source)

        return len(conn)

#visito grafo
def getBFSNodesFromTree(self,source):
   #nodi raggiungibili da source
    tree=nx.bfs_tree(self._grafo,source) #ritorna un albero orientato
    archi=list(tree.edges())
    nodi=list(tree.nodes())
    return nodi[1:] #perchè non ci serve il nodo source
    #man mano mi allontano dal nodo source

def getBFSNodesFromEdges(self,source):
    #trovo i nodi dagli archi
    archi=nx.bfs_edges(self._grafo,source) #lista di tuple(partenza,arrivo)
    res=[]
    for u,v in archi:
        res.append(v) #solo i nodi di arrivo
    return res

def getDFSNodesFromTree(self,source):
    tree=nx.dfs_tree(self._grafo,source)
    archi=list(tree.edges())
    nodi=list(tree.nodes())
    return nodi[1:]
    #ordine diverso da bfs perchè va sempre con l'adiacente

#lista di archi di un grafo
archi= list(self._grafo.edges(data=True))



