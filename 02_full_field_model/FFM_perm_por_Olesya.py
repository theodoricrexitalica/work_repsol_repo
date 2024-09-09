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
print "Well MD,m TVDSS,m Porosity,v/v Permrability,mD, QC_vnigni, PS"
for well in db.selectedWellList():
	ds = "RCAL"
	ds_zone = "ZONES_PARA"
	
	db.variableCopy(well, ds_zone, "Paraseq", ds, "Paraseq", "automatic")
	por = db.variableLoad(well, ds, "Reservoir Porosity_vv")
	perm = db.variableLoad(well, ds, "Reservoir Permeability")
	qc = db.variableLoad(well, ds, "Accept")
	hv6 = db.datasetZoneIndice(well, ds, ds_zone, "HV6")
	hv3 = db.datasetZoneIndice(well, ds, ds_zone, "HV3")
	zones = db.variableLoad(well, ds, "Paraseq")
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	tvdss = db.variableLoad(well, ds, "TVDSS")
	list = []
	for i in range(len(md)):
		if zones[i] == "HV6" or zones[i] == "HV5" or zones[i] == "HV4" or zones[i] == "HV3"  and perm[i] != MissingValue:
			#print well, md[i], tvdss[i], por[i], perm[i],qc[i], zones[i]
			list.append(perm[i])
list.sort()
for i in list:
	print i

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-11-13"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""