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
	print well
	ds = "Repsol_PPeval"
	fluid_list = "Repsol_Fluid"
	
	if db.variableExists(well, ds, "Fluid_index"):
		db.variableDelete(well, ds, "Fluid_index")
	if db.variableExists(well, ds, "Fluids"):
		db.variableDelete(well, ds, "Fluids")
	if db.variableExists(well, ds, "Zones"):
		db.variableDelete(well, ds, "Zones")
	
	db.variableCopy(well, fluid_list, "Fluids", ds, "Fluids", "shift")
	db.variableCopy(well, "ZONATION", "Zones", ds, "Zones", "zonation") 
	
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	fluid_index = [i*0 for i in md]
	
	fluids = db.variableLoad(well, ds, "Fluids")
	zones = db.variableLoad(well, ds, "Zones")
	vikolovskaya_top = zones.index("Vikulovskaya")
	koshayskaya_top = zones.index("Koshayskaya")
	leushinskaya_top = zones.index("Leushinskaya")


	vik_oil_top = []
	vik_water_top = []
	vik_gas_top = vikolovskaya_top
	for i in range(len(fluids)):
		if fluids[i] == "Vik_TopGas":
			print "Vik_TopGas", md[i]
			vik_gas_top = i
		elif fluids[i] == "Vik_TopOil":
			print "Vik_TopOil", md[i]
			vik_oil_top = i
		elif fluids[i] == "Vik_TopWater":
			print "Vik_TopWater", md[i]
			vik_water_top = i
	for i in range(len(md))[vik_gas_top:vik_oil_top]:
		fluid_index[i] = 3
	for i in range(len(md))[vik_oil_top:vik_water_top]:
		fluid_index[i] = 2
	for i in range(len(md))[vik_water_top:koshayskaya_top]:
		fluid_index[i] = 1
	for i in range(len(md))[koshayskaya_top:leushinskaya_top]:
		fluid_index[i] = MissingValue
	

	leu_oil_top = []
	leu_water_top = []
	leu_gas_top = leushinskaya_top
	for i in range(len(fluids)):
		if fluids[i] == "Leu_TopGas":
			leu_gas_top = i
		elif fluids[i] == "Leu_TopOil":
			leu_oil_top = i
		elif fluids[i] == "Leu_TopWater":
			leu_water_top = i
	for i in range(len(md))[leu_gas_top:leu_oil_top]:
		fluid_index[i] = 3
	for i in range(len(md))[leu_oil_top:leu_water_top]:
		fluid_index[i] = 2
	for i in range(len(md))[leu_water_top:]:
		fluid_index[i] = 1
	#print fluid_index
	print db.variableSave(well, ds, "Fluid_index", "Fluid Code", "unitless", fluid_index), well
	db.variableDelete(well, ds, "Fluids")
	 

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-08-28"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""