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
#Считает роктайпы по vsh для леушинки

for well in db.selectedWellList():
	ds = "Repsol_PPeval"
	var = "VSH"
	rt_name = "rt_vsh_N"
	vsh = db.variableLoad(well, ds, var)
	db.variableDuplicate(well, ds, var, rt_name)
	rt_logs = db.variableLoad(well, ds, rt_name)
	func = lambda x: x*0
	rt_logs = map(func, rt_logs)
	index_vik = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	index_leu = db.datasetZoneIndice(well, ds, "ZONATION", "Leushinskaya")
	#print "Vik", index_vik, "Leu", index_leu
	#for i in range(len(vsh))[index_vik[0]:index_vik[1]]:
		#if vsh[i] >= 0.62:
			#rt_logs[i] = 3
		#elif vsh[i] > 0.45 and vsh[i] < 0.62:
			#rt_logs[i] = 2
		#elif vsh[i] <= 0.45:
			#rt_logs[i] = 1
	for i in range(len(vsh))[index_leu[0]:index_leu[1]]:
		if vsh[i] >= 0.8:
			rt_logs[i] = 7
		if vsh[i] >= 0.68 and vsh[i] < 0.8:
			rt_logs[i] = 6
		elif vsh[i] > 0.55 and vsh[i] < 0.68:
			rt_logs[i] = 5
		elif vsh[i] <= 0.55:
			rt_logs[i] = 4
	
	print db.variableSave(well, ds, rt_name, "Petrophysical Group", "unitless", rt_logs), well

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-10-11"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""