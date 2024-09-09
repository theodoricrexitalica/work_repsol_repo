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
ds = "RCAL"
var = "Permeability Klinkenberg"
print "Well MD Sample Perm_X Perm_Y Perm_Z rt_vik rt_leu"
for well in db.selectedWellList():
	perm_x = db.variableLoad(well, ds, var + " X")
	perm_y = db.variableLoad(well, ds, var + " Y")
	perm_z = db.variableLoad(well, ds, var + " Z")
	sample = db.variableLoad(well, ds, "Sample")
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	rt_vik = db.variableLoad(well, ds, "rt_vik_kphi_res")
	rt_leu = db.variableLoad(well, ds, "rt_leu_kphi_res")
	
	for i in range(len(md)):
		print well, md[i], sample[i], perm_x[i], perm_y[i], perm_z[i], rt_vik[i], rt_leu[i]

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-10-24"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""