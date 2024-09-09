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
#base equation  log10(Core Permeability) = + 46.6821 * Core Porosity - 13.9 уравнение от Франа из Geolog
#v1 log10(Core Permeability) = + 16.27288 * Core Porosity - 4.072498 coreZone без 7П, Y function of X, базовая версия
#v2 log10(Core Permeability) = + 38.513 * Core Porosity - 11.064 добавлена 7П, reduced major axis Y/X, новая версия
#v3 log10(Core Permeability) = + 28.834 * Core Porosity - 7.67 satZone, reduced major axis Y/X
#v4 log10(Core Permeability) = + 14.574 * Core Porosity - 3.405 satZone, Y function of X

for well in db.selectedWellList():
	ds = "Repsol_PPeval"
	name = "PERM_PHIT_16_no_calc"
	phit = db.variableLoad(well, ds, "PHIT_no_calc")
	vik = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	#hrz = db.datasetZoneIndice(well, ds, "ZONE_HRZ", "HRZ_well")
	db.variableDuplicate(well, ds, "PHIT", name)
	perm = db.variableLoad(well, ds, name)
	func = lambda x: x*0
	perm = map(func, perm)
	for i in range(len(phit))[vik[0]:vik[1]]:
	#for i in range(len(phit))[hrz[0]:hrz[1]]:
		#perm[i] = 10**(46.6821*phit[i]-13.9)
		#perm[i] = 10**(16.27*phit[i]-4.07)
		#perm[i] = 10**(38.513*phit[i]-11.064)
		#perm[i] = 10**(28.834*phit[i]-7.67)
		#perm[i] = 10**(14.574*phit[i]-3.405)
	db.variableSave(well, ds, name, "Permeability", "mD", perm)

#обнуляем значения в точках с плотняками
	calc = db.variableLoad(well, ds, "Calicite_log")
	perm = db.variableLoad(well, ds, name)
	for i in range(len(perm)):
		if perm[i] != MissingValue and calc[i] == 1:
			#phit[i] = MissingValue
			perm[i] = MissingValue
	print "Perm", db.variableSave(well, ds, name, "Permeability", "mD", perm)
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-08-23"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""