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
	ds = "Mudlogs"
	wh = "Wh"
	bh = "Bh"
	ch  ="Ch"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	c1 = db.variableLoad(well, ds, "C1_GZG")
	c2 = db.variableLoad(well, ds, "C2_GZG")
	c3 = db.variableLoad(well, ds, "C3_GZG")
	ic4 = db.variableLoad(well, ds, "iC4_GZG")
	ic5 = db.variableLoad(well, ds, "iC5_GZG")
	nc4 = db.variableLoad(well, ds, "nC4_GZG")
	nc5 = db.variableLoad(well, ds, "nC5_GZG")
	
#Calculation Wb, Bh, Ch
	db.variableDuplicate(well, ds, db.referenceName(well, ds), wh)
	db.variableFamilyChange(well, ds, wh, "Mud Gas Wetness")
	db.variableUnitChange(well, ds, wh, "unitless")
	db.variableTypeChange(well, ds, wh, "Plug")
	db.variableDuplicate(well, ds, db.referenceName(well, ds), bh)
	db.variableFamilyChange(well, ds, bh, "Mud Gas Balance")
	db.variableUnitChange(well, ds, bh, "unitless")
	db.variableTypeChange(well, ds, bh, "Plug")
	db.variableDuplicate(well, ds, db.referenceName(well, ds), ch)
	db.variableFamilyChange(well, ds, ch, "Oil Probability")
	db.variableUnitChange(well, ds, ch, "unitless")
	db.variableTypeChange(well, ds, ch, "Plug")
	wh =  db.variableLoad(well, ds, wh)
	bh = db.variableLoad(well, ds, bh)
	ch = db.variableLoad(well, ds, ch)
	for i in range(len(md)):
		if (c1[i] + c2[i] + c3[i] + ic4[i] + nc4[i] + ic5[i] + nc5[i]) != 0:
			wh[i] = ((c2[i] + c3[i] + ic4[i] + nc4[i] + ic5[i] + nc5[i]) / (c1[i] + c2[i] + c3[i] + ic4[i] + nc4[i] + ic5[i] + nc5[i]))*100
		else:
			wh[i] = MissingValue
		if (c3[i] + ic4[i] + nc4[i] + ic5[i] + nc5[i]) != 0:
			bh[i] = (c1[i] + c2[i] ) / (c3[i] + ic4[i] + nc4[i] + ic5[i] + nc5[i])
		else:
			bh[i] = MissingValue
		if c3[i] != 0:
			ch[i] = (ic4[i] + nc4[i] + ic5[i] + nc5[i])/c3[i]
		else:
			ch[i] = MissingValue
	print well
	print "Wh", db.variableSave(well, ds, "Wh", "Mud Gas Wetness", "unitless", wh)
	print "Bh", db.variableSave(well, ds, "Bh", "Mud Gas Balance", "unitless", bh)
	print "Ch", db.variableSave(well, ds, "Ch", "Oil Probability", "unitless", ch)

#Calculation TG_chromo
	db.variableDuplicate(well, ds, db.referenceName(well, ds), "TG_chromo")
	db.variableFamilyChange(well, ds, "TG_chromo", "Total Gas")
	db.variableUnitChange(well, ds, "TG_chromo", "%")
	tg_chromo =  db.variableLoad(well, ds, "TG_chromo")
	for i in range(len(md)):
		tg_chromo[i] = (c1[i] + c2[i] + c3[i] + ic4[i] + nc4[i] + ic5[i] + nc5[i])/10000
		if tg_chromo[i] < 0:
			tg_chromo[i] = MissingValue
	print "TG_chromo", db.variableSave(well, ds, "TG_chromo", "Total Gas", "%", tg_chromo)
	
#Calculation Ratios
	db.variableDuplicate(well, ds, db.referenceName(well, ds), "C1_C2")
	db.variableTypeChange(well, ds, "C1_C2", "Plug")
	c1_c2=  db.variableLoad(well, ds, "C1_C2")
	db.variableDuplicate(well, ds, db.referenceName(well, ds), "C1_C3")
	db.variableTypeChange(well, ds, "C1_C3", "Plug")
	c1_c3=  db.variableLoad(well, ds, "C1_C3")
	db.variableDuplicate(well, ds, db.referenceName(well, ds), "C2_C3")
	db.variableTypeChange(well, ds, "C2_C3", "Plug")
	c2_c3=  db.variableLoad(well, ds, "C2_C3")
	for i in range(len(md)):
		if c2[i] != 0:
			c1_c2[i] = c1[i]/c2[i]
		if c3[i] != 0:
			c1_c3[i] = c1[i]/c3[i]
			c2_c3[i] = c2[i]/c3[i]
	print "C1_C2", db.variableSave(well, ds, "C1_C2", " ", " ", c1_c2)
	print "C1_C3", db.variableSave(well, ds, "C1_C3", " ", " ", c1_c3)
	print "C2_C3", db.variableSave(well, ds, "C2_C3", " ", " ", c2_c3)
	

__author__ = """Taras DOLGUSHIN (se64403)"""
__date__ = """2019-10-25"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""