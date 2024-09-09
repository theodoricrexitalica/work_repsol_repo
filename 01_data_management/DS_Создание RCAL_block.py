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
	#ds = "Facies_Mark_sft"
	#var = "Facies"
	ds = "RCAL"
	var = "Reservoir Permeability"
	data = db.variableLoad(well, ds, var)
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	perm_top = []
	perm_bot = []
	md_list = []
	perm_list = []
	for i in range(len(data)):
		#perm_top.append(md[i]-0.015)
		#perm_bot.append(md[i]+0.015)
		md_list.append(md[i]-0.015)
		perm_list.append(data[i])
		md_list.append(md[i]+0.015)
		perm_list.append(MissingValue)
for i in range(len(md_list)):
	print md_list[i], perm_list[i]
	#print perm_top[i], data[i], perm_bot[i]
db.datasetCreate(well,"RCAL_block", "MD", "Measured Depth", "m", md_list)
db.variableCreate(well, "RCAL_block", var + " Avg", 1)
db.variableSave(well, "RCAL_block", var + " Avg", "Average Permeability", "mD", perm_list)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-12-13"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""