# -*- coding: utf-8 -*-
from __future__ import division
#Declarations
#The dictionary of parameters v2.0
#name,bname,type,family,measurement,unit,value,mode,description,group,min,max,list,enable,iscombocheckbox,isused
parameterDict = {}
try:
	if Parameter:
		pass
except NameError:
	class Parameter:
		def __init__(self, **d):
			pass
#DeclarationsEnd
for well in db.selectedWellList():
	ds = "Repsol_PPeval"
	calc = db.variableLoad(well, ds, "Calicite_log")
	perm = db.variableLoad(well, ds, "PERM_COATES")
	phit = db.variableLoad(well, ds, "PHIT")
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	db.variableDuplicate(well, ds, "PERM_COATES", "PERM_COATES_no_dens")
	for i in range(len(perm)):
		if phit[i] != MissingValue and calc[i] == 1:
			phit[i] = MissingValue
			perm[i] = MissingValue
	print well
	print "Phit", db.variableSave(well, ds, "PHIT_no_dens", "Porosity", "V/V", phit)
	print "Perm", db.variableSave(well, ds, "PERM_COATES_no_dens", "Permeability", "mD", perm)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-07-23"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""