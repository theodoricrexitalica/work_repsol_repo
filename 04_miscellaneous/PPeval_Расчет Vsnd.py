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
def MissValueZero(list):
	for i in range(len(list)):
		if list[i] == MissingValue:
			list[i] = 0
	return list
#elan_list = ["VQUA","VORT", "VUOI", "VUWA", "VUGA", "VXOI", "VXWA",  " VXGA", "VSAN"]
elan_list = ["VQUA","VORT", "VSAN"]
ds = "ELAN_Slb"
list = []
for well in db.selectedWellList():
	for i in range(len(elan_list)):
		#print elan_list[i]
		if db.variableExists(well, ds, elan_list[i]):
			elan_var = db.variableLoad(well, ds,  elan_list[i])
			print well, elan_list[i]
			MissValueZero(elan_var)
			list.append(elan_var)
v_sand = map(lambda x: x*0, list[0])
#print list[0]
for j in range(len(list)-1):
	for i in range(len(list[j])):
		v_sand[i] = list[j][i] + list[j+1][i] + v_sand[i]
#print v_sand
db.variableSave(well, ds, "VSND", "Sand Volume Fraction", "v/v", v_sand)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-06-28"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""