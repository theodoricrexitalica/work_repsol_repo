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
	ds = "DST"
	ds_imp = "DST_imperial"
	db.datasetDuplicate(well, ds, well, ds_imp)
	db.variableUnitConvert(well, ds_imp, "Qoil", "bbl/d")
	db.variableUnitConvert(well, ds_imp, "Qwater", "bbl/d")
	db.variableUnitConvert(well, ds_imp, "BHP", "psi")
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-28"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""