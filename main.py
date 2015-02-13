from __future__ import division
from neuron import *
from visual import *
from visual.graph import *

DELTA_T = .000001
""" capacitance, conductance, membranePotential, time, h, m """
myNeuron = Neuron(40, 50, 60, 0, 10, 20)


# (red, green, blue)

G_Na = gcurve(color("#ffd700"))         # Depends directly on [m, h]                                        # gold: "#ffd700"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('Sodium Conductance'), xtitle=('Time (ms)'), ytitle=(''))


G_k = gcurve(color("#dcdcdc")           # Depends directly on nOfT(membranePotential, time)                 # gainsboro: "#dcdcdc"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('Potassium Conductance'), xtitle=('Time (ms)'), ytitle=(''))


alphaNFunc = gcurve(color("#deb887"))   # Depends on membranePotential                                      # burlywood: "#deb887"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('Alpha N'), xtitle=('Time (ms)'), ytitle=('Membrane Potential (mV)'))


betaNFunc = gcurve(color("#ffebcd"))    # Depends on membranePotential                                      #blanchedalmond: "#ffebcd"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('Beta N'), xtitle=('Time (ms)'), ytitle=('Membrane Potential (mV)'))


alphaMFunc = gcurve(color("#ffefd5"))   # Depends on membranePotential                                      #papayawhip: "#ffefd5"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('Alpha M'), xtitle=('Time (ms)'), ytitle=('Membrane Potential (mV)'))


betaMFunc = gcurve(color("#4682b4"))    # Depends on membranePotential                                      #steelblue: "#4682b4"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('Beta M'), xtitle=('Time (ms)'), ytitle=('Membrane Potential (mV)'))


alphaHFunc = gcurve(color("#ff6347"))   # Depends on membranePotential                                      #tomato: "#ff6347"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('Alpha H'), xtitle=('Time (ms)'), ytitle=('Membrane Potential (mV)'))


betHFunc = gcurve(color("#ff6347"))     # Depends on membranePotential                                      #turquoise: "#40e0d0"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('Beta H'), xtitle=('Time (ms)'), ytitle=('Membrane Potential (mV)'))


nRestingFunc = gcurve(color("#9acd32")) # Depends on [alphaN, betaN]                                        #yellowgreen: "#9acd32"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('N Resting'), xtitle=('Time (ms)'), ytitle=(''))


mRestingFunc = gcurve(color("#fffacd")) # Depends on [alphaM, betaM]                                        #lemonchiffon: "#fffacd"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('M Resting'), xtitle=('Time (ms)'), ytitle=(''))


hRestingFunc = gcurve(color("#e9967a")) # Depends on [alphaH, betaH]                                        #darksalmon: "#e9967a"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('H Resting'), xtitle=('Time (ms)'), ytitle=(''))


nOfT = gcurve(color("#d2691e"))         # Depends on [nResting, membranePotential, alphaN, betaN, time]     #chocolate: "#d2691e"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('N(t)'), xtitle=('Time (ms)'), ytitle=(''))


mOfT = gcurve(color("#ffe4c4"))         # Depends on [mResting, membranePotential, alphaM, betaM, time]     #bisque: "#ffe4c4"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('M(t)'), xtitle=('Time (ms)'), ytitle=(''))


hOfT = gcurve(color("#dc143c"))         # Depends on [hResting, membranePotential, alphaH, betaH, time]     #crimson: "#dc143c"
scene1 = gdisplay(background=color.white, foreground=color.black, title=('H(t)'), xtitle=('Time (ms)'), ytitle=(''))


for i in range(100):
	myNeuron.update(DELTA_T)
	print myNeuron.gOfNa()
	print myNeuron.gOfK()
	print myNeuron.time

	print ""
	#Gna.plot(pos=(myNeuron.time, myNeuron.gOfNa()))
	Gk.plot(pos=(myNeuron.time, myNeuron.gOfK()))

	print "hi"
