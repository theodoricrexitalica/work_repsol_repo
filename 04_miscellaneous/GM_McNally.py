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
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		#mcnally = 185213*2.71**(-0.037*x)
		dtc = db.variableLoad(well, ds, "DTC")
		func = lambda x: 185213*2.71**(-0.037*x)
		result = map(func, dtc)
		db.variableSave(well, ds, "UCS_McNally", "Unconfined Compressive Strength", "psi", result)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-20"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""