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
grafo2.edges(data=True) #[(u,v,{"weight":3,...}




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


