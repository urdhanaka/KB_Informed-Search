# import llibrary
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristic = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def addHeuristic(self, u, v):
        self.heuristic[u].append(v)

    def greedyBestFirstSearch(self, startPoint, endPoint):
        # flag to check the search result
        # 0 = success to find the path to end point
        # 1 = loop happens
        # 2 = can't find the path to end point 
        flag = 0
        currentCity = startPoint
        visited = set()
        cityOrder = list()

        visited.add(startPoint)
        cityOrder.append(startPoint)
        
        while(True):
            currentHeuristic = 1000
            tempCity = currentCity
            if (currentCity == endPoint):
                flag = 0
                break
            else:
                if currentCity in self.graph: # check if current node has edge 
                    for city in self.graph[currentCity]:
                        cityHeuristic = self.heuristic[city][0]
                        if cityHeuristic <= currentHeuristic:
                            currentHeuristic = self.heuristic[city][0]
                            tempCity = city
                else:
                    flag = 2
                    break

            currentCity = tempCity
            
            if currentCity in visited:
                flag = 1
                break
            
            visited.add(currentCity)
            cityOrder.append(currentCity)

        if (flag == 2): 
            print("Jalur menuju kota tujuan tidak ditemukan\n")
        elif (flag == 1):
            print("Terjadi loop pada saat pencarian:\n")
            for city in cityOrder:
                print(city, end="->")
                
            print(currentCity + "...\n")
        elif (flag == 0):
            print("Jalur ditemukan:\n")
            for i in range(len(cityOrder)):
                if i < len(cityOrder) - 1:
                    print(cityOrder[i], end="->")
                else:
                    print(cityOrder[i])
    
# Main function start here
g = Graph()

# add heuristic
g.addHeuristic("Magetan", 162)
g.addHeuristic("Surabaya", 0)
g.addHeuristic("Ngawi", 130)
g.addHeuristic("Ponorogo", 128)
g.addHeuristic("Madiun", 126)
g.addHeuristic("Bojonegoro", 60)
g.addHeuristic("Nganjuk", 70)
g.addHeuristic("Jombang", 36)
g.addHeuristic("Lamongan", 36)
g.addHeuristic("Gresik", 12)
g.addHeuristic("Sidoarjo", 22)
g.addHeuristic("Probolinggo", 70)
g.addHeuristic("Situbondo", 146)
g.addHeuristic("Bangkalan", 140)
g.addHeuristic("Sampang", 90)
g.addHeuristic("Pamekasan", 104)
g.addHeuristic("Sumenep", 150)

# add edge
g.addEdge("Magetan", "Ngawi")
g.addEdge("Magetan", "Madiun")
g.addEdge("Magetan", "Ponorogo")

g.addEdge("Surabaya", "Gresik")
g.addEdge("Surabaya", "Jombang")
g.addEdge("Surabaya", "Bangkalan")
g.addEdge("Surabaya", "Sidoarjo")

g.addEdge("Ngawi", "Magetan")
g.addEdge("Ngawi", "Madiun")
g.addEdge("Ngawi", "Bojonegoro")

g.addEdge("Ponorogo", "Madiun")
g.addEdge("Ponorogo", "Magetan")

g.addEdge("Madiun", "Magetan")
g.addEdge("Madiun", "Ngawi")
g.addEdge("Madiun", "Ponorogo")
g.addEdge("Madiun", "Nganjuk")

g.addEdge("Bojonegoro", "Ngawi")
g.addEdge("Bojonegoro", "Nganjuk")
g.addEdge("Bojonegoro", "Jombang")
g.addEdge("Bojonegoro", "Lamongan")

g.addEdge("Nganjuk", "Madiun")
g.addEdge("Nganjuk", "Bojonegoro")
g.addEdge("Nganjuk", "Jombang")

g.addEdge("Jombang", "Nganjuk")
g.addEdge("Jombang", "Bojonegoro")
g.addEdge("Jombang", "Surabaya")

g.addEdge("Lamongan", "Bojonegoro")
g.addEdge("Lamongan", "Gresik")

g.addEdge("Gresik", "Lamongan")
g.addEdge("Gresik", "Surabaya")

g.addEdge("Sidoarjo", "Surabaya")
g.addEdge("Sidoarjo", "Probolinggo")

g.addEdge("Probolinggo", "Sidoarjo")
g.addEdge("Probolinggo", "Situbondo")

g.addEdge("Situbondo", "Probolinggo")

g.addEdge("Bangkalan", "Surabaya")
g.addEdge("Bangkalan", "Sampang")

g.addEdge("Sampang", "Bangkalan")
g.addEdge("Sampang", "Pamekasan")

g.addEdge("Pamekasan", "Sumenep")
g.addEdge("Pamekasan", "Sampang")

g.addEdge("Sumenep", "Pamekasan")

# searching start here
g.greedyBestFirstSearch("Ngawi", "Surabaya")