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
list_logs = ["DEPTH","AT10", "AT90", "RHOB", "TNPH", "CGR","Calicite_log"]
for well in db.selectedWellList():
	ds = "Repsol_Input"
	ds_petrel = "Repsol_Petrel"
	ds_ppeval = "Repsol_PPeval"
	db.datasetDuplicate(well, ds, well, ds_petrel)
	for var in db.variableList(well, ds_petrel):
		if var not in list_logs:
			db.variableDelete(well, ds_petrel, var)
	db.variableCopy(well, ds_ppeval, "PHIT", ds_petrel, "PHIT", "automatic")
	db.variableCopy(well, ds_ppeval, "PERM_COATES", ds_petrel, "PERM_COATES", "automatic")
	db.variableCopy(well, ds_ppeval, "rt_vsh_N", ds_petrel, "rt_vsh_N", "automatic")
	db.variableCopy(well, ds_ppeval, "rt_kphi_N", ds_petrel, "rt_kphi_N", "automatic")
	db.variableCopy(well, ds_ppeval, "VSH", ds_petrel, "VSH", "automatic")
	
	
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-22"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""