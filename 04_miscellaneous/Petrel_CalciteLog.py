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
	ds = "Repsol_Input"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	db.variableDuplicate(well,  ds, db.referenceName(well, ds), "Calicite_log")
	calcite_log = db.variableLoad(well, ds, "Calicite_log")
	func = lambda x: x*0
	calicite_log = map(func, calcite_log)
	print well, db.variableSave(well, ds, "Calicite_log", "Calcite Flag", "m", calicite_log)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-22"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""