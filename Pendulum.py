import numpy as np

# Physical constants
g = 9.8
L = 2
mu = 0.1  # air friction coefficient

theta_0 = np.pi / 3 # 60 degreed
theta_dot_0 = 0  # no initial angular velocity

# Define 2-ns order Ordinary Diff Eq
def theta_double_dot(theta, theta_dot):
  return -mu * theta_dot - (g/L)*np.sin(theta)
  
# Solve differential equation
def theta(t):
  # Initialize vector
  theta = theta_0
  theta_dot = theta_dot_0
  delta_t = 0.01
  
  for time in np.arange(0,t,delta_t):
    theta_double_dot = theta_double_dot(theta,theta_dot)
    theta += theta_dot*delta_t
    theta_dot += theta_double_dot*delta_t
  
  return theta
