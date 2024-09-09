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
#Считает статистику по парасиквенсам
s = ";"
print "well",s,"Phit_res",s,"Perm_res", "ISA1cm_avg"
ds_zn = "ZONES_PARA"
rcal = "RCAL"
prseq = "Paraseq"
isa1 = "ISA 1 cm SHIFT"
for well in db.selectedWellList():
	zone = db.variableLoad(well, ds_zn, prseq)
	por_res = db.variableLoad(well, rcal, "Reservoir Porosity")
	perm_res = db.variableLoad(well, rcal, "Reservoir Permeability")
	isa1cm = db.variableLoad(well, isa1, "ISA1cmsh")
	for i in range(len(zone)):
		if "H" in zone[i]:
			ind_rcal = db.datasetZoneIndice(well, rcal, ds_zn, zone[i]) #indecies of paraseq for RCAL-dataset
			try:
				phit_avg = ts.average(por_res[ind_rcal[0]:ind_rcal[1]])
				perm_avg = ts.average(perm_res[ind_rcal[0]:ind_rcal[1]])
			except:
				continue
			
			ind_isa =  db.datasetZoneIndice(well, isa1, ds_zn, zone[i]) #indecies of paraseq for ISA-dataset
			try:
				isa_avg = ts.average(isa1cm[ind_isa[0]:ind_isa[1]])
			except:
				continue
			print well, zone[i], s, phit_avg, s, perm_avg, s, isa_avg
			

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-01"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""