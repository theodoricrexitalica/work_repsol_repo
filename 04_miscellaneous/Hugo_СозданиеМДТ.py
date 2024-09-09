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
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		func = lambda x: x+1.6
		md2 = map(func, md)
		for i in range(len(md)):
			md.append(md2[i])
		md.sort()
		print md
		db.datasetCreate(well, "MDT_test", "MD", "Measured Depth", "m", md)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-21"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""