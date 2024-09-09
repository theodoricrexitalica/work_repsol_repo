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
	print well
	ds = "Repsol_PPeval"
	phit = db.variableLoad(well, ds, "PHIT")
	perm = db.variableLoad(well, ds, "PERM_COATES")
	respay = db.variableLoad(well, ds, "RES_NET_FLAG")
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	zone = db.datasetZoneIndice(well, ds, "ZONATION", "Vikulovskaya")
	sample = md[1]-md[0]
	func = lambda x: x*0
	phith = map(func, md)
	permh = map(func, md)
	for i in range(len(md))[zone[1]:zone[0]:-1]:
		if respay[i] == 1 and phit[i] != MissingValue and perm[i] !=MissingValue :
			phith[i-1] = phith[i] + sample*phit[i]
			permh[i-1] = permh[i] + sample*perm[i]
			
		else:
			phith[i-1] = phith[i] + sample*0
			permh[i-1] = permh[i] + sample*0
	phith_max = max(phith)
	permh_max = max(permh)
	
	func_norm_phith = lambda x: x/phith_max
	func_norm_permh = lambda x: x/permh_max
	phith = map(func_norm_phith, phith)
	permh = map(func_norm_permh, permh)
	print "phith", db.variableSave(well, ds, "PHITH", "", "", phith)
	print "permh", db.variableSave(well, ds, "PERMH", "", "", permh)
	
	
	
	
	

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2019-06-14"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""