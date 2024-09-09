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
name1 = "ROCKTYPE_C"
#family1 = "Pore Throat Radius Distribution (Array)"
#unit1 = "um"
source1 = "Repsol_flowind_vik"
dest1 = "Elastic Properties"
#dest2 = "Repsol_flowind_leu"

for well in db.wellList():
	for ds in db.datasetList(well):
		for var in db.variableList(well, ds):
			#db.variableFamilyChange(well, ds, name1, family1)
			#db.variableUnitChange(well, ds, name1, unit1)
			db.variableCopy(well, source1, name1, dest1, name1, "anti-aliasing")
			#db.variableCopy(well, source1, name1, dest2, name1, "anti-aliasing")

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-08-14"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""