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
	ds = "FFM_Olesya"
	psvsh = "PSEUDO_VSH"
	db.variableDuplicate(well, ds, psvsh, "rt_vsh")
	rt_vsh = db.variableLoad(well, ds, "rt_vsh")
	for i in range(len(rt_vsh)):
		print  rt_vsh[i]
		if rt_vsh[i] <= 0.45 and rt_vsh[i]!= MissingValue:
			rt_vsh[i] = "1"
	
		elif rt_vsh[i] <= 0.62 and  rt_vsh[i] >= 0.45 and rt_vsh[i]!= MissingValue:
			rt_vsh[i] = "2"
		
		elif rt_vsh[i] >= 0.62 and rt_vsh[i]!= MissingValue:
			rt_vsh[i] = "3"
	print rt_vsh
	db.variableSave(well, ds, "rt_vsh", "", "", rt_vsh)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-08-12"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""