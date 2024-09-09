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
import TechlogStat as ts

for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		nmr = db.variableLoad(well,ds, "FFV_16MS")
		nmr_smooth = ts.gaussianSmooth(nmr, 20)
		db.variableSave(well, ds, "FFV_16MS_smooth3m", "NMR Free Fluids", "V/V", nmr_smooth)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-05"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""