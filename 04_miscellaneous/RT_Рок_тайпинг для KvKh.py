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
for well in db.selectedWellList():
	ds = "Repsol_PPeval"
	var = "K_phi"
	rt_name_vik = "rt_vik_kphi"
	rt_name_leu = "rt_leu_kphi"
	kphi = db.variableLoad(well, ds, var)
	db.variableDuplicate(well, ds, var, rt_name_vik)
	#db.variableDuplicate(well, ds, var, rt_name_leu)
	rt_vik = db.variableLoad(well, ds, rt_name_vik)
	#rt_leu = db.variableLoad(well, ds, rt_name_leu)
	func = lambda x: x*0
	rt_vik = map(func, rt_vik)
	#rt_leu = map(func, rt_leu)
	index_vik = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	#index_leu = db.datasetZoneIndice(well, ds, "ZONATION", "Leushinskaya")
	print index_vik
	#print rt_vik
	for i in range(len(kphi))[index_vik[0]:index_vik[1]]:
		if kphi[i] <= 15:
			rt_vik[i] = 3
		elif kphi[i] > 15 and kphi[i] < 71:
			rt_vik[i] = 2
		elif kphi[i] >= 71:
			rt_vik[i] = 1
	#for i in range(len(kphi))[index_leu[0]:index_leu[1]]:
		#if kphi[i] <= 4:
			#rt_leu[i] = 6
		#if kphi[i] >= 4 and kphi[i] < 22:
			#rt_leu[i] = 6
		#elif kphi[i] >= 22 and kphi[i] < 76:
			#rt_leu[i] = 5
		#elif kphi[i] >= 76:
			#rt_leu[i] = 4
	#print well
	print db.variableSave(well, ds, rt_name_vik, "Petrophysical Group", "unitless", rt_vik)
	#print db.variableSave(well, ds, rt_name_leu, "Petrophysical Group", "unitless", rt_leu)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-10-11"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""