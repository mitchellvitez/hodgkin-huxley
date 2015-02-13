import equations

class Neuron:
	""" Implements the Hodgkin-Huxley model for a single cell """
	def __init__(self, capacitance, conductance, membranePotential, h, m, n):
		self.capacitance = capacitance
		self.conductance = conductance
		self.membranePotential = membranePotential
		self.time = 0
		self.h = equations.hOfT(self.membranePotential, self.time)
		self.m = equations.mOfT(self.membranePotential, self.time)
		self.n = equations.nOfT(self.membranePotential, self.time)

	def update(self, deltaT):
		self.time += deltaT
		self.h = equations.hOfT(self.membranePotential, self.time)
		self.m = equations.mOfT(self.membranePotential, self.time)
		self.n = equations.nOfT(self.membranePotential, self.time)

	def gOfK(self):
		return equations.gOfK(self.membranePotential, self.time)

	def gOfNa(self):
		return equations.gOfNa(self.membranePotential, self.h, self.m)
