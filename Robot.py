import numpy as np 
class Diif_Robot:

    def __init__(self,r,L,robot_state):
        self.r = r
        self.L = L
        self.y = robot_state[0]
        self.x = robot_state[1] 
        self.theta = robot_state[2]
        

    def forward_kinematics(self,phi_dot_r,phi_dot_l,dt):
        
        J = np.array([[(self.r/2)*np.sin(self.theta),(self.r/2)*np.sin(self.theta)],[(self.r/2)*np.cos(self.theta),(self.r/2)*np.cos(self.theta)],[self.r/(self.L),-self.r/(self.L)]])
        phi_dot = np.array([phi_dot_r,phi_dot_l])
        state = np.matmul(J,phi_dot)*dt
        self.y += state[0]
        self.x += state[1]
        self.theta += state[2]

        return np.array([self.y,self.x,self.theta])
    
    
    def get_state(self):
        return np.array([self.y,self.x,self.theta])
    
    def get_angular_velocity(self,v,omega):
        phi_dot_l = self.r*v/2 - self.L*omega/2
        phi_dot_r = self.r*v/2 + self.L*omega/2
        return np.array([phi_dot_r,phi_dot_l])
    
    def motion_model(self, u, dt):
        v = u[0]
        omega = u[1]
        phi_dot = self.get_angular_velocity(v,omega)
        return self.forward_kinematics(phi_dot[0],phi_dot[1],dt)
    
  




