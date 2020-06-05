import time
from src.List5.mutual_exclusion_alg import *
from src.List5.independent_set_alg import *
from src.List5.graph_reader import *


def ex12(n):
    dijkstra_mutual_exclusion(n, None)


def ex13(file_name, n):
    graph = graph_reader(file_name, n)
    independent_set = find_maximal_independent(graph)
    ind_to_str = graph_to_str(independent_set)
    return ind_to_str


if __name__ == '__main__':
    file_graph = "data/graph.txt"

    print("Uruchomienie rozwiązania zajac nawet kilkanascie minut.")

    print("Zad 12. Ponizej zostana wywolane wyniki stanow procesorow po wykonaniu 5000 iteracji algorytmu Dijkstry. \
        \nTrwa praca...")
    ex12(500)

    print("Zad 13. Trwa praca...")
    independent = ex13(file_graph, 0)
    print("Dla grafu opisanego w pliku \"" + str(file_graph) + "\" otrzymano niezalezny zbior wierzcholkow:\
        \n" + independent + "\
        \nFormat zapisu reprezentacji grafu: 1 linia: n - ilosc wierzcholkow,\
        \nkolejne n linii: numer wierzcholka z wymienionymi numerami wierzcholkow sasiadujacych.\
        \nLacznie n+1 linii.\
        \nUwaga! Kolejne wierzcholki grafu nalezy etykietowac kolejnymi liczbami naturalnymi: 0, 1, 2, 3, ...")
