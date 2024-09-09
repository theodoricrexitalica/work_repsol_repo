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
path = r"W:\22. X - change\Taras\Оперативные задачи\ФацииТерриМарк\Facies_ver2.xlsx"

s = ";"
print "value; well; sample"
for well in db.wellList():
	ds = "RCAL"
	var = ["MD", "Permeability Klinkenberg X", "Sample"]
	data = db.variableLoad(well, ds, var[1])
	value = 1465.3
	for i in range(len(data)):
		if round(data[i],1) == value:
			print round(data[i],1), well, db.variableLoad(well, ds, var[2])[i]

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-12-12"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""