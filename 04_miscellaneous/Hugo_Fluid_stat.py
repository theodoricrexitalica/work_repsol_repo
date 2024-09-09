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
	ds = "Repsol_Fluid_stat"
	ds2 = "Repsol_FluidCont"
	phit = db.variableLoad(well, ds, "Repsol_PPeval_PHIT_Arithmetic mean")
	perm = db.variableLoad(well, ds, "Repsol_PPeval_PERM_COATES_Arithmetic mean")
	swt = db.variableLoad(well, ds, "Repsol_PPeval_SWT_Arithmetic mean")
	zone = db.variableLoad(well, ds, "ZONE_NAME")
	res_flag = db.variableLoad(well, ds, "RES_NET_FLAG")
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	tvdss_fluid = db.variableLoad(well, ds2, db.referenceName(well, ds2))
	print well
	print "Vikulovo"
	for i in range(len(md)):
		if res_flag[i] == "1" and perm[i] != MissingValue:
			if "Vik" in zone[i]:
				print zone[i], round(tvdss_fluid[i],0), "-",round(tvdss_fluid[i+1],0)
				print zone[i], "Phit", round(phit[i]*100,1)
				print zone[i], "Perm", round(perm[i],1)
				print zone[i], "Sw", round(swt[i]*100,0)
				print ""
	print well
	print "Leushinskay"
	for i in range(len(md)):
		if res_flag[i] == "1" and perm[i] != MissingValue:
			if "Leu" in zone[i]:
				print zone[i], round(tvdss_fluid[i],0), "-",round(tvdss_fluid[i+1],0)
				print zone[i], "Phit", round(phit[i]*100,1)
				print zone[i], "Perm", round(perm[i],1)
				print zone[i], "Sw", round(swt[i]*100,0)
				print ""

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-06-21"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""