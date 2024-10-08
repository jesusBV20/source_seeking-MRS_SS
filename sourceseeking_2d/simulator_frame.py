import numpy as np

from .toolbox import L_sigma

"""
Clase común a todas las simulac iones
  * x0: [t0, p0, v0, ...]
  * n: dimensión del espacio real
  ---------------------------------
  * P: matriz de posiciones (N x n)
  * V: matriz de posiciones (N x n)
"""
class sim_frame:
  def __init__(self, n_agents, x0, dt):
    self.t0 = x0[0]              # Tiempo inicial de la simulación (s)
    self.tf = x0[0]              # Tiempo actual de la simulación (s)
    self.dt = dt                 # Pasos temporales en la simulación (s)

    self.N  = n_agents           # Número de agentes simulados

    # Lista con vectores de estado
    self.states = x0[1:]

  """
  Aproximación para la dirección de ascenso.
    * sigma: vector (N x 1)
    * X: matriz de posiciones relativas al centroide (N x n)
  """
  def L_sigma(self, X, sigma, denom=None):
    return L_sigma(X, sigma, denom)

  """
  Euler integrator.
    * dX: lista de matrices con las mismas dimensiones que self.states.
  """
  def frame_int_euler(self, dX): #TODO: Poder elegir entre RK4 y euler
    self.tf = self.tf + self.dt
    if len(self.states) == len(dX):
      for i in range(len(self.states)):
        self.states[i] = self.states[i] + dX[i] * self.dt
    else:
      print("El vctor dX no tiene el mismo tamaño que el vector de estados.")