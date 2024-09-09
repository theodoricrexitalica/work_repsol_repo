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
print "well", "H_calcite", "H_ps", "%"
for well in db.selectedWellList():
	ds = "Repsol_PPeval"
	calcite = db.variableLoad(well, ds, "Calicite_log")
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	hv3 = db.datasetZoneIndice(well, ds, "ZONES_PARA", "HV3")
	cc = 0
	for i in range(len(md))[hv3[0]:hv3[1]]:
		if calcite[i] > 0:
			cc +=1
	print well, cc*0.15, hv3[1]-hv3[0], round((cc*0.15)/( hv3[1]-hv3[0]),2)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-08-20"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""