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
#Нарезает лас-файлы по парасиквенсам.При подаче на вход пористоти или проницаемости, 
#надо заменить дублирование переменной в строках 15-16, а так переписать имя переменной
#с perm на phit и обратно
#Для работы надо запускать функцию каждый раз с указанием парасиквенса вручну!!!

paraseq = ["Vikulovskaya",
"HV6",
"HV5",
"HV4",
"HV3",
"HV2",
"HV1",
"HV0"]

def perm_cutter(paraseq, var, name):
	zone = db.datasetZoneIndice(well, ds, "ZONES_PARA",paraseq)
	#db.variableDuplicate(well, ds, "PERM_COATES", "FFM_" + name +"_" + paraseq)
	db.variableDuplicate(well, ds, "PHIT", "FFM_" + name +"_" + paraseq)
	list = db.variableLoad(well, ds, "FFM_" + name +"_" + paraseq)
	#print zone[0], zone[1]
	zone[1] = zone[1]+1
	for i in range(len(perm[:zone[0]])):
		var[i] = -999.25
	for i in range(len(perm[zone[1]:])):
		i = zone[1]+i
		var[i] = -999.25
	db.variableSave(well, ds,  "FFM_" + name +"_" + paraseq, "", "", var)
	return


for well in db.selectedWellList():
	print well
	ds = "Repsol_Petrel_110619"
	perm = db.variableLoad(well, ds, "PERM_COATES")
	phit = db.variableLoad(well, ds, "PHIT")
	
	#perm_cutter(paraseq[7], perm, "perm")
	perm_cutter(paraseq[7], phit, "phit")
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-06-10"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""