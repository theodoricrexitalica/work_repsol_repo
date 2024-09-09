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
import webbrowser as wb

import os
well_serv = r"W:\WELLS"
for well in db.wellList():
	path_las = well_serv +"\\" + well + r"\1.DRILLING\Logging\3.Production\Open hole\Las"
	for i in os.walk(path_las):
		for j in i[2]:
			if "Rt" in j:
				wb.open(path_las)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-06-28"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""