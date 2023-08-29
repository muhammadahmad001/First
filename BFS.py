# Name : Muhammad Ahmad
# Roll No : 201370130
map = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Craiova': {'Rimnicu Vilcea': 146, 'Pitesti': 138, 'Drobeta': 120},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}
def bfs(start_state, goal_state):
    fring = [(start_state, [start_state], 0)]
    while fring:
        current_location, path, path_cost = fring.pop(0)
        if current_location == goal_state:
            print("Goal state reached!")
            print("Full path:", path)
            print("Path cost:", path_cost)
            return
        for neighbor, distance in map[current_location].items():
            if neighbor not in path:
                new_path = path + [neighbor]
                new_path_cost = path_cost + distance
                fring.append((neighbor, new_path, new_path_cost))
        print("Expanding=> ", current_location)
        print("Current path=> ", path)
        print("Path cost=> ", path_cost)
        print("Fringe=> ", [node for node, _, _ in fring])
# Test
start ='Arad'
goal ='Bucharest'
bfs(start,goal)
