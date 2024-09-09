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
	ds = "RCAL"
	var1 = "rt_vik_kphi_res"
	var2 = "rt_leu_kphi_res"
	var1 = db.variableLoad(well, ds, var1)
	var2 = db.variableLoad(well, ds, var2)
	db.variableDuplicate(well, ds,  "rt_vik_kphi_res", "rt_vik_kphi_res_N")
	db.variableDuplicate(well, ds,  "rt_leu_kphi_res", "rt_leu_kphi_res_N")
	var1_n = db.variableLoad(well, ds, "rt_vik_kphi_res_N")
	var2_n = db.variableLoad(well, ds, "rt_leu_kphi_res_N")
	func = lambda x: x*0
	var1_n = map(func, var1_n)
	var2_n = map(func, var2_n)
	
	for i in range(len(var1)):
		if var1[i] == "RT1":
			var1_n[i] = 1
		if var1[i] == "RT2":
			var1_n[i] = 2
		if var1[i] == "RT3":
			var1_n[i] = 3
		if var1[i] == "0":
			var1_n[i] = 0
	db.variableSave(well, ds, "rt_vik_kphi_res_N", "Petrophysical Group", "unitless", var1_n)
	
	for i in range(len(var2)):
		if var2[i] == "RT4":
			var2_n[i] = 4
		if var2[i] == "RT5":
			var2_n[i] = 5
		if var2[i] == "RT67":
			var2_n[i] = 67
		if var2[i] == "0":
			var2_n[i] = 0
	db.variableSave(well, ds, "rt_leu_kphi_res_N", "Petrophysical Group", "unitless", var2_n)

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-11-08"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""