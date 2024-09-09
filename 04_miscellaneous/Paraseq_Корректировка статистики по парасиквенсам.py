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
list = ["MD", "Repsol_PPeval_PERM_COATES_Arithmetic mean", "Repsol_PPeval_PHIT_Arithmetic mean", \
			"Repsol_PPeval_VOL_SS_Arithmetic mean", "RES_NET_FLAG", "ZONE_NAME"]
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		res_flag = db.variableLoad(well, ds, "RES_NET_FLAG")
		perm = db.variableLoad(well, ds, "Repsol_PPeval_PERM_COATES_Arithmetic mean")
		phi = db.variableLoad(well, ds, "Repsol_PPeval_PHIT_Arithmetic mean")
		volss = db.variableLoad(well, ds, "Repsol_PPeval_VOL_SS_Arithmetic mean")
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		print well
		for i in range(len(md)):
			if res_flag[i] == "0":
				perm[i] = -9999
				phi[i] = -9999
				volss[i] = -9999
			else:
				phi[i] = phi[i]*100
		db.variableSave(well, ds, "Repsol_PPeval_PERM_COATES_Arithmetic mean", "Average Permeability", "mD", perm)
		db.variableSave(well, ds, "Repsol_PPeval_PHIT_Arithmetic mean", "Total Porosity", "V/V", phi)
		db.variableSave(well, ds, "Repsol_PPeval_VOL_SS_Arithmetic mean", "Net Sand Fraction", "V/V", volss)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-06-19"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""