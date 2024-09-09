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
def rt_percent(rt,indice):
	rt1 = []
	rt2 = []
	rt3 = []
	rt_total = []
	for i in range(len(rt))[indice[0]:indice[1]]:
		rt_total.append(rt[i])
		if rt[i] == 1:
			rt1.append(rt[i])
		if rt[i] == 2:
			rt2.append(rt[i])
		if rt[i] == 3:
			rt3.append(rt[i])
	return len(rt1)/len(rt_total), len(rt2)/len(rt_total), len(rt3)/len(rt_total)


for well in db.selectedWellList():
	ds = "Repsol_PPeval"
	var = "rt_vsh_N"
	zone = "ZONES_PARA"
	rt = db.variableLoad(well, ds, var)
	vik = db.datasetZoneIndice(well, ds, zone, "Vikulovskaya")
	print well, "Vikulovskaya", rt_percent(rt,vik)
	hv6 = db.datasetZoneIndice(well, ds, zone, "HV6")
	print well, "HV6", rt_percent(rt,hv6)
	hv5 = db.datasetZoneIndice(well, ds, zone, "HV5")
	print well, "HV5", rt_percent(rt,hv5)
	hv4 = db.datasetZoneIndice(well, ds, zone, "HV4")
	print well, "HV4", rt_percent(rt,hv4)
	hv3 = db.datasetZoneIndice(well, ds, zone, "HV3")
	print well, "HV3", rt_percent(rt,hv3)
	hv2 = db.datasetZoneIndice(well, ds, zone, "HV2")
	print well, "HV2", rt_percent(rt,hv2)
	hv1 = db.datasetZoneIndice(well, ds, zone, "HV1")
	print well, "HV1", rt_percent(rt,hv1)
	
	#rt1 = []
	#rt2 = []
	#rt3 = []
	#rt_total = []
	#for i in range(len(rt))[vik[0]:vik[1]]:
		#rt_total.append(rt[i])
		#if rt[i] == 1:
			#rt1.append(rt[i])
		#if rt[i] == 2:
			#rt2.append(rt[i])
		#if rt[i] == 3:
			#rt3.append(rt[i])
#print "RT1,%", len(rt1)/len(rt_total)
#print "RT2,%", len(rt2)/len(rt_total)
#print "RT3,%", len(rt3)/len(rt_total)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-05-17"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""