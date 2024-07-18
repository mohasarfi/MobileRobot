import numpy as np

def cells_in_lidar(lidarrange,map_width, map_height):
    i = int(map_height/2)
    j = int(map_width/2)
    count = 0 
    for x in range(i-(lidarrange+1),i+(lidarrange+1)):
        for y in range(j-(lidarrange+1),j+(lidarrange+1)):
            count += 1 
    return count 


# map related variables 
# summarize all variables in one or two lines 
angle_step = 0.0001
meas_phi = np.arange(-np.pi,np.pi,angle_step)
rmax , aplha , beta  = 8 , 1 , 0.008   
map_width , map_height = 50 , 50
map_size = (map_width,map_height)
num_obstacles = 10
obstacle_size = (4, 4)
min_distance = 10

# state, action, and reward related variables 
normigfactor = cells_in_lidar(rmax,map_width,map_height)
number_of_clusters = 10
action_size = number_of_clusters



    