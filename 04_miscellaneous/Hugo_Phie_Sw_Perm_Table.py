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

print "Well; Oilzone; Netpay;Phie avg; Perm avg; Swt avg; Zone"
for well in db.selectedWellList():
	ds = "Repsol_PPeval_PhieSwt"
	s = ";"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	np_flag = db.variableLoad(well, ds, "PAY_OIL_NET_FLAG")
	perm_amean = db.variableLoad(well, ds, "Repsol_PPeval_PERM_COATES_Arithmetic mean")
	phie_amean = db.variableLoad(well, ds, "Repsol_PPeval_PHIE_Arithmetic mean")
	swt_amean = db.variableLoad(well, ds, "Repsol_PPeval_SWT_Arithmetic mean")
	zones = db.variableLoad(well, ds, "ZONE_NAME")
	zone_vik = db.datasetZoneIndice(well, "Repsol_PPeval", "ZONATION", "Vikulovskaya")
	net_pay_vik = 0
	for i in set(db.variableLoad(well, "Repsol_PPeval", "PAY_OIL_THICKNESS")[zone_vik[0]:zone_vik[1]]):
		if i > 0:
			net_pay_vik +=i
	zone_leu = db.datasetZoneIndice(well, "Repsol_PPeval", "ZONATION", "Leushinskaya")
	net_pay_leu = 0
	for i in set(db.variableLoad(well, "Repsol_PPeval", "PAY_OIL_THICKNESS")[zone_leu[0]:zone_leu[1]]):
		if i > 0:
			net_pay_leu +=i
	
	
	for i in range(len(np_flag)):
		#print np_flag[i]
		if np_flag[i] == "1" and zones[i] == "Vikulovskaya":
			print well, s, round(md[i],1), "-", round(md[i+1],1), s, round(net_pay_vik,1), \
			s, round(phie_amean[i]*100,1), s, round(perm_amean[i],1), s, round(swt_amean[i]*100,1), s, zones[i]
	
	for i in range(len(np_flag)):
		if np_flag[i] == "1" and zones[i] == "Leushinskaya":
			print well, s, round(md[i],1), "-", round(md[i+1],1), s, round(net_pay_leu,1), \
			s, round(phie_amean[i]*100,1), s, round(perm_amean[i],1), s, round(swt_amean[i]*100,1), s, zones[i]

	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-28"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""