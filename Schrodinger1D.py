from typing import Callable

import numpy as np


class Schrodinger1D:
    """
    Class implementing solvers for the one-dimensional variant of the Schrödinger equation.

    Parameters
    ----------
    hbar: float
        Value of the reduced Planck constant.
    m: float
        Mass of the particle.
    L: float
        Spatial extent of the grid (from -L/2 to L/2).
    T: float
        Maximum time.
    """

    def __init__(
            self,
            hbar: float,
            m: float,
            L: float,
            T: float,
    ):
        self.hbar: float = hbar
        self.m: float = m
        self.L: float = L
        self.T: float = T

    def get_spatial_grid(self, dx: float) -> np.ndarray:
        """
        Returns the grid of spatial positions corresponding to the position step.

        Parameters
        ----------
        dx: float
            Spatial step size.

        Returns
        -------
        ndarray
            Array of spatial positions.
        """
        return np.linspace(start=-0.5 * self.L, stop=0.5 * self.L, num=int(self.L / dx) + 1)

    def get_time_grid(self, dt: float) -> np.ndarray:
        """
        Returns the grid of timestamps corresponding to the time step.

        Parameters
        ----------
        dt: float
            Time step size.

        Returns
        -------
        ndarray
            Array of timestamps.
        """
        return np.linspace(start=0.0, stop=self.T, num=int(self.T / dt) + 1)

    def solve(
            self,
            dx: float,
            dt: float,
            potential: Callable,
            paquet: Callable
    ) -> np.ndarray:
        """
        Solves the Schrödinger equation for given parameters.

        Parameters
        ----------
        dx: float
            Spatial step size.
        dt: float
            Time step size.
        potential: callable
            Function that returns the potential energy at a given position in space & time.
        paquet: callable, optional
            Function that returns the initial wave paquet for a given space discretization.

        Returns
        -------
        ndarray
            Wave function values through space & time.
        """
        x = self.get_spatial_grid(dx=dx)
        t = self.get_time_grid(dt=dt)
        nx = len(x)
        nt = len(t)

        # precompute coefficients
        A = np.zeros(shape=(nx, nx), dtype=complex)
        B = np.zeros(shape=(nx, nx), dtype=complex)
        psi = np.zeros(shape=(nx, nt), dtype=complex)

        # Initialize A & B at t=0
        v0 = potential(x=x, t=0.0)
        for i in range(1, nx - 1):
            A[i, i - 1] = A[i, i + 1] = -self.hbar ** 2 / (4 * self.m * dx ** 2)
            A[i, i] = 1j * self.hbar / dt + self.hbar ** 2 / (2 * self.m * dx ** 2) + v0[i] / 2

            B[i, i - 1] = B[i, i + 1] = self.hbar ** 2 / (4 * self.m * dx ** 2)
            B[i, i] = 1j * self.hbar / dt - self.hbar ** 2 / (2 * self.m * dx ** 2) - v0[i] / 2

        # Time evolution
        psi[:, 0] = paquet(x=x)
        for i, tt in enumerate(t[1:]):
            # compute new values of potential
            vt = potential(x=x, t=tt)

            # update A & B with the new potential
            A[1:nx - 1, 1:nx - 1] += np.diag(vt[1:nx - 1] / 2)
            B[1:nx - 1, 1:nx - 1] -= np.diag(vt[1:nx - 1] / 2)

            # update interior points of the wave paquet
            psi[1:nx - 1:, i + 1] = np.linalg.solve(A[1:nx - 1, 1:nx - 1], B[1:nx - 1, 1:nx - 1].dot(psi[1:nx - 1, i]))

        return psi
