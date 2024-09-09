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
#Paraseq_arith_Perm
for well in db.selectedWellList():
	ds = "ZONES_PARA_Stat"
	var_perm = "LOG_PERM_COATES_Arithmetic mean"
	var_zone = "ZONE_NAME"
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-05-17"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""