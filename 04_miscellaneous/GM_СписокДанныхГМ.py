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
s = ";"
for well in db.selectedWellList():
	ds1 = "Elastic Properties"
	ep = db.variableList(well, ds1)
	if db.datasetExists(well, ds1):
		for i in range(len(ep)):
			print well, s, ds1, s, ep[i], s, db.variableFamily(well, ds1, ep[i]), s
	else:
		print well, s, ds1, " doesnt exist", s
		pass
	
	ds2 = "PGM_MechProp"
	pgm = db.variableList(well, ds2)
	if db.datasetExists(well, ds2):
		for i in range(len(pgm)):
			print well, s, ds2, s, pgm[i], s, db.variableFamily(well, ds2, pgm[i]), s
	else:
		print well, s, ds2, " doesnt exist", s
		pass
		
	ds3 = "Slb_MechProp"
	smp = db.variableList(well, ds3)
	if db.datasetExists(well, ds3):
		for i in range(len(smp)):
			print well, s, ds3, s, smp[i], s, db.variableFamily(well, ds3, smp[i]), s
	else:
		print well, s, ds3, " doesnt exist", s
		pass

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-03-20"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""