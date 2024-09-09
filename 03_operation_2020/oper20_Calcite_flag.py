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
print "Well; MD m; TVDSS m"
s = ";"
for well in db.wellList():
	for ds in db.datasetList(well):
		for var in db.selectedVariableList(well,ds):
			md = db.variableLoad(well, ds, db.referenceName(well,ds))
			tvdss = db.variableLoad(well, ds, "TVDSS")
			flag = db.variableLoad(well, ds, var)
			for i in range(len(flag)):
				if flag[i] == 1 and flag[i-1] != 1:
					print well, s, round(md[i],0), s, round(tvdss[i],0)
				if flag[i] == 1 and flag[i+1] != 1:
					print well, s, round(md[i],0), s, round(tvdss[i],0)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-06-13"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""