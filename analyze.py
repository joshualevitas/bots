import numpy as np
import matplotlib.pyplot as plt

back_leg_data = np.load("data/backlegsensorvalues.npy")
front_leg_data = np.load("data/frontlegsensorvalues.npy")
torso_data = np.load("data/torsosensorvalues.npy")

plt.plot(back_leg_data, label="back leg")
plt.plot(front_leg_data, label="front_leg")
plt.legend()
plt.show()
