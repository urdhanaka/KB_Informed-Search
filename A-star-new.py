from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristic = defaultdict(list)
        
    def addEdge(self, u, v, dist):
        self.graph[u].append((v, dist))
    
    def addHeuristic(self, u, v):
        self.heuristic[u].append(v)

    def aStarSearch(self, startPoint, endPoint):
        open_list = set([startPoint])
        closed_list = set([])
        
        g = {}
        g[startPoint] = 0
        
        parents = {}
        parents[startPoint] = startPoint
        
        while len(open_list) > 0:
            n = None
            
            for v in open_list:
                if n == None or g[v] + self.heuristic[v][0] < g[n] + self.heuristic[n][0]:
                    n = v
                    
            if n == None:
                print("Path doesn't exist")
                return None
            
            if n == endPoint:
                distanceTraveled = 0
                path = []
                
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]

                path.append(startPoint)
                path.reverse()

                for i in range(len(path) - 1):
                    for (city, dist) in self.graph[path[i]]:
                        if city == path[i + 1]:
                            distanceTraveled += dist
                    
                print(f'Path found: {path}\nDistance traveled: {distanceTraveled}')
                return path
        
            for (m, dist) in self.graph[n]:
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + dist
                else:
                    if g[m] > g[n] + dist:
                        g[m] = g[n] + dist
                        parents[m] = n
                        
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
                          
            open_list.remove(n)
            closed_list.add(n)

        print("Path doesn't exist")
        return None
    
g = Graph()

# add heuristic
g.addHeuristic("Magetan",       162)
g.addHeuristic("Surabaya",      0)
g.addHeuristic("Ngawi",         130)
g.addHeuristic("Ponorogo",      128)
g.addHeuristic("Madiun",        126)
g.addHeuristic("Bojonegoro",    60)
g.addHeuristic("Nganjuk",       70)
g.addHeuristic("Jombang",       36)
g.addHeuristic("Lamongan",      36)
g.addHeuristic("Gresik",        12)
g.addHeuristic("Sidoarjo",      22)
g.addHeuristic("Probolinggo",   70)
g.addHeuristic("Situbondo",     146)
g.addHeuristic("Bangkalan",     140)
g.addHeuristic("Sampang",       90)
g.addHeuristic("Pamekasan",     104)
g.addHeuristic("Sumenep",       150)

# add edge
g.addEdge("Magetan", "Ngawi",       32)
g.addEdge("Magetan", "Madiun",      22)
g.addEdge("Magetan", "Ponorogo",    34)

g.addEdge("Surabaya", "Gresik",     12)
g.addEdge("Surabaya", "Jombang",    72)
g.addEdge("Surabaya", "Bangkalan",  44)
g.addEdge("Surabaya", "Sidoarjo",   25)

g.addEdge("Ngawi", "Magetan",       32)
g.addEdge("Ngawi", "Madiun",        22)
g.addEdge("Ngawi", "Bojonegoro",    44)

g.addEdge("Ponorogo", "Madiun",     29)
g.addEdge("Ponorogo", "Magetan",    34)

g.addEdge("Madiun", "Magetan",      22)
g.addEdge("Madiun", "Ngawi",        30)
g.addEdge("Madiun", "Ponorogo",     29)
g.addEdge("Madiun", "Nganjuk",      48)

g.addEdge("Bojonegoro", "Ngawi",    44)
g.addEdge("Bojonegoro", "Nganjuk",  33)
g.addEdge("Bojonegoro", "Jombang",  70)
g.addEdge("Bojonegoro", "Lamongan", 42)

g.addEdge("Nganjuk", "Madiun",      48)
g.addEdge("Nganjuk", "Bojonegoro",  33)
g.addEdge("Nganjuk", "Jombang",     40)

g.addEdge("Jombang", "Nganjuk",     40)
g.addEdge("Jombang", "Bojonegoro",  70)
g.addEdge("Jombang", "Surabaya",    72)

g.addEdge("Lamongan", "Bojonegoro", 42)
g.addEdge("Lamongan", "Gresik",     14)

g.addEdge("Gresik", "Lamongan",     14)
g.addEdge("Gresik", "Surabaya",     12)

g.addEdge("Sidoarjo", "Surabaya",       25)
g.addEdge("Sidoarjo", "Probolinggo",    78)

g.addEdge("Probolinggo", "Sidoarjo",    78)
g.addEdge("Probolinggo", "Situbondo",   99)

g.addEdge("Situbondo", "Probolinggo",   99)

g.addEdge("Bangkalan", "Surabaya",  44)
g.addEdge("Bangkalan", "Sampang",   52)

g.addEdge("Sampang", "Bangkalan",   52)
g.addEdge("Sampang", "Pamekasan",   31)

g.addEdge("Pamekasan", "Sumenep",   54)
g.addEdge("Pamekasan", "Sampang",   31)

g.addEdge("Sumenep", "Pamekasan",   54)

# searching start here
g.aStarSearch("Magetan", "Surabaya")