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

for well in db.selectedWellList():
	ds = "RCAL"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	vik_ind = db.datasetZoneIndice(well, "RCAL", "ZONATION", "Vikulovskaya")
	leu_ind = db.datasetZoneIndice(well, "RCAL", "ZONATION", "Leushinskaya")
	list_vik = []
	for i in range(len(md))[vik_ind[0]:vik_ind[1]]:
		sample = md[i+1] - md[i]
		list_vik.append(sample)

for i in list_vik:
	print i

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-04-03"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""