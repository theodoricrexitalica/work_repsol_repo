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
ds = "ELAN_Slb"
var = "VSND"
for well in db.selectedWellList():
	if db.variableExists(well, ds, var):
		v_sand = map(lambda x: x*0, db.variableLoad(well, ds, var))
db.variableSave(well, ds, "VSND", "Sand Volume Fraction", "v/v", v_sand)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-06-28"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""