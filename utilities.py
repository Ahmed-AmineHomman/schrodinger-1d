from functools import partial
from typing import Callable

import numpy as np


class PotentialFactory:
    """
    Factory class building potentials.

    When called, returns the potential function corresponding to the provided name & parameter.
    All methods take the following inputs:

    - x: ``np.ndarray``
    - t: ``float``

    All methods take the following parameters:

    - alpha: ``float``, related to the position ``x``
    - omega: ``float``, related to the time ``t``.

    Notes
    -----
    The potentials returned by this instance might be physically absurd.
    They are just implemented for demonstration purposes.
    """
    _supported_potentials = ["harmonic_ti", "trigonometric_ti", "harmonic_td", "trigonometric_td"]

    @staticmethod
    def harmonic_ti(x: np.ndarray, t: float, alpha: float, omega: float) -> np.ndarray:
        """ Time-independent Harmonic oscillator potential. """
        return 0.5 * alpha * alpha * x ** 2

    @staticmethod
    def trigonometric_ti(x: np.ndarray, t: float, alpha: float, omega: float) -> np.ndarray:
        """ Time-independent Trigonometric potential. """
        return alpha * np.cos(x) + (1.0 - alpha) * np.sin(x)

    @staticmethod
    def harmonic_td(x: np.ndarray, t: float, alpha: float, omega: float) -> np.ndarray:
        """ Time-dependent Harmonic oscillator potential. """
        return 0.5 * alpha * alpha * x ** 2 * (1.0 + omega * t) ** 2

    @staticmethod
    def trigonometric_td(x: np.ndarray, t: float, alpha: float, omega: float) -> np.ndarray:
        """ Time-dependent Trigonometric potential. """
        return alpha * np.cos(omega * t * x) + (1.0 - alpha) * np.sin(omega * t * x)

    def __call__(self, name: str, alpha: float, omega: float) -> Callable:
        if name not in self._supported_potentials:
            raise ValueError(f"Potential {name} is not supported")
        return partial(getattr(self, name), alpha=alpha, omega=omega)


def initial_wave_packet(
        x: np.ndarray,
        x0: float,
        sigma: float,
        k0: float
) -> np.ndarray:
    """
    Initial Gaussian wave packet.

    Parameters
    ----------
    x : ndarray
        Spatial grid points.
    x0 : float
        Center of the Gaussian wave packet.
    sigma : float
        Width of the Gaussian wave packet.
    k0 : float
        Wave number of the Gaussian wave packet.
    """
    return np.exp(-(x - x0) ** 2 / (2 * sigma ** 2)) * np.exp(1j * k0 * x)
