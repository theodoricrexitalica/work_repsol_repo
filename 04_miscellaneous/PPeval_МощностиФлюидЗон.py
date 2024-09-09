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
	ds = "Repsol_Fluid"
	tvdss = db.variableLoad(well, "Index", "TVDSS")
	oil_zone = ["Vik_TopOil", "Leu_TopOil"]
	gas_zone = ["Vik_TopGas", "Leu_TopGas"]
	vik_ind_oil = db.datasetZoneIndice(well, "Index", ds, oil_zone[0])
	vik_ind_gas = db.datasetZoneIndice(well, "Index", ds, oil_zone[1])
	top_oil = tvdss[vik_ind_oil[0]:vik_ind_oil[1]][0]
	bot_oil = tvdss[vik_ind_oil[0]:vik_ind_oil[1]][-1]
	top_gas = tvdss[vik_ind_gas[0]:vik_ind_gas[1]][0]
	bot_gas = tvdss[vik_ind_gas[0]:vik_ind_gas[1]][-1]
	gas_thickness = round(bot_gas - top_gas,1)
	oil_thickness = round(bot_oil - top_oil,1)
	print well, gas_thickness, oil_thickness

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-04-08"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""