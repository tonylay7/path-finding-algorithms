import heapq

class Dijkstra:
    """Implementation of Dijkstra's Shortest Path Algorithm

    Attributes:
        graph (dict): the graph to compute on
        start_node (str): the starting node to compute on
        distances (dict): calculated best distances for each node on the graph from the start node
        parents_map (dict): mapping of nodes to parents based on best distance

    Methods:
        _calculate_distances(start_node): calculate the distances to all nodes starting from a specified start node
        get_shortest_path(end_node): Return the shortest path from the start node a specified end node
    """
    
    def __init__(self, graph,start_node):
        self.graph = graph # Stores the graph
        self.start_node = start_node # Stores the starting node
        self.distances = {} # Stores best distances
        self.parents_map = {} # Stores parents of the best nodes (nodes with the lowest accumulative distances)
        self._calculate_distances(start_node) # Calculate best distances to each node from the starting node

    def _calculate_distances(self, start_node):
        """Calculate the distances to all nodes starting from a specified start node
        Args:
            start_node (str): the starting node on the graph 
        """
        # Initialise all distances to infinity as we don't know the distance for each node
        self.distances = {node: float('infinity') for node in self.graph}

        # We start at the start node so we know the distance is 0
        self.distances[start_node] = 0

        # A priority queue is used to keep track of nodes that need to be processed
        # Nodes with the lowest distance are considered 'high priority'
        priority_queue = [(0, start_node)]

        # While the priority queue is not empty
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # If the distance is greater than what we've already got, don't bother processing further through this rute
            if current_distance > self.distances[current_node]:
                continue

            # For each neighbour (adjacent) node, compute the distances and update our dictionary of distances as necessary
            for neighbour, weight in self.graph[current_node].items():
                distance = current_distance + weight

                # If the distance is better (lower) than what we have in our dictionary, update the best distance and note down its parent-child relationship in parents_map
                if distance < self.distances[neighbour]:
                    self.parents_map[neighbour] = current_node
                    self.distances[neighbour] = distance
                    heapq.heappush(priority_queue, (distance, neighbour))

    def get_shortest_path(self,end_node):
        """Return the shortest path from the start node a specified end node
        Args:
            end_node (str): a destination node on the graph 
        Returns:
            path (list): the shortest path
        """
        current_node = end_node
        path = [current_node]
        
        # Backtrack through the parents_map dict until we find the 'highest parent' which would be the starting node
        while current_node != self.start_node:
            current_node = self.parents_map[current_node]
            path.append(current_node)
        path.reverse()
        return path

graph = {
    'A': {'B': 4, 'C': 7, 'D': 2, 'F': 9},
    'B': {'A': 5, 'D': 3, 'C': 1, 'E': 4},
    'C': {'B': 9, 'A': 15, 'D': 4, 'E': 2, 'F': 6},
    'D': {'A': 6, 'B': 6, 'C': 1, 'E': 8},
    'E': {'D': 3, 'C': 1, 'F': 1},
    'F': {'C': 8, 'E': 5},
}

dijkstra = Dijkstra(graph,'A')

print(dijkstra.distances)
# >> {'A': 0, 'B': 4, 'C': 3, 'D': 2, 'E': 5, 'F': 6}
print(dijkstra.get_shortest_path('E'))
# >> ['A', 'D', 'C', 'E']
