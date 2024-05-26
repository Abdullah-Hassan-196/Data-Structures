class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
#       self.weights = []



    def addvertex(self, n):
        self.vertices.append(n)
        self.edges.append([])
#        self.weights.append([])

    def addedge(self, fr, to, wgt=None):
        frinx = self.vertices.index(fr)
        toinx = self.vertices.index(to)
        self.edges[frinx].append(toinx)
#        self.weights[frinx].append(wgt)

    def Display(self):
        seen = [False] * len(self.vertices)
        self.DisplayAux(0, 0, seen)
        print()

    def DisplayAux(self, r, level, seen):
        if r != None and seen[r] == False:
            seen[r] = True
            print("    "*level, self.vertices[r], sep="")
            for c in self.edges[r]:
                self.DisplayAux(c, level+1, seen)

def main():
    # Create a new GraphButNotGood
    tg = Graph()

#   Add vertices to the Graph
    tg.addvertex(10)
    tg.addvertex(30)
    tg.addvertex(80)
    tg.addvertex(60)
    tg.addvertex(40)
    tg.addvertex(20)
    tg.addvertex(70)
    tg.addvertex(50)

#   Add edges to the Graph
    tg.addedge(30, 10)
    tg.addedge(30, 80)
    tg.addedge(40, 10)
    tg.addedge(20, 30)
    tg.addedge(50, 70)
    tg.addedge(10, 20)
    tg.addedge(60, 20)
    tg.addedge(60, 30)
    tg.addedge(70, 50)
    tg.addedge(30, 60)

    # Display Graph data
    print("Display Graph data")
    tg.Display()

    print()


main()
