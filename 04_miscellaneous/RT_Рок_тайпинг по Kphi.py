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
	ds = "Repsol_PPeval"
	var = "K_phi_logs"
	rt_name = "rt_kphi_logs_N"
	kphi = db.variableLoad(well, ds, var)
	db.variableDuplicate(well, ds, var, rt_name)
	rt_logs = db.variableLoad(well, ds, rt_name)
	func = lambda x: x*0
	rt_logs = map(func, rt_logs)
	index_vik = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	index_leu = db.datasetZoneIndice(well, ds, "ZONATION", "Leushinskaya")
	print "Vik", index_vik, "Leu", index_leu
	for i in range(len(kphi))[index_vik[0]:index_vik[1]]:
		if kphi[i] <= 15:
			rt_logs[i] = 3
		elif kphi[i] > 15 and kphi[i] < 71:
			rt_logs[i] = 2
		elif kphi[i] >= 71:
			rt_logs[i] = 1
	#for i in range(len(kphi))[index_leu[0]:index_leu[1]]:
		#if kphi[i] <= 4:
			#rt_logs[i] = 7
		#if kphi[i] >= 4 and kphi[i] < 22:
			#rt_logs[i] = 6
		#elif kphi[i] >= 22 and kphi[i] < 76:
			#rt_logs[i] = 5
		#elif kphi[i] >= 76:
			#rt_logs[i] = 4
	
	print db.variableSave(well, ds, rt_name, "Petrophysical Group", "unitless", rt_logs), well

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-10-11"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""