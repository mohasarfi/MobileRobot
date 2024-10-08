import numpy as np
import random
from config import map_height, map_width, num_obstacles, obstacle_size

class Map_Generator:
    def __init__(self, seed, width=map_width, height=map_height, numb_of_obstacles=num_obstacles, obs_size=obstacle_size, margins=(2, 2)):
        self.width = width
        self.height = height
        self.numb_of_obstacles = numb_of_obstacles
        self.seed = seed
        self.obstacle_size = obs_size
        self.margins = margins
        
        np.random.seed(self.seed)
        random.seed(self.seed)
        
        self.map = np.zeros((self.height, self.width))  # Initialize with free space
        self.generate_maze()

    def generate_maze(self):
        # Initialize the maze with free space
        maze = np.zeros((self.height, self.width), dtype=bool)
        
        # Starting point
        start = (1, 1)
        maze[start] = True
        
        # Stack for DFS
        stack = [start]
        
        while stack:
            current = stack[-1]
            neighbors = self.get_unvisited_neighbors(current, maze)
            
            if neighbors:
                neighbor = random.choice(neighbors)
                self.remove_wall(current, neighbor, maze)
                stack.append(neighbor)
            else:
                stack.pop()
        
        self.map = (1 - maze.astype(int))  # Invert free spaces to obstacles and vice versa

    def get_unvisited_neighbors(self, cell, maze):
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        neighbors = []
        for d in directions:
            neighbor = (cell[0] + d[0], cell[1] + d[1])
            if 0 <= neighbor[0] < self.height and 0 <= neighbor[1] < self.width and not maze[neighbor]:
                neighbors.append(neighbor)
        return neighbors

    def remove_wall(self, current, neighbor, maze):
        between = ((current[0] + neighbor[0]) // 2, (current[1] + neighbor[1]) // 2)
        maze[between] = True
        maze[neighbor] = True



    def ref_map(self):
        # Change borders to obstacles (now representing free space as 0)
        finalMap = self.map.copy()
        return finalMap


# if __name__ == "__main__":
#     generator = Map_Generator(seed=np.random.randint(1,1000))
#     map_with_obstacles = generator.ref_map()

#     import matplotlib.pyplot as plt
#     plt.figure(figsize=(10, 10))
#     plt.imshow(np.subtract(1,map_with_obstacles), cmap='gray', vmin=0, vmax=1,origin='lower')
#     plt.show()



# import numpy as np
# from config import map_height, map_width, num_obstacles, obstacle_size
# class Map_Generator:
#     def __init__(self, seed, width = map_width, height = map_height , numb_of_obstacles = num_obstacles, obs_size = obstacle_size, margins=(2, 2)):
#         self.width = width
#         self.height = height
#         self.numb_of_obstacles = numb_of_obstacles
#         self.seed = seed
#         self.obstacle_size = obs_size
#         self.margins = margins
        
#         np.random.seed(self.seed)
        
#         self.map = np.zeros((self.width, self.height))
#         self.generate_obstacles()
#         self.apply_obstacles_to_map()

#     def generate_obstacles(self):
#         marginW, marginH = self.margins
#         wMin, wMax = marginW, self.width - marginW
#         hMin, hMax = marginH, self.height - marginH
        
#         self.obstaclePositions = np.array([
#             (np.random.randint(wMin, wMax), np.random.randint(hMin, hMax))
#             for _ in range(self.numb_of_obstacles)
#         ])

#     def apply_obstacles_to_map(self):
#         for (w, h) in self.obstaclePositions:
#             obWidth = np.random.randint(self.obstacle_size[0], self.obstacle_size[0] + 1)
#             obHeight = np.random.randint(self.obstacle_size[1], self.obstacle_size[1] + 1)
            
#             for i in range(obWidth):
#                 for j in range(obHeight):
#                     wI, hJ = min(w + i, self.width - 1), min(h + j, self.height - 1)
#                     self.map[wI, hJ] = 1

#     def ref_map(self):
#         #change borders to obstacles 
#         finalMap = self.map.copy()
#         finalMap[0, :] = 1
#         finalMap[-1, :] = 1
#         finalMap[:, 0] = 1
#         finalMap[:, -1] = 1
#         return finalMap

