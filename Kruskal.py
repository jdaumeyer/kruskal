def sort (e)
    return int(e[0])

def kruskal (e1, e2, e3, e4, e5, e6):
    edges = [[e1, "AB"], [e2, "BC"], [e3, "CD"], [e4, "DA"], [e5, "AC"], [e6, "BD"]]
    edges.sort(key=sort)
    keptEdges = []
    connections = 0
    i = 0

    while connections < 3:
        keptEdges.append(edges[i])
        i += 1;
        connections += 1;
    
    return keptEdges
    

running = False
while running:
    edge1 = input("Distance from A to B: ")
    edge2 = input("Distance from B to C: ")
    edge3 = input("Distance from C to D: ")
    edge4 = input("Distance from D to A: ")
    edge5 = input("Distance from A to C: ")
    edge6 = input("Distance from B to D: ")

    print(kruskal(edge1, edge2, edge3, edge4, edge5, edge6))

    if input("Quit(q) or Continue(c)?") == "q":
        running = False;
