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
	print well
	ds = "Repsol_Fluid"
	zone_name = db.variableLoad(well, ds, "Fluids")
	md = db.variableLoad(well, "Index", db.referenceName(well, "Index"))
	
	for i in zone_name:
		if i != "Vik_FLW" and i != "Leu_FWL":
			print i,
			ind = db.datasetZoneIndice(well, "Index", ds, i)
			print round(md[ind[0]],1), "-", round(md[ind[1]],1), "m MD"
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-06-21"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""