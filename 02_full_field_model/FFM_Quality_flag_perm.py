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
	var = "Reservoir Permeability" 
	db.variableDuplicate(well, ds, var, "Accept")
	list = db.variableLoad(well, ds, "Accept")
	func = lambda x: x*0+1
	list = map(func, list)
	db.variableSave(well, ds, "Accept", "", "", list)
	comments = db.variableLoad(well, ds, "Comments")
	flag = db.variableLoad(well, ds, "Accept")
	for i in range(len(flag)):
		if comments[i] != "":
			flag[i] = 0
		else:
			flag[i] = 1
	db.variableSave(well, ds, "Accept", "", "", flag)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-08-14"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""