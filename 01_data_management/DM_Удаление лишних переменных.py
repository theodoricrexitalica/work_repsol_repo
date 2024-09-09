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
#list = ['MD', 'DL_PERM_COATES_Arithmetic mean', \
#'DL_PERM_COATES_Q10', 'DL_PERM_COATES_Q90', \
#'DL_PERM_COATES_Variance', 'DL_PERM_COATES_Standard Deviation', \
#'DL_PHIT_Arithmetic mean', \
#'DL_PHIT_Q10', 'DL_PHIT_Q90', \
#'DL_PHIT_Standard Deviation', 'DL_PHIT_Variance']

for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		for var in db.variableList(well, ds):
			#if "PERM" in var:
				#db.variableFamilyChange(well, ds, var, "Average Permeability")
				#db.variableUnitChange(well, ds, var, "mD")
			#if "PHIT" in var:
				#db.variableFamilyChange(well, ds, var, "Average Porosity")
				#db.variableUnitChange(well, ds, var, "v/v")
			#if "Repsol_PPeva" in var:
				##print "_".join(var.split("_")[1:])
				#db.variableRename(well, ds, var,  "LOG_"+ "_".join(var.split("_")[2:]))
			db.variableCopy(well, ds, var, "ZONES_PARA_Stat", var, "automatic")

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-04"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""