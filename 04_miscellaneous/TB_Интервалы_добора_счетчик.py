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
	ds = "RCAL"
	var = "Core_dist"
	core_dist = db.variableLoad(well, ds, var)
	vik = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	cc = 0
	for i in range(len(core_dist))[vik[0]:vik[1]]:
		if core_dist[i] != MissingValue:
			cc +=1
	print well, cc-1

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-08-29"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""