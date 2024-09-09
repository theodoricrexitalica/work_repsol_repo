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
	var = "PHIE"
	zone_para = "ZONES_PARA"
	phie = db.variableLoad(well, ds, var)
	perf = db.variableLoad(well, ds, "Perf")
	md = db.variableLoad(well, ds, db.referenceName(well,ds))
	zone_ind_2 = db.datasetZoneIndice(well, ds, zone_para, "HV2")[1]
	zone_ind_6 = db.datasetZoneIndice(well, ds, zone_para, "HV6")[0]

	db.variableDuplicate(well, ds,  db.referenceName(well,ds), "PHIEH")
	phie_h = db.variableLoad(well, ds, "PHIEH")
	func1 = lambda x: x==-9999
	phie_h = map(func1, phie_h)
	db.variableFamilyChange(well, ds, "PHIEH", " ")
	db.variableUnitChange(well, ds, "PHIEH", " ")
	quant = md[1] - md[0]
	
	for i in range(len(md))[zone_ind_2:zone_ind_6:-1]:
		phie_h[i-1] =phie_h[i] + phie[i]*quant
	
	db.variableSave(well, ds, "PHIEH", " ", " ", phie_h)
	
	#zone_ind_6 = db.datasetZoneIndice(well, ds, zone_para, "HV6")
	#zone_ind_5 = db.datasetZoneIndice(well, ds, zone_para, "HV5")
	#zone_ind_4 = db.datasetZoneIndice(well, ds, zone_para, "HV4")
	#zone_ind_3 = db.datasetZoneIndice(well, ds, zone_para, "HV3")
	#zone_ind_2 = db.datasetZoneIndice(well, ds, zone_para, "HV2")
	print well
	#print "HV6:", phie_h[zone_ind_6[1]], phie_h[zone_ind_6[0]], round(phie_h[zone_ind_6[0]] - phie_h[zone_ind_6[1]],1)
	#print "HV5:", phie_h[zone_ind_5[1]], phie_h[zone_ind_5[0]], round(phie_h[zone_ind_5[0]] - phie_h[zone_ind_5[1]],1)
	#print "HV4:", phie_h[zone_ind_4[1]], phie_h[zone_ind_4[0]], round(phie_h[zone_ind_4[0]] - phie_h[zone_ind_4[1]],1)
	#print "HV3:", phie_h[zone_ind_3[1]], phie_h[zone_ind_3[0]], round(phie_h[zone_ind_3[0]] - phie_h[zone_ind_3[1]],1)
	#print "HV2:", phie_h[zone_ind_2[1]], phie_h[zone_ind_2[0]], round(phie_h[zone_ind_2[0]] - phie_h[zone_ind_2[1]],1)
	
	zone_ind_oil = db.datasetZoneIndice(well, ds, "Repsol_Fluid", "Vik_TopOil")
	#print "Vik_TopOil:",  round(phie_h[zone_ind_oil[1]],2), round(phie_h[zone_ind_oil[0]],2), round(phie_h[zone_ind_oil[0]]-phie_h[zone_ind_oil[1]],2)
	for i in range(len(md)):
		if perf[i]== 1 and perf[i+1] != 1:
			perf_top = perf[i]
	print perf_top

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-07-15"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""