from src.List5.independent_set_alg import Node


def graph_reader(file_name, n):
    file = open(file_name, "r")

    nodes_num = int(file.readline())

    nodes = []
    for line in file:
        vertex_config = line.split(' ')
        node = Node(int(vertex_config[0]))
        nodes.append(node)

    file = open(file_name, "r")
    file.readline()

    for line in file:
        vertex_config = line.split(' ')
        node = nodes[int(vertex_config[0])]
        neighbours = []
        for n in range(1, len(vertex_config)):
            neighbours.append(nodes[int(vertex_config[n])])
        node.set_neighs(neighbours)
        # nodes_with_neighs.append(node)

    return nodes


def graph_to_str(graph):
    ind_to_str = "["
    for v in graph:
        ind_to_str += str(v.i)
        ind_to_str += ", "
    ind_to_str += "]"
    return ind_to_str

