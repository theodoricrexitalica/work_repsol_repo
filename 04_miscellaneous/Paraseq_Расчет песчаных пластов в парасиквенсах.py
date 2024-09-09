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
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		sample_rate = md[101] - md[100]
		res_net = db.variableLoad(well, ds,"RES_NET_FLAG")
		zone = db.variableLoad(well, "ZONES_PARA", "Paraseq")
		hv6 = db.datasetZoneIndice(well, ds, "ZONES_PARA", zone[1])
		hv5 = db.datasetZoneIndice(well, ds, "ZONES_PARA", zone[2])
		hv4 = db.datasetZoneIndice(well, ds, "ZONES_PARA", zone[3])
		hv3 = db.datasetZoneIndice(well, ds, "ZONES_PARA", zone[4])
		hv2 = db.datasetZoneIndice(well, ds, "ZONES_PARA", zone[5])
		hv1 = db.datasetZoneIndice(well, ds, "ZONES_PARA", zone[6])
		
		cc_res = 0
		for i in res_net[hv6[0]:hv6[1]]:
			if i == 1:
				cc_res +=1
		print well
		print zone
		print "HV6"
		print cc_res*sample_rate, len(res_net[hv6[0]:hv6[1]])*sample_rate, 100*(cc_res*sample_rate)/(len(res_net[hv6[0]:hv6[1]])*sample_rate), "%"
		
		cc_res = 0
		for i in res_net[hv5[0]:hv5[1]]:
			if i == 1:
				cc_res +=1
		print "HV5"
		print cc_res*sample_rate, len(res_net[hv5[0]:hv5[1]])*sample_rate, 100*(cc_res*sample_rate)/(len(res_net[hv5[0]:hv5[1]])*sample_rate), "%"
		
		cc_res = 0
		for i in res_net[hv4[0]:hv4[1]]:
			if i == 1:
				cc_res +=1
		print "HV4"
		print cc_res*sample_rate, len(res_net[hv4[0]:hv4[1]])*sample_rate, 100*(cc_res*sample_rate)/(len(res_net[hv4[0]:hv4[1]])*sample_rate), "%"
		
		cc_res = 0
		for i in res_net[hv3[0]:hv3[1]]:
			if i == 1:
				cc_res +=1
		print "HV3"
		print cc_res*sample_rate, len(res_net[hv3[0]:hv3[1]])*sample_rate, 100*(cc_res*sample_rate)/(len(res_net[hv3[0]:hv3[1]])*sample_rate), "%"

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-02-05"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""