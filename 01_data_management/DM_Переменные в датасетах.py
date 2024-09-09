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
for well in db.wellList():
	ds1 = "Repsol_Rocktype"
	ds2 = "Repsol_flowind_vik"
	var = "ROCKTYPE"
	var_new = "ROCKTYPE_L"
	list = [ds1, ds2]
	for i in list:
		#db.variableFamilyChange(well, i, var, "Petrophysical Group")
		#db.variableUnitChange(well, i, var, "unitless")
		#db.variableTypeChange(well, i, var, "Plug")
		db.variableRename(well, i, var, var_new)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-08-10"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""