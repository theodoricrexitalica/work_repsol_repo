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
import TechlogStat as ts
s = ";"
ds = "Repsol_PPeval"
for well in db.selectedWellList():
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	swt = db.variableLoad(well, ds, "SWT")
	phit = db.variableLoad(well, ds, "PHIT")
	fluid = db.variableLoad(well, ds, "Fluid_index")
	zone = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	sample_rate = md[1] - md[0]
	h = 0
	oiip = 0
	phi_avg = []
	swt_avg = []
	for i in range(len(md))[:zone[1]]:
		if fluid[i] == 1 and swt[i] != -9999.0:
			#print md[i], fluid[i], swt[i]
			h = h + sample_rate
			phi_avg.append(phit[i])
			swt_avg.append(swt[i])
			oiip = oiip + sample_rate*phit[i]*(1-swt[i])
	print well
	print "H; phi_avg; shc_avg; fiip"
	phi_avg = ts.average(phi_avg)
	swt_avg = ts.average(swt_avg)
	print round(h,2), s , round(phi_avg,3), s, round(1- swt_avg,3), s, round(oiip, 2)
		

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-09-27"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""