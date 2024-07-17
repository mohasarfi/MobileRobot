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
        
        self.map = np.ones((self.height, self.width))  # Initialize with obstacles
        self.generate_random_office_layout()
        self.generate_random_obstacles()
        self.apply_obstacles_to_map()
        self.keep_largest_free_space()

    def generate_random_office_layout(self):
        # Define maximum and minimum room sizes
        min_room_size = (int(map_height/10), (int(map_width/10)))
        max_room_size = (2*int(map_height/10), 2*int(map_width/10))
        corridor_width = int(map_height/20)

        # List to hold room positions
        self.room_positions = []

        # Randomly place rooms
        for _ in range(random.randint(10, 20)):  # Fewer rooms to increase free space
            room_height = random.randint(min_room_size[0], max_room_size[0])
            room_width = random.randint(min_room_size[1], max_room_size[1])
            top_left_y = random.randint(1, self.height - room_height - 1)
            top_left_x = random.randint(1, self.width - room_width - 1)
            self.create_room(top_left_y, top_left_x, (room_height, room_width))
            self.room_positions.append((top_left_y, top_left_x, room_height, room_width))

        # Ensure all rooms are connected with corridors
        self.connect_rooms(corridor_width)

    def create_room(self, top_left_y, top_left_x, room_size):
        room_height, room_width = room_size
        for i in range(room_height):
            for j in range(room_width):
                if top_left_y + i < self.height and top_left_x + j < self.width:
                    self.map[top_left_y + i, top_left_x + j] = 0  # Free space

    def connect_rooms(self, corridor_width):
        for i in range(len(self.room_positions) - 1):
            y1, x1, h1, w1 = self.room_positions[i]
            y2, x2, h2, w2 = self.room_positions[i + 1]

            # Determine midpoints of the current and next room
            mid_y1, mid_x1 = y1 + h1 // 2, x1 + w1 // 2
            mid_y2, mid_x2 = y2 + h2 // 2, x2 + w2 // 2

            # Create a horizontal corridor first, then a vertical corridor
            if mid_x1 < mid_x2:
                self.map[mid_y1, mid_x1:mid_x2 + 1] = 0
            else:
                self.map[mid_y1, mid_x2:mid_x1 + 1] = 0

            if mid_y1 < mid_y2:
                self.map[mid_y1:mid_y2 + 1, mid_x2] = 0
            else:
                self.map[mid_y2:mid_y1 + 1, mid_x2] = 0

    def generate_random_obstacles(self):
        marginH, marginW = self.margins
        wMin, wMax = marginW, self.width - marginW
        hMin, hMax = marginH, self.height - marginH
        
        self.obstaclePositions = np.array([
            (np.random.randint(hMin, hMax), np.random.randint(wMin, wMax))
            for _ in range(self.numb_of_obstacles // 2)  # Fewer obstacles
        ])

    def apply_obstacles_to_map(self):
        for (h, w) in self.obstaclePositions:
            obWidth = np.random.randint(self.obstacle_size[0], self.obstacle_size[0] + 1)
            obHeight = np.random.randint(self.obstacle_size[1], self.obstacle_size[1] + 1)
            
            for i in range(obWidth):
                for j in range(obHeight):
                    wI, hJ = min(w + i, self.width - 1), min(h + j, self.height - 1)
                    if self.map[hJ, wI] == 0:  # Only place obstacles in free spaces
                        self.map[hJ, wI] = 1

    def keep_largest_free_space(self):
        visited = np.zeros_like(self.map, dtype=bool)
        largest_area = None
        max_size = 0

        for y in range(self.height):
            for x in range(self.width):
                if self.map[y, x] == 0 and not visited[y, x]:
                    size, stack = 0, [(y, x)]
                    component = []
                    while stack:
                        cy, cx = stack.pop()
                        if not visited[cy, cx]:
                            visited[cy, cx] = True
                            component.append((cy, cx))
                            size += 1
                            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                ny, nx = cy + dy, cx + dx
                                if 0 < ny < self.height and 0 < nx < self.width and self.map[ny, nx] == 0 and not visited[ny, nx]:
                                    stack.append((ny, nx))
                    if size > max_size:
                        max_size = size
                        largest_area = component

        # Set all non-largest free spaces to obstacles
        if largest_area is not None:
            self.map.fill(1)
            for y, x in largest_area:
                self.map[y, x] = 0

    
    def ref_map(self):
        # Change borders to obstacles 
        finalMap = self.map.copy()
        finalMap[0, :] = 1
        finalMap[-1, :] = 1
        finalMap[:, 0] = 1
        finalMap[:, -1] = 1
        return finalMap

# if __name__ == "__main__":
#     for _ in range(100):
#         generator = Map_Generator(seed=np.random.randint(1,1000))
#         map_with_obstacles = generator.ref_map()

#         # plt.figure(figsize=(5, 5))
#         # plt.imshow(np.subtract(1, map_with_obstacles), cmap='gray',origin="lower")
#         # plt.show()