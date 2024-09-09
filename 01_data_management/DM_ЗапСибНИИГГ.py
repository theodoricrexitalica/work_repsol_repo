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
		db.datasetTypeChange(well, ds, "continuous")
		db.variableDelete(well, ds, "Alpha PS")
		db.variableFamilyChange(well, ds, "FF", "Formation Resistivity Factor")
		db.variableTypeChange(well, ds, "FF", "Plug")
		db.variableFamilyChange(well, ds, "Fluid", "Fluid Code")
		db.variableFamilyChange(well, ds, "H", "Net")
		db.variableTypeChange(well, ds, "H","TopBottomCurve")
		db.variableFamilyChange(well, ds, "K", "Average Permeability")
		db.variableFamilyChange(well, ds, "Phi", "Average Porosity")
		db.variableFamilyChange(well, ds, "rhob_sample", "Bulk Density (Array)")
		db.variableTypeChange(well, ds, "rhob_sample","TopBottomCurve")
		db.variableFamilyChange(well, ds, "RI", "Resistivity Index (Array)")
		db.variableTypeChange(well, ds, "RI", "Plug")
		db.variableFamilyChange(well, ds, "rt_sample", "Profile Resistivity")
		db.variableTypeChange(well, ds, "rt_sample","TopBottomCurve")
		db.variableFamilyChange(well, ds, "rw", "Formation Water Resistivity")
		db.variableTypeChange(well, ds, "rw","TopBottomCurve")
		db.variableFamilyChange(well, ds, "Shc", "Hydrocarbon Saturation")
		db.variableTypeChange(well, ds, "Shc","TopBottomCurve")
		db.variableFamilyChange(well, ds, "Sw", "Water Saturation")
		db.variableTypeChange(well, ds, "Sw","TopBottomCurve")

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2018-09-04"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""