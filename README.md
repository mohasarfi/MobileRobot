# MobileRobot
This repository contains the 2D simulation environment of a mobile robot.

It should contain the following files:
- env_generator.py # Generates the environment including static and dynamic obstacles
- robot.py # The kinematic model of the robot(s)
- perception.py # The perception model including the sensor model which are LIDAR, IMU, Accelerometer, and camera
- Localization.py # The localization model based on EKF, UKF, and Particle Filter
- mapping.py # The mapping model. Ideally, it should be SLAM
- MotionPlanning.py # The motion planning model. It should include the path planning and trajectory planning
- control.py # The control model. It should include the PID controller, MPC, and LQR
- Exploration.py # The exploration model. It should include the frontier-based exploration and information gain-based exploration
- TaskAllocation.py # The task allocation model. It should include the auction-based task allocation and the market-based task allocation
- main.py # The main file that runs the simulation
