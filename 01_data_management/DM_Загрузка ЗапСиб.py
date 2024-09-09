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
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		#db.variableCreate(well,ds,"1_PhiZS", 1)
		#db.variableCreate(well,ds,"2_PermZS", 1)
		#db.variableCreate(well,ds,"3_SwZS", 1)
		
		#db.variableRename(well,ds,"1_PhiZS","PhiZS" )
		#db.variableRename(well,ds,"2_PermZS", "PermZS")
		#db.variableRename(well,ds,"3_SwZS", "SwZS")

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-08-09"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""