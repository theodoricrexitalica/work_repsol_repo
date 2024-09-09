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
print "Well Fluid Top Bot NetPay Zone"
for well in db.selectedWellList():
	ds = "Repsol_Fluid"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	fluid = db.variableLoad(well, ds, "Fluids")
	gasz_ind = db.datasetZoneIndice(well, ds, ds, "Vik_TopGas")
	oilz_ind = db.datasetZoneIndice(well, ds, ds, "Vik_TopOil")
	watz_ind = db.datasetZoneIndice(well, ds, ds, "Vik_TopWater")
	gas_zone =  md[oilz_ind[0]] - md[gasz_ind[0]]
	oil_zone = md[watz_ind[0]] - md[oilz_ind[0]]
	print well, "Gas", round(md[gasz_ind[0]],2), round(md[oilz_ind[0]],2), round(gas_zone,2), "Vikulovskaya"
	print well, "Oil", round(md[oilz_ind[0]],2), round(md[watz_ind[0]],2), round(oil_zone,2), "Vikulovskaya"

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-03-20"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""