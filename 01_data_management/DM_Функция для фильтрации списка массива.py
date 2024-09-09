# -*- coding: utf-8 -*-
from __future__ import division
#Declarations
#The dictionary of parameters
#name,bname,type,family,unit,value,mode,description,group,min,max,list,enable,iscombocheckbox,isused
parameterDict = {}
try:
	if Parameter:
		pass
except NameError:
	class Parameter:
		def __init__(self, **d):
			pass
#DeclarationsEnd
def myFunc(x):
	if x == -9.992500305175781:
		x = -9999
	return x

for well in db.wellList():
	for ds in db.datasetList(well):
		for var in db.selectedVariableList(well,ds):
			sw = db.variableLoad(well,ds,var)
			sw = map(myFunc, sw)
			db.variableSave(well, ds, var, "Water Saturation", "v/v", sw)
			print sw

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-09-26"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""