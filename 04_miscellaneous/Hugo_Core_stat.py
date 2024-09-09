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
	ds = "RCAL_stat"
	samples = db.variableLoad(well, ds, "RCAL_Reservoir Permeability_Number of values")
	phit = db.variableLoad(well, ds, "RCAL_Reservoir Porosity_Arithmetic mean")
	perm = db.variableLoad(well, ds, "RCAL_Reservoir Permeability_Arithmetic mean")
	
	md = db.variableLoad(well, "RCAL", db.referenceName(well, "RCAL"))
	vik_ind = db.datasetZoneIndice(well, "RCAL", "ZONATION", "Vikulovskaya")
	leu_ind = db.datasetZoneIndice(well, "RCAL", "ZONATION", "Leushinskaya")
	#print well
	print "Vikulovo"
	print  well, "Vik", "Depth: ", round(md[vik_ind[0]],0), "-", round(md[vik_ind[1]],0), "m"
	print well, "Vik", "Lenght: ", round(md[vik_ind[1]],0) - round(md[vik_ind[0]],0), "m"
	print well, "Vik", "PhiT,%: ", round(phit[0],3)*100
	print well, "Vik", "Perm, mD: ", round(perm[0],1)
	print well, "Vik", "Samples: ", samples[0], "plugs"
	##print "Phit: ", round((phit[0]*100),1), "%"
	#print "Kg avg: ", round(perm[0], 1), "mD"
	print ""
	print "Leushinskaya"
	print well,"Leu", "Depth: ", round(md[leu_ind[0]],0), "-", round(md[leu_ind[1]],0), "m"
	print well,"Leu", "Lenght: ", round(md[leu_ind[1]],0) - round(md[leu_ind[0]],0), "m"
	print well, "Vik", "PhiT,%: ", round(phit[2],3)*100
	print well, "Vik", "Perm, mD: ", round(perm[2],1)
	print well,"Leu",  "Samples: ", samples[2], "plugs"
	#print "Phit: ", round((phit[2]*100),1), "%"
	#print "Kg avg: ", round(perm[2], 1), "mD"
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-20"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""