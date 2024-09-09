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
for well in db.selectedWellList():
	path = "w:\\WELLS\\" + well + "\\5.EOWR\\Petrophysical evaluation\\FranBataller_PPeval"
	os.mkdir(path, 0755)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-06-29"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""