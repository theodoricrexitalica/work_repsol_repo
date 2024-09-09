# -*- coding: utf-8 -*-
from __future__ import division
#Declarations
#The dictionary of parameters
#name,bname,type,family,unit,value,mode,description,group,min,max,list,enable,iscombocheckbox,isused
parameterDict = {}
try:
	if Parameter:
		pass
except NameError:
	class Parameter:
		def __init__(self, **d):
			pass
#DeclarationsEnd
ds = "RCAL"
var = ["Ambient Porosity", 							#0
			"Permeability Klinkenberg X", 			#1
			"Reservoir Permeability",					#2
			"Reservoir Porosity",							#3
			"Sample",												#4
			"Permeability Klinkenberg Y"]			#5
s = ";"
print "Well", s, "MD, m", s, var[4], s, var[0], s, var[1], s, var[2], s, var[5], s, var[3]
for well in db.selectedWellList():
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	sample = db.variableLoad(well, ds, var[4])
	phi_amb = db.variableLoad(well, ds, var[0])
	perm_kl_x = db.variableLoad(well, ds, var[1])
	perm_kl_y = db.variableLoad(well, ds, var[5])
	perm_res = db.variableLoad(well, ds, var[2])
	phi_res = db.variableLoad(well, ds, var[3])
	for i in range(len(md)):
		print well, s, md[i], s, sample[i], s, phi_amb[i], s,  perm_kl_x[i], perm_kl_y[i], s, perm_res[i], s, phi_res[i]

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-10-24"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""