from functools import partial

import matplotlib.pyplot as plt
import numpy as np

from Schrodinger1D import Schrodinger1D
from utilities import PotentialFactory, initial_wave_packet

# ----------
# Parameters
# ----------


# time & space discretization
L = 10.0  # Spatial extent of the grid
T = 2.0  # Maximum time
dx = 0.01  # Spatial step size
dt = 0.05  # Time step size

# physics parameters
m = 5.0  # Mass of the particle
hbar = 1.0  # Reduced Planck constant
sigma = 0.5  # Width of the initial wave packet
k0 = 5  # wave number of the initial wave paquet
alpha = 0.5  # position-related potential parameter
omega = 0.5  # time-related potential parameter

# ---------
# EXECUTION
# ---------


print(". initialize solver")
solver = Schrodinger1D(m=m, hbar=hbar, L=L, T=T)
potential = PotentialFactory()("harmonic_td", alpha=alpha, omega=omega)
paquet = partial(initial_wave_packet, x0=0.0, sigma=sigma, k0=k0)

print(". solve equation")
psi = solver.solve(dx=dx, dt=dt, potential=potential, paquet=paquet)

print(". plot results")
x = solver.get_spatial_grid(dx=dx)
t = solver.get_time_grid(dt=dt)
title_specs = dict(fontsize=16, fontweight='bold')

plt.figure(figsize=(10, 6))
plt.plot(x, np.abs(psi[:, 0]) ** 2, label="initial")
plt.plot(x, np.abs(psi[:, -1]) ** 2, label="final")
plt.title('Probability Density', **title_specs)
plt.xlabel('position')
plt.ylabel('density')
plt.legend()
plt.grid()
plt.savefig("density.png")

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ux, ut = np.meshgrid(x, t)
ax.plot_surface(ux, ut, np.abs(psi ** 2).T)
ax.set_title('Wave function', **title_specs)
ax.set_xlabel('position')
ax.set_ylabel('time')
ax.set_zlabel('wave function')
plt.savefig("wave_function.png")
