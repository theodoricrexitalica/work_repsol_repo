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
	src = "w:\\WELLS\\" + well + "\\1.DRILLING\\Logging\\1.Napralenie"
	dst = "w:\\WELLS\\" + well + "\\1.DRILLING\\Logging\\1.Napravlenie"
	os.rename(src, dst)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-06-29"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""