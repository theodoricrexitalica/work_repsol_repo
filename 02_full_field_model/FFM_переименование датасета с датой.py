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
from time import gmtime, strftime
date = strftime("%d%m%y", gmtime())
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		db.datasetDuplicate(well, ds, well, ds+"_"+date)

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-06-11"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""