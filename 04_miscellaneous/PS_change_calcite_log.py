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

#1_Udalenie 0 v Calcite_loge
for well in db.wellList():
	for ds in db.datasetList(well):
		for var in db.selectedVariableList(well,ds):
			db.variableDescriptionChange(well,ds,var,"reservoir=0; calcite=-9999")
			
			list = db.variableLoad(well, ds, var)
			for i in range(len(list)):
				if list[i]==1:
					list[i]=-9999
			db.variableSave(well, ds, var, "","",list)
			db.variableTypeChange(well, ds, var, "TopBottomCurve")
			db.variableFamilyChange(well, ds, var, "Calcite Flag")
			db.variableUnitChange(well, ds, var, "unitless")
			
			
#2_Pereimenovanie semeist v RCAL_stat_PS		
#for well in db.wellList():
	#for ds in db.selectedDatasetList(well):
		#for i in db.variableList(well, ds):
		#for var in db.selectedVariableList(well,ds):
			#db.variableTypeChange(well, ds, var, "TopBottomCurve")
			#db.variableFamilyChange(well, ds, var, "Calcite Flag")
			#db.variableUnitChange(well, ds, var, "unitless")
			#if i!="MD" and i!="ZONE_NAME" and i!="Calicite_log":
				#db.variableFamilyChange(well, ds, i, "")
				#db.variableTypeChange(well, ds, i,"TopBottomCurve")

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2020-01-20"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""