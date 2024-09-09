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
		wlpath = db.variableLoad(well, ds, "TVDSS")
		wlpath_sag = db.variableLoad(well, "TL_WellPath_sag", "TVDSS")
		print well, "tvdss:", round(wlpath[-1],1), "tvdss_sag:", round(wlpath_sag[-1],1), "diff:", round(wlpath[-1] - wlpath_sag[-1], 1), "m"
		

__doc__ = """Выбираем датасет TL_WellPath, скорректированный датасет скрипт находит сам. Считает разницу"""
__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-07-03"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""