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
	cc = 0
	
	perm =  db.variableLoad(well, ds, "Reservoir Permeability")
	for i  in perm:
		if i != MissingValue:
			cc +=1
	print well, "Reservoir Porosity", cc
	
	cc=0
	por = db.variableLoad(well, ds, "Reservoir Porosity")
	for i  in por:
		if i != MissingValue:
			cc +=1
	print well, "Reservoir Permeability", cc
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-03-20"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""