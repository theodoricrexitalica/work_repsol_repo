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
list = [7356,
7353,
7349,
7345,
7342,
7338,
7334,
7330,
7325,
7322,
7318,
7314,
7309,
7307,
7304,
7301,
7297,
7294,
7291,
7287,
7283,
7278,
7273,
7269,
7264,
7259,
7257,
7251,
7246,
7241,
7237,
7233,
7228,
7225,
7222,
7219,
7214,
7211,
7206,
7201,
7198,
7195,
7190,
7189,
7186,
7183,
7179,
7176,
7173,
7169,
7167,
7164,
7161,
7158,
7154,
7151,
7148,
7145,
7142,
7139,
7136,
7134,
7131,
7129,
7126,
7122,
7119,
7116,
7111,
7108,
7105,
7102,
7100,
7097,
7094,
7090,
7087,
7083,
7081,
7077,
7073,
7067,
7064,
7060,
7057,
7053,
7048,
7045,
7042,
7038,
7036,
7033,
7030,
7025,
7023,
7018,
7013,
7010,
7006,
7003]



#print list
for well in db.selectedWellList():
	ds = "RCAL"
	sample = db.variableLoad(well, ds, "Sample")
	md = db.variableLoad(well, ds, "MD")
	for i in range(len(md)):
		#print md[i]
		for j in range(len(list)):
			if int(sample[i]) == list[j]:
				print "results",md[i], list[j]

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-04-25"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""