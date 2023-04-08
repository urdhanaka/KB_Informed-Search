from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.heuristic = defaultdict(list)

    def addEdge(self, u, v, dist):
        for i in range(len(v)):
            self.graph[u].append([v[i], dist[i]])

    def addHeuristic(self, u, v):
        self.heuristic[u].append(v)

    def aStarSearch(self, startPoint, endPoint):
        # flag to determine if the path could be found or not
        # also to determine if loop happens
        flag = 0
        currentCity = startPoint
        visited = set()
        cityOrder = []
        distance = 0

        visited.add(currentCity)
        cityOrder.append(currentCity)

        while(True):
            tempCity = currentCity
            currentValue = 20000
            if (currentCity == endPoint):
                flag = 0
                break
            else:
                if tempCity in self.graph:
                    distTotal = 0
                    for city in self.graph[currentCity]:
                        destination = city[0]
                        dist = city[1]
                        heuristic = self.heuristic[destination][0]
                        res = distance + dist + heuristic
                        print("heuristic: ", heuristic, "| destination", destination, "| res: ", res)
                        if res <= currentValue:
                            tempCity = destination
                            currentValue = res
                            distTotal = dist
                    distance += distTotal
                    print("currentCity: ", currentCity, "| tempCity: ", tempCity, "| distance: ", distance)
                    print("distTotal: ", distTotal, "| currentValue: ", currentValue)
                    print("\n")
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

            print(currentCity + "->...\n")
        elif (flag == 0):
            print("Jalur ditemukan:\n")
            for i in range(len(cityOrder)):
                if i < (len(cityOrder) - 1):
                    print(cityOrder[i], end="->")
                else:
                    print(cityOrder[i])
            print(f"Total distance traveled: {distance}")

# Main function start here
g = Graph()

# add heuristic
g.addHeuristic("Arad",       366)
g.addHeuristic("Sibiu",       253)
g.addHeuristic("Bucharest",       0)
g.addHeuristic("Fagaras",       178)
g.addHeuristic("Pitesti",       100)
g.addHeuristic("Rimnicu Vilcea",       193)
g.addHeuristic("Craiova",       160)
g.addHeuristic("Drobeta",       242)
g.addHeuristic("Mehadia",       241)
g.addHeuristic("Lugoj",       244)
g.addHeuristic("Timisoara",       329)
g.addHeuristic("Zerind",       374)
g.addHeuristic("Oradea",       380)
g.addHeuristic("Giurgiu",       77)
g.addHeuristic("Urziceni",       80)
g.addHeuristic("Hirsova",       151)
g.addHeuristic("Eforie",       161)
g.addHeuristic("Vaslui",       199)
g.addHeuristic("Iasi",       226)
g.addHeuristic("Neamt",       234)

# add edge
g.addEdge("Arad", ["Zerind", "Timisoara", "Sibiu"], [75, 118, 140])
g.addEdge("Zerind", ["Oradea", "Arad"], [71, 75])
g.addEdge("Oradea", ["Zerind", "Sibiu"], [71, 151])
g.addEdge("Timisoara", ["Arad", "Lugoj"], [118, 111])
g.addEdge("Lugoj", ["Timisoara", "Mehadia"], [111, 70])
g.addEdge("Mehadia", ["Lugoj", "Drobeta"], [70, 75])
g.addEdge("Drobeta", ["Mehadia", "Craiova"], [75, 120])
g.addEdge("Craiova", ["Drobeta", "Rimnicu Vilcea", "Pitesti"], [120, 146, 138])
g.addEdge("Rimnicu Vilcea", ["Sibiu", "Pitesti", "Craiova"], [80, 97, 146])
g.addEdge("Sibiu", ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"], [140, 151, 99, 80])
g.addEdge("Fagaras", ["Sibiu", "Bucharest"], [99, 211])
g.addEdge("Pitesti", ["Rimnicu Vilcea", "Craiova", "Bucharest"], [97, 138, 101])
g.addEdge("Bucharest", ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"], [211, 101, 90, 85])
g.addEdge("Giurgiu", ["Bucharest"], [90])
g.addEdge("Urziceni", ["Bucharest", "Hirsova", "Vaslui"], [85, 98, 142])
g.addEdge("Hirsova", ["Urziceni", "Eforie"], [98, 86])
g.addEdge("Eforie", ["Hirsova"], [86])
g.addEdge("Vaslui", ["Urziceni", "Iasi"], [142, 92])
g.addEdge("Iasi", ["Vaslui", "Neamt"], [92, 87])
g.addEdge("Neamt", ["Iasi"], [87])

g.aStarSearch("Arad", "Bucharest")