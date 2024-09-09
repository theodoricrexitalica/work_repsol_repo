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

print "well avg perc90 median"
for well in db.selectedWellList():
	#ds = "Facies_Mark_sft"
	#var = "Facies"
	ds = "ISA 1 cm SHIFT"
	var = "ISA1cmsh"
	data = db.variableLoad(well, ds, var)
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	list = []
	for i in range(len(data))[:-1]:
		#print round(md[i+1],2), round(md[i],2), round((md[i+1] - md[i]),2)
		list.append(round((md[i+1] - md[i]),2))
	print well, ts.average(list), ts.percentile(list,90), ts.median(list)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-12-13"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""