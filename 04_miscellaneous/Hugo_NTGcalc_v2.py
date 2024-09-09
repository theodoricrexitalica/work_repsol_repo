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
	flag_rock = "ROCK_NET_FLAG"
	flag_res = "RES_NET_FLAG"
	flag_netp = "PAY_OIL_NET_FLAG"
	ds = "Repsol_PPeval"
	stat_ds = "Repsol_PPeval_PhiTSwK"
	
	md = db.variableLoad(well, ds, db.referenceName(well,ds))
	rock = db.variableLoad(well, ds, flag_rock)
	res = db.variableLoad(well, ds, flag_res)
	netp = db.variableLoad(well, ds, flag_netp)
	phit_vik = db.variableLoad(well, stat_ds, "Repsol_PPeval_PHIT_Arithmetic mean")[0]
	perm_vik = db.variableLoad(well, stat_ds, "Repsol_PPeval_PERM_COATES_Arithmetic mean")[0]
	swt_vik = db.variableLoad(well, stat_ds, "Repsol_PPeval_SWT_Arithmetic mean")[0]
	phit_leu = db.variableLoad(well, stat_ds, "Repsol_PPeval_PHIT_Arithmetic mean")[1]
	perm_leu = db.variableLoad(well, stat_ds, "Repsol_PPeval_PERM_COATES_Arithmetic mean")[1]
	swt_leu = db.variableLoad(well, stat_ds, "Repsol_PPeval_SWT_Arithmetic mean")[1]
	zone_vik = db.datasetZoneIndice(well, "Repsol_PPeval", "ZONATION", "Vikulovskaya")
	zone_leu = db.datasetZoneIndice(well, "Repsol_PPeval", "ZONATION", "Leushinskaya")
	cc_rock = 0
	cc_res = 0
	cc_netp = 0
	sample = md[101] - md[100]
	for i in range(len(md))[zone_vik[0]:zone_vik[1]]:
		if rock[i] == 1:
			cc_rock += 1
		if res[i] == 1:
			cc_res += 1
		if netp[i] == 1:
			cc_netp +=1
	print "Vikulovo"
	print round(md[zone_vik[0]],1), "-", round(md[zone_vik[1]],1)
	print "Gross, m: ", cc_rock*sample
	print "Net, m: ", round(cc_res*sample,2) 
	print "Net Pay, m: ", cc_netp*sample 
	print "NTG, %: ", int(round(((cc_res*sample) / (cc_rock*sample)*100),0))
	print "PhiT_res, %", round(phit_vik,3)*100
	print "Perm_res, mD", round(perm_vik,1)
	print "Swt_res, %", round(swt_vik,3)*100
	print
	
	

	cc_rock = 0
	cc_res = 0
	cc_netp = 0
	sample = md[101] - md[100]
	for i in range(len(md))[zone_leu[0]:zone_leu[1]]:
		if rock[i] == 1:
			cc_rock += 1
		if res[i] == 1:
			cc_res += 1
		if netp[i] == 1:
			cc_netp +=1

	print "Leushinskaya"
	print round(md[zone_leu[0]],1), "-", round(md[zone_leu[1]],1)
	print "Gross: ", cc_rock*sample, "m"
	print "Net: ", cc_res*sample , "m"
	print "Net Pay: ", cc_netp*sample, "m" 
	print "NTG: ", int(round(((cc_res*sample) / (cc_rock*sample)*100),0)), "%"
	print "PhiT_res, %", round(phit_leu,3)*100
	print "Perm_res, mD", round(perm_leu,1)
	print "Swt_res, %", round(swt_leu,3)*100

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-03-04"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""