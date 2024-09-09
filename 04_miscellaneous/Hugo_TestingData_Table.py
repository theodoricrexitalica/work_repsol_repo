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
	ds = "DST"
	s = ";"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	qoil = db.variableLoad(well, ds, "Qoil")
	qwat = db.variableLoad(well, ds, "Qwater")
	wc = db.variableLoad(well, ds, "WC")
	bhp = db.variableLoad(well, ds, "BHP")
	zones = db.variableLoad(well, ds, "Zones")
	print "Well;Perf;H,m; Qoil; Qwat;WC; BHP; Zone"
	#print "Perf;H,m; Qoil,bbl/d; Qwat,bbl/d;WC,%; BHP,psi;Zone"
	for i in range(len(qoil)):
		if qoil[i] != MissingValue:
			print well, s, md[i], "-", md[i+1], s, round(md[i+1] - md[i],0), " m", s, round(qoil[i],1), " m3/d", s, round(qwat[i],1), " m3/d",s, round(wc[i],0), " %", s, round(bhp[i],0), " atm", s, zones[i]

	ds = "DST_imperial"
	s = ";"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	qoil = db.variableLoad(well, ds, "Qoil")
	qwat = db.variableLoad(well, ds, "Qwater")
	wc = db.variableLoad(well, ds, "WC")
	bhp = db.variableLoad(well, ds, "BHP")
	
	for i in range(len(qoil)):
		if qoil[i] != MissingValue:
			print well, s, md[i], "-", md[i+1], s, round(md[i+1] - md[i],0), " m", s, round(qoil[i],1), " bbl/d", s, round(qwat[i],1), " bbl/d",s, round(wc[i],0), " %", s, round(bhp[i],0), " psi", s, zones[i]

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-28"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""