# -*- coding: utf-8 -*-
from __future__ import division
#Declarations
#The dictionary of parameters
#name,bname,type,family,unit,value,mode,description,group,min,max,list,enable,iscombocheckbox,isused
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
s = ";"
ds = "XRD"
print "well; mineral; average quaintity"
for well in db.wellList():
	for var in db.variableList(well, ds):
		if var != "MD" and var != "Sample":
			print well, s, var, s, ts.average(db.variableLoad(well, ds, var))

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-07-09"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""