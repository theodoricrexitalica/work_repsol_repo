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
def zero(data):
	if data == -9999.0:
		data = ","
	else:
		data = round(data,0)
	return data

for well in db.selectedWellList():
	ds = "DST"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	bhp = db.variableLoad(well, ds, "BHP")
	perf = db.variableLoad(well, ds, "Perf")
	qgas = db.variableLoad(well, ds, "Qgas")
	for i in range(len(md)-1):
		if i%2 == 0:
			print md[i], "-", md[i+1], zero(bhp[i]), zero(qgas[i])

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-18"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""