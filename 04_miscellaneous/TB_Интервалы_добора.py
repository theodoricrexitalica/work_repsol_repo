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
	cutoff = 0.4
	ds = "RCAL"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	db.variableDuplicate(well, ds, db.referenceName(well,ds), "Core_dist")
	core_dist = db.variableLoad(well, ds, "Core_dist")
	func = lambda x: x*0
	core_dist = map(func, core_dist)
	for i in range(len(md))[:-1]:
		core_dist[i] = md[i+1]-md[i]
		if core_dist[i] >= cutoff:
			core_dist[i] = core_dist[i]
		else:
			core_dist[i] = -9999
	db.variableSave(well, ds, "Core_dist", "", "", core_dist)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-08-23"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""