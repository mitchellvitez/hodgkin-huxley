import numpy

def dnDt(membranePotential, n):
	return alphaN(membranePotential) * (1 - n) - betaN(membranePotential) * n

def dmDt(membranePotential, m):
	return alphaM(membranePotential) * (1 - m) - betaM(membranePotential) * m

def dhDt(membranePotential, h):
	return alphaH(membranePotential) * (1 - h) - betaH(membranePotential) * h



def alphaN(membranePotential):
	return (.01 * membranePotential + 10) / (numpy.exp ((membranePotential + 10) / 10 -  1))

def betaN(membranePotential):
	return .125 * numpy.exp(membranePotential / 80)

def alphaM(membranePotential):
	return (0.1 * 25 - membranePotential) / (numpy.exp((25 - membranePotential)/10) - 1)

def betaM(membranePotential):
	return 4 * numpy.exp(-membranePotential / 18)

def alphaH(membranePotential):
	return .07 * numpy.exp(-membranePotential / 20)

def betaH(membranePotential):
	return 1 / (numpy.exp(0.1 * (30 - membranePotential)) + 1)



def nResting(membranePotential):
	return alphaN(membranePotential) / (alphaN(membranePotential) + betaN(membranePotential))

def mResting(membranePotential):
	return alphaM(membranePotential) / (alphaM(membranePotential) + betaM(membranePotential))

def hResting(membranePotential):
	return alphaH(membranePotential) / (alphaH(membranePotential) + betaH(membranePotential))



def nOfT(membranePotential, time):
	return nResting(membranePotential) - (nResting(membranePotential) - nResting(0)) * \
		numpy.exp(-time * alphaN(membranePotential) + betaN(membranePotential))

def mOfT(membranePotential, time):
	return mResting(membranePotential) - (mResting(membranePotential) - mResting(0)) * \
		numpy.exp(-time * alphaM(membranePotential) + betaM(membranePotential))

def hOfT(membranePotential, time):
	return hResting(membranePotential) - (hResting(membranePotential) - hResting(0)) * \
		numpy.exp(-time * alphaH(membranePotential) + betaH(membranePotential))



def gOfK(membranePotential, time):
	return .36 * nOfT(membranePotential, time) ** 4

def gOfNa(membranePotential, h, m):
	return 1.2 * m ** 3 * h