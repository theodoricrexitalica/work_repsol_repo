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
ds = "ZapSibNIIGG_swpc_leu"

for well in db.selectedWellList():
	db.currentChange("import")
	for importWell in db.wellList():
		db.wellRename(importWell,well)
		for importDs in db.datasetList(well):
			db.datasetRename(well,importDs,ds)
			db.datasetCopy(well,ds,"import","project")
		db.currentChange("project")
		db.importBufferClose()

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-09-25"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""