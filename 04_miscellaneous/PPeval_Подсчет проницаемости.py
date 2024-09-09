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
import TechlogStat as ts
ds = "Repsol_PPeval"
zn = "ZONATION"
perm_var = "PERM_COATES"

def PermCalc(well, ds, zn, perm_var):
	for well in db.selectedWellList():
		print well, ds
		zones = db.variableLoad(well, zn, "Zones")
		perm = db.variableLoad(well, ds, perm_var)
		for i in range(len(zones)-1):
			indice =  db.datasetZoneIndice(well, ds, zn, zones[i])
			ind1 = indice[0]
			ind2 = indice[1]
			print zones[i], round(ts.average(perm[ind1:ind2]), 1)
		print
	return

for well in db.selectedWellList():
	PermCalc(well, "Repsol_PPeval",  "ZONATION", "PERM_COATES")
	PermCalc(well, "Oreshko_NewAppr_PPeval",  "ZONATION", "KTIM_new")

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-06-29"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""