# -*- coding: utf-8 -*-
from __future__ import division
from math import *
from TechlogMath import *
from operator import *
import sys
if sys.version_info[0]==3:
    from six.moves import range

PI     = 3.14159265358979323846
PIO2   = 1.57079632679489661923
PIO4   = 7.85398163397448309616E-1
SQRT2  = 1.41421356237309504880
SQRTH  = 7.07106781186547524401E-1
E      = exp(1)
LN2    = log(2)
LN10   = log(10)
LOG2E  = 1.4426950408889634073599
LOG10E = 1.0 / LN10
MissingValue = -9999
def iif(condition, trueResult=MissingValue, falseResult=MissingValue):
	if condition:
		return trueResult
	else:
		return falseResult

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
#Type:Variable
#BName:rt
#Family:Petrophysical Group
#Unit:v/v
#Mode:In
#Description:Description
RT = Variable("10-R", "Slb_WLL", "RT_VK1_TiCo_pet", u"Petrophysical Group", u"v/v")
parameterDict.update({'RT' : Parameter(name='RT',bname='rt',type='Variable',family='Petrophysical Group',measurement='',unit='v/v',value='10-R.Slb_WLL.RT_VK1_TiCo_pet',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swirr
#Family:Irreducible Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
Swirr = Variable("10-R", "Slb_WLL", "SWL_pet", u"Irreducible Water Saturation", u"v/v")
parameterDict.update({'Swirr' : Parameter(name='Swirr',bname='swirr',type='Variable',family='Irreducible Water Saturation',measurement='',unit='v/v',value='10-R.Slb_WLL.SWL_pet',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:sw
#Family:Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
Sw = Variable("10-R", "Slb_WLL", "SWAT_final_pet", u"Water Saturation", u"v/v")
parameterDict.update({'Sw' : Parameter(name='Sw',bname='sw',type='Variable',family='Water Saturation',measurement='',unit='v/v',value='10-R.Slb_WLL.SWAT_final_pet',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:visc_o
#Family:Oil Viscosity
#Unit:cP
#Mode:In
#Description:Description
Visc_o = Variable("10-R", "Slb_WLL", "VISC_OP", u"Oil Viscosity", u"cP")
parameterDict.update({'Visc_o' : Parameter(name='Visc_o',bname='visc_o',type='Variable',family='Oil Viscosity',measurement='',unit='cP',value='10-R.Slb_WLL.VISC_OP',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:visc_w
#Family:Water Viscosity
#Unit:cP
#Mode:In
#Description:Description
Visc_w = Variable("10-R", "Slb_WLL", "VISC_W", u"Water Viscosity", u"cP")
parameterDict.update({'Visc_w' : Parameter(name='Visc_w',bname='visc_w',type='Variable',family='Water Viscosity',measurement='',unit='cP',value='10-R.Slb_WLL.VISC_W',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
bo_unit = u"unitless"
#Measurement:Coefficient
bo_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
bo = 1.1
parameterDict.update({'bo' : Parameter(name='bo',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='1.1',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
krwe1_unit = u"unitless"
#Measurement:Coefficient
krwe1_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
krwe1 = 0.1216
parameterDict.update({'krwe1' : Parameter(name='krwe1',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.1216',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
nw1_unit = u"unitless"
#Measurement:Coefficient
nw1_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
nw1 = 3.2
parameterDict.update({'nw1' : Parameter(name='nw1',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='3.2',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
kroe1_unit = u"unitless"
#Measurement:Coefficient
kroe1_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
kroe1 = 0.5793
parameterDict.update({'kroe1' : Parameter(name='kroe1',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.5793',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
no1_unit = u"unitless"
#Measurement:Coefficient
no1_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
no1 = 2.2
parameterDict.update({'no1' : Parameter(name='no1',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='2.2',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
krwe2_unit = u"unitless"
#Measurement:Coefficient
krwe2_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
krwe2 = 0.071
parameterDict.update({'krwe2' : Parameter(name='krwe2',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.071',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
nw2_unit = u"unitless"
#Measurement:Coefficient
nw2_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
nw2 = 3.5
parameterDict.update({'nw2' : Parameter(name='nw2',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='3.5',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
kroe2_unit = u"unitless"
#Measurement:Coefficient
kroe2_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
kroe2 = 0.405
parameterDict.update({'kroe2' : Parameter(name='kroe2',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.405',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
no2_unit = u"unitless"
#Measurement:Coefficient
no2_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
no2 = 2.3
parameterDict.update({'no2' : Parameter(name='no2',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='2.3',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
krwe3_unit = u"unitless"
#Measurement:Coefficient
krwe3_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
krwe3 = 0.0383
parameterDict.update({'krwe3' : Parameter(name='krwe3',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.0383',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
nw3_unit = u"unitless"
#Measurement:Coefficient
nw3_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
nw3 = 3.5
parameterDict.update({'nw3' : Parameter(name='nw3',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='3.5',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
kroe3_unit = u"unitless"
#Measurement:Coefficient
kroe3_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
kroe3 = 0.3309
parameterDict.update({'kroe3' : Parameter(name='kroe3',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.3309',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
no3_unit = u"unitless"
#Measurement:Coefficient
no3_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
no3 = 3.8
parameterDict.update({'no3' : Parameter(name='no3',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='3.8',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:krw
#Family:Relative Water Permeability
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
KRW = Variable("10-R", "Slb_WLL", "krw", u"Relative Water Permeability", u"v/v")
KRW.setGroupName("test")
parameterDict.update({'KRW' : Parameter(name='KRW',bname='krw',type='Variable',family='Relative Water Permeability',measurement='',unit='v/v',value='10-R.Slb_WLL.krw',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:kro
#Family:Relative Oil Permeability
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
KRO = Variable("10-R", "Slb_WLL", "kro", u"Relative Oil Permeability", u"v/v")
KRO.setGroupName("test")
parameterDict.update({'KRO' : Parameter(name='KRO',bname='kro',type='Variable',family='Relative Oil Permeability',measurement='',unit='v/v',value='10-R.Slb_WLL.kro',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:wor
#Family:Ratio
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
WOR = Variable("10-R", "Slb_WLL", "wor", u"Ratio", u"unitless")
WOR.setGroupName("test")
parameterDict.update({'WOR' : Parameter(name='WOR',bname='wor',type='Variable',family='Ratio',measurement='',unit='unitless',value='10-R.Slb_WLL.wor',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:wco
#Family:Water Cut
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
WCO = Variable("10-R", "Slb_WLL", "WCO", u"Water Cut", u"unitless")
WCO.setGroupName("test")
parameterDict.update({'WCO' : Parameter(name='WCO',bname='wco',type='Variable',family='Water Cut',measurement='Coefficient',unit='unitless',value='10-R.Slb_WLL.WCO',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-11-30"""
__version__ = """1.0"""
__pyVersion__ = """3"""
__group__ = """test"""
__suffix__ = """_test"""
__prefix__ = """"""
__applyMode__ = """2"""
__awiEngine__ = """v2"""
__layoutTemplateMode__ = """"""
__includeMissingValues__ = """True"""
__keepPreviouslyComputedValues__ = """True"""
__areInputDisplayed__ = """True"""
__useMultiWellLayout__ = """True"""
__idForHelp__ = """"""
__executionGranularity__ = """full"""
#DeclarationsEnd
### Begin Automatic Generation Loop [LOOP_MVTEST:]###
loopSize = RT.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	rt = RT.value(loopIterator)
	swirr = Swirr.value(loopIterator)
	sw = Sw.value(loopIterator)
	visc_o = Visc_o.value(loopIterator)
	visc_w = Visc_w.value(loopIterator)
	krw = MissingValue
	kro = MissingValue
	wor = MissingValue
	wco = MissingValue
	if MissingValue not in [rt, swirr, sw, visc_o, visc_w] :
		### Automatic Generation Loop End ###
		if rt == 1 and sw>=swirr:
			sw = limitValue(sw, 0, 1)
			krw = krwe1*((sw-swirr)/(1-swirr))**nw1
			kro = kroe1*((1-sw)/(1-swirr))**no1
			kro = limitValue(kro, 0.000001, 1)
			krwo = krw / kro
			wor = bo * krwo * visc_o/visc_w
			wco = wor / (1+wor)
		elif rt == 2 and sw>=swirr:
			sw = limitValue(sw, 0, 1)
			krw = krwe2*((sw-swirr)/(1-swirr))**nw2
			kro = kroe2*((1-sw)/(1-swirr))**no2
			kro = limitValue(kro, 0.000001, 1)
			krwo = krw / kro
			wor = bo * krwo * visc_o/visc_w
			wco = wor/(1+wor)
		elif rt == 3 and sw>=swirr:
			sw = limitValue(sw, 0, 1)
			krw = krwe3*((sw-swirr)/(1-swirr))**nw3
			kro = kroe3*((1-sw)/(1-swirr))**no3
			kro = limitValue(kro, 0.000001, 1)
			krwo = krw / kro
			wor = bo * krwo * visc_o/visc_w
			wco = wor/(1+wor)
	### Begin Automatic Generation EndLoop ###
	KRW.setValue(loopIterator, krw)
	KRO.setValue(loopIterator, kro)
	WOR.setValue(loopIterator, wor)
	WCO.setValue(loopIterator, wco)
KRW.save(True)
KRO.save(True)
WOR.save(True)
WCO.save(True)
### Automatic Generation EndLoop End ###
