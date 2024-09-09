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
#выбери переменную FLAG_HPAY и запускай скрипт
for well in db.wellList():
	for ds in db.datasetList(well):
		for var in db.selectedVariableList(well, ds):
			md = db.variableLoad(well, ds, db.referenceName(well,ds))
			flag = db.variableLoad(well, ds, var)
			for i in range(len(md)):
				if flag[i] == 1 and flag[i-1] != 1:
					print well, var, "top", round(md[i],0)
				if flag[i] == 1 and flag[i+1] != 1:
					print well, var, "bot", round(md[i],0)
		

__doc__ = """Выбирает переменную FLAG_HPAY и запускаме скрипт.
Скрипт находит 1й и последний индексы, отличную от нуля, и выдает их как топ и бот интервала с индексом 1"""
__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-06-15"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""