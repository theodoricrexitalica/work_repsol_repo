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
ds = "Slb_ELAN"
s = ";"
print "well; var; family; description"
for well in db.wellList():
	for var in db.variableList(well, ds):
		if "V" in var:
			print well, s, var, s, db.variableFamily(well, ds, var), s, db.variableDescription(well, ds, var)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-07-09"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""