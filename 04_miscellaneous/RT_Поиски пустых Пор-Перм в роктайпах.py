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
ds = "Rocktype_final"
for well in db.selectedWellList():
	if not db.variableExists(well, ds, "PERM_COATES"):
		print well, db.variableCopy(well, "Repsol_PPeval", "PERM_COATES", "Rocktype_final", "PERM_COATES","anti-aliasing")
	if not db.variableExists(well, ds, "PHIT"):
		print well, db.variableCopy(well, "Repsol_PPeval", "PHIT", "Rocktype_final", "PHIT","anti-aliasing")
	if not db.variableExists(well, ds, "TVDSS"):
		print well, db.variableCopy(well, "Index", "TVDSS", "Rocktype_final", "TVDSS","anti-aliasing")
		
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	phi = db.variableLoad(well, ds, "PHIT")
	perm = db.variableLoad(well, ds, "PERM_COATES")
	hafwl = db.variableLoad(well, ds, "HAFWL")
	tvdss = db.variableLoad(well, ds, "TVDSS")
	rt = db.variableLoad(well, ds, "ROCKTYPE")
	
	for i in range(len(md)):
		if phi[i] == MissingValue or perm[i] == MissingValue:
			if rt[i] != MissingValue:
				print md[i], rt[i], phi[i], perm[i]

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-08-09"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""