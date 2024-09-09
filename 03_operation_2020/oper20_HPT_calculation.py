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
cc = 0
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		flag = db.variableLoad(well, ds, "FLAG_HPAY")
		phie = db.variableLoad(well, ds, "MT_PHEXC")
		sw = db.variableLoad(well, ds, "SW")
		incr = round(md[1]-md[0], 2)
		for i in range(len(md)):
			if flag[i] == 1 and sw[i] != MissingValue and phie[i] != MissingValue:
				cc = cc + (phie[i]/100)*+(1-sw[i])*incr
				#print cc, md[i]

		print well, round(cc,0)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-06-16"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""