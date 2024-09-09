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
import TechlogStat as ts
s = ";"

for well in db.selectedWellList():
	ds = "RCAL"
	ds2 = "DST"
	ds3 = "Repsol_PPeval"
	

#Выгрузка данных по керну
	#db.variableCopy(well, "ZONATION", "Zones", ds, "Zones", "automatic")
	#por = db.variableLoad(well, ds, "Reservoir Porosity")
	#perm = db.variableLoad(well, ds, "Reservoir Permeability")
	#md = db.variableLoad(well, ds, db.referenceName(well, ds))
	#zones = db.variableLoad(well, ds, "Zones")
	#ind_vik = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	
	#for i in range(len(md))[ind_vik[0]:ind_vik[1]]:
		#print well, md[i], por[i], perm[i], zones[i]
	
	#ind_leu = db.datasetZoneIndice(well, ds, "ZONATION", "Leushinskaya")
	#for i in range(len(md))[ind_leu[0]:ind_leu[1]]:
		#print well, md[i], por[i], perm[i], zones[i]
	
			
#Выгрузка данных по DST в RCAL
	#db.variableCopy(well, ds2, "Perm_rel_oil", ds, "Res_DST_Perm", "automatic")
	#perm_dst = db.variableLoad(well, ds, "Res_DST_Perm")
	#por = db.variableLoad(well, ds, "Reservoir Porosity")
	#md = db.variableLoad(well, ds, db.referenceName(well, ds))
	#ind_vik = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	
	#list_por = []
	#list_perm = []
	#list_i = []
	#for i in range(len(md))[ind_vik[0]:ind_vik[1]]:
		#if perm_dst[i] != MissingValue:
			#list_i.append(i)
			#list_por.append(por[i])
			#list_perm.append(perm_dst[i])
	#print well, s, round(md[list_i[0]],0), "-", round(md[list_i[-1]],0), s, ts.average(list_por), s, ts.average(list_perm), s, "Vikulovskaya"
	
	#ind_leu = db.datasetZoneIndice(well, ds, "ZONATION", "Leushinskaya")
	#list_por = []
	#list_perm = []
	#list_i = []
	#for i in range(len(md))[ind_leu[0]:ind_leu[1]]:
		#if perm_dst[i] != MissingValue:
			#list_i.append(i)
			#list_por.append(por[i])
			#list_perm.append(perm_dst[i])
	#print well, s, round(md[list_i[0]],0), "-", round(md[list_i[-1]],0), s, ts.average(list_por), s, ts.average(list_perm), s, "Leushinskaya"


#Копирование МДТ_проницаемости из ХРТ в Repsol_PPeval и расчет 
	db.variableCopy(well, "XPT", "Perm_DDmob", ds3, "Perm_DDmob", "automatic")
	perm_mdt = db.variableLoad(well, ds3, "Perm_DDmob")
	por = db.variableLoad(well, ds3, "PHIT")
	md = db.variableLoad(well, ds3, db.referenceName(well, ds3))
	zones = db.variableLoad(well, ds3, "Zones")

#Включить для Викулова
	#ind_vik = db.datasetZoneIndice(well, ds3, "ZONATION", "Vikulovskaya")
	#for i in range(len(md))[ind_vik[0]:ind_vik[1]]:
		#if perm_mdt[i] != MissingValue:
			#print well, md[i], por[i]*100, perm_mdt[i], zones[i]

#Включить для Леушинки
	ind_leu = db.datasetZoneIndice(well, ds3, "ZONATION", "Leushinskaya")
	for i in range(len(md))[ind_leu[0]:ind_leu[1]]:
		if perm_mdt[i] != MissingValue:
			print well, md[i], por[i]*100, perm_mdt[i], zones[i]
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-03-19"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""