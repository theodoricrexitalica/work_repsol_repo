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
	ds = "RCAL"
	vik_ind = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	print well
	print "Core Vik: ", round(md[vik_ind[0]],1), "-", round(md[vik_ind[1]],1)
	leu_ind = db.datasetZoneIndice(well, ds, "ZONATION", "Leushinskaya")
	print "Core Leu: ", round(md[leu_ind[0]],1), "-", round(md[leu_ind[1]],1)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-21"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""