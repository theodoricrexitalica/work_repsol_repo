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
for well in db.selectedWellList():
	ds = "Repsol_PPeval"
	ds_zone = "ZONATION"
#Ob'yavlenit peremennyh i raschet Phit v %
	phit = db.variableLoad(well, ds, "PHIT_no_calc")
	func = lambda x: x*100
	phit = map(func, phit)
	perm= db.variableLoad(well, ds, "PERM_COATES_no_calc")
	rt_kphi = db.variableLoad(well, ds, "rt_kphi_N")
	zone = db.datasetZoneIndice(well, ds, ds_zone, "Vikulovskaya")
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
#Dublirovanie krivoy Phit dlya R35
	r35_vik = db.variableDuplicate(well, ds, "PHIT_no_calc","R35")
	r35_vik = db.variableLoad(well, ds, "R35")
	func = lambda x: x*0
	r35_vik = map(func, r35_vik)
#Blok rascheta R35_winland
	for i in range(len(md))[zone[0]:zone[1]]:
		if perm[i] != MissingValue and phit[i] != MissingValue:
			r35_vik[i] = 10**(0.732+0.588*log(perm[i])-0.864*log(phit[i]))
print well, db.variableSave(well, ds, "R35"," "," ", r35_vik)
db.variableDescriptionChange(well, ds, "R35", "Winland R35 calculation nased on log data")

#Dublirovanie krivoy Perm dlya Perm_rt
	#perm_rt = db.variableDuplicate(well, ds, "PERM_COATES_no_calc","PERM_RT_W35")
	#func = lambda x: x*0
	#perm_rt = map(func, perm)
#Blok rascheta pronizaemosti po rok-tipam
	#for i in range(len(md))[zone[0]:zone[1]]:
		#if rt_kphi[i] == 1:
			#perm_rt[i] = 10**((log(2.2)+0.864*(log(phit[i]))-0.732)/0.588)
		#if rt_kphi[i] == 2:
			#perm_rt[i] = 10**((log(1.2)+0.864*(log(phit[i]))-0.732)/0.588)
		#if rt_kphi[i] == 3:
			#perm_rt[i] = 10**((log(0.45)+0.864*(log(phit[i]))-0.732)/0.588)
	#func = lambda x: x/1000
	#perm_rt = map(func, perm_rt)
	#db.variableSave(well, ds, "PERM_RT_W35","Permeability","mD", perm_rt)
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-12-16"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""