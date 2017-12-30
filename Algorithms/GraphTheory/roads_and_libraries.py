import sys


def DFS(graph, start):
    S = set([])
    Q = []
    Q.append(start)
    while Q:
        current = Q.pop(0)
        if current not in S:
            S.add(current)
            if len(graph[current]) != 0:
                for n in graph[current]:
                    Q.insert(0, n)
    return list(S)

#import of the data
#Loop over each graph
q = int(input().strip())
for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]
    graph_list = {}
    #Loop over the edges of each graph
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1) - 1, int(city_2) - 1]
        #creating a dict of connected nodes for each key node
        if city_1 in graph_list:
            graph_list[city_1] += [city_2]
        else:
            graph_list[city_1] = [city_2]
        if city_2 in graph_list:
            graph_list[city_2] += [city_1]
        else:
            graph_list[city_2] = [city_1]

    subgraphs_list = []
    #loop to determine the number of node of each connected subgraph
    while graph_list:
        subgraph = 0
        b = DFS(graph_list, list(graph_list.keys())[0])
        for n in b:
            graph_list.pop(n)
            subgraph += 1
        subgraphs_list.append(subgraph)
    cost = 0
    for sub in subgraphs_list:
        # print(len(sub))
        cost += (min(y * (sub - 1) + x, x * (sub)))
    print(cost)
