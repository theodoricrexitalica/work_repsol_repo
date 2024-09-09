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
ds = "Repsol_PPeval"
print "Well; MD; PHIT; PHIE; SWT; SWE; SWI; Zones"
s = ";"
for well in db.selectedWellList():
	if "Zones" in ds:
		print "Zones in PPeval"
	else:
		db.variableCopy(well, "ZONATION", "Zones", ds, "Zones")
	md = db.variableLoad(well, ds, db.referenceName(well,ds))
	phit = db.variableLoad(well, ds, "PHIT")
	phie = db.variableLoad(well, ds, "PHIE")
	swt = db.variableLoad(well, ds, "SWT")
	swe = db.variableLoad(well, ds, "SWE")
	swi = db.variableLoad(well, ds, "SWI")
	zones = db.variableLoad(well, ds, "Zones")
	for i in range(len(md)):
		print well, s, md[i], s, phit[i], s, phie[i], s, swt[i], s, swe[i], s, swi[i], s, zones[i]

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-11-06"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""