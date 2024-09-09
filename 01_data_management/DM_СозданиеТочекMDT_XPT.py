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
	print well
	ds_mdt = "MDT"
	ds_xpt = "XPT"
	if not db.variableExists(well, ds_mdt, "Points"):
		db.variableDuplicate(well, ds_mdt, db.referenceName(well, ds_mdt), "Points")
		points = db.variableLoad(well, ds_mdt, "Points")
		func = lambda x: x*0+1
		points = map(func, points)
		db.variableSave(well, ds_mdt, "Points", "Name", "unitless", points)
	else:
		print "MDT Points already exists"
		pass
	
	
	if not db.variableExists(well, ds_xpt, "Points"):
		db.variableDuplicate(well, ds_xpt, db.referenceName(well, ds_xpt), "Points")
		points = db.variableLoad(well, ds_xpt, "Points")
		func = lambda x: x*0+1
		points = map(func, points)
		db.variableSave(well, ds_xpt, "Points", "Name", "unitless", points)
	else:
		print "XPT Points already exists"
		pass
	
	print "MDT copy fluid", db.variableCopy(well, "Repsol_PPeval", "Fluid_index", ds_mdt, "Fluid_index", "automatic")
	print "XPT copy fluid", db.variableCopy(well, "Repsol_PPeval", "Fluid_index", ds_xpt, "Fluid_index", "automatic")

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-25"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""