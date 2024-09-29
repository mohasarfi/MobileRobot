import numpy as np 
class Diif_Robot:

    def __init__(self,r,L,x_0 = 0 ,y_0=0 ,theta_0=0):
        self.r = r
        self.L = L
        self.x = x_0
        self.y = y_0
        self.theta = theta_0

    def forward_kinematics(self,phi_dot_r,phi_dot_l,dt):
        
        J = np.array([[self.r/2*np.cos(self.theta),self.r/2*np.cos(self.theta)],[self.r/2*np.sin(self.theta),self.r/2*np.sin(self.theta)],[self.r/(2*self.L),-self.r/(2*self.L)]])
        phi_dot = np.array([phi_dot_r,phi_dot_l])
        state = np.matmul(J,phi_dot)*dt
        self.x += state[0]
        self.y += state[1]
        self.theta += state[2]


        return np.array([self.y,self.x,self.theta])
    
    def get_state(self):
        return np.array([self.y,self.x,self.theta])
    
    def get_angular_velocity(self,v,omega):
        phi_dot_l = self.r*v/2 - self.L*omega/2
        phi_dot_r = self.r*v/2 + self.L*omega/2
        return np.array([phi_dot_r,phi_dot_l])
    
  




