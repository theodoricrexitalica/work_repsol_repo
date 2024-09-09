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
#BName:perm
#Family:Permeability
#Unit:mD
#Mode:In
#Description:Description
Perm = Variable("11-R", "Slb_WLL", "PERM_TiCo_res_pet_leu", u"Permeability", u"mD")
parameterDict.update({'Perm' : Parameter(name='Perm',bname='perm',type='Variable',family='Permeability',measurement='',unit='mD',value='11-R.Slb_WLL.PERM_TiCo_res_pet_leu',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:rt
#Family:Petrophysical Group
#Unit:v/v
#Mode:In
#Description:Description
RT = Variable("11-R", "Slb_WLL", "RT_pet_leu", u"Petrophysical Group", u"v/v")
parameterDict.update({'RT' : Parameter(name='RT',bname='rt',type='Variable',family='Petrophysical Group',measurement='',unit='v/v',value='11-R.Slb_WLL.RT_pet_leu',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:soirr
#Family:Irreducible Oil Saturation
#Unit:v/v
#Mode:In
#Description:Description
Soirr = Variable("11-R", "Slb_WLL", "SOWCR_pet_leu_v5", u"Irreducible Oil Saturation", u"v/v")
parameterDict.update({'Soirr' : Parameter(name='Soirr',bname='soirr',type='Variable',family='Irreducible Oil Saturation',measurement='',unit='v/v',value='11-R.Slb_WLL.SOWCR_pet_leu_v5',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swirr
#Family:Irreducible Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
Swirr = Variable("11-R", "Slb_WLL", "SWL_pet_leu_v5", u"Irreducible Water Saturation", u"v/v")
parameterDict.update({'Swirr' : Parameter(name='Swirr',bname='swirr',type='Variable',family='Irreducible Water Saturation',measurement='',unit='v/v',value='11-R.Slb_WLL.SWL_pet_leu_v5',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:sw
#Family:Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
Sw = Variable("11-R", "Slb_WLL", "SWAT", u"Water Saturation", u"v/v")
parameterDict.update({'Sw' : Parameter(name='Sw',bname='sw',type='Variable',family='Water Saturation',measurement='',unit='v/v',value='11-R.Slb_WLL.SWAT',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:visc_o
#Family:Oil Viscosity
#Unit:cP
#Mode:In
#Description:Description
Visc_o = Variable("11-R", "Slb_WLL", "VISC_OP", u"Oil Viscosity", u"cP")
parameterDict.update({'Visc_o' : Parameter(name='Visc_o',bname='visc_o',type='Variable',family='Oil Viscosity',measurement='',unit='cP',value='11-R.Slb_WLL.VISC_OP',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:visc_w
#Family:Water Viscosity
#Unit:cP
#Mode:In
#Description:Description
Visc_w = Variable("11-R", "Slb_WLL", "VISC_W", u"Water Viscosity", u"cP")
parameterDict.update({'Visc_w' : Parameter(name='Visc_w',bname='visc_w',type='Variable',family='Water Viscosity',measurement='',unit='cP',value='11-R.Slb_WLL.VISC_W',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
sw_corr_unit = u"unitless"
#Measurement:Coefficient
sw_corr_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
sw_corr = 0
parameterDict.update({'sw_corr' : Parameter(name='sw_corr',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
swirr_corr_unit = u"unitless"
#Measurement:Coefficient
swirr_corr_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
swirr_corr = 0
parameterDict.update({'swirr_corr' : Parameter(name='swirr_corr',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
krwe1 = 0.1209
parameterDict.update({'krwe1' : Parameter(name='krwe1',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.1209',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
nw1 = 4
parameterDict.update({'nw1' : Parameter(name='nw1',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='4',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
kroe1 = 0.5719
parameterDict.update({'kroe1' : Parameter(name='kroe1',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.5719',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
no1 = 2.3
parameterDict.update({'no1' : Parameter(name='no1',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='2.3',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
krwe2 = 0.1031
parameterDict.update({'krwe2' : Parameter(name='krwe2',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.1031',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
nw2 = 3.8
parameterDict.update({'nw2' : Parameter(name='nw2',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='3.8',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
kroe2 = 0.4975
parameterDict.update({'kroe2' : Parameter(name='kroe2',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.4975',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
no2 = 3
parameterDict.update({'no2' : Parameter(name='no2',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='3',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
krwe3 = 0.0235
parameterDict.update({'krwe3' : Parameter(name='krwe3',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.0235',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
nw3 = 4
parameterDict.update({'nw3' : Parameter(name='nw3',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='4',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
kroe3 = 0.1455
parameterDict.update({'kroe3' : Parameter(name='kroe3',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0.1455',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
no3 = 3.5
parameterDict.update({'no3' : Parameter(name='no3',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='3.5',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:krw
#Family:Relative Water Permeability
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
KRW = Variable("11-R", "Slb_WLL", "krw", u"Relative Water Permeability", u"v/v")
KRW.setGroupName("test")
parameterDict.update({'KRW' : Parameter(name='KRW',bname='krw',type='Variable',family='Relative Water Permeability',measurement='',unit='v/v',value='11-R.Slb_WLL.krw',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:kro
#Family:Relative Oil Permeability
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
KRO = Variable("11-R", "Slb_WLL", "kro", u"Relative Oil Permeability", u"v/v")
KRO.setGroupName("test")
parameterDict.update({'KRO' : Parameter(name='KRO',bname='kro',type='Variable',family='Relative Oil Permeability',measurement='',unit='v/v',value='11-R.Slb_WLL.kro',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:wor
#Family:Ratio
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
WOR = Variable("11-R", "Slb_WLL", "wor", u"Ratio", u"unitless")
WOR.setGroupName("test")
parameterDict.update({'WOR' : Parameter(name='WOR',bname='wor',type='Variable',family='Ratio',measurement='',unit='unitless',value='11-R.Slb_WLL.wor',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:wco
#Family:Water Cut
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
WCO = Variable("11-R", "Slb_WLL", "WCO", u"Water Cut", u"unitless")
WCO.setGroupName("test")
parameterDict.update({'WCO' : Parameter(name='WCO',bname='wco',type='Variable',family='Water Cut',measurement='Coefficient',unit='unitless',value='11-R.Slb_WLL.WCO',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
loopSize = Perm.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	perm = Perm.value(loopIterator)
	rt = RT.value(loopIterator)
	soirr = Soirr.value(loopIterator)
	swirr = Swirr.value(loopIterator)
	sw = Sw.value(loopIterator)
	visc_o = Visc_o.value(loopIterator)
	visc_w = Visc_w.value(loopIterator)
	krw = MissingValue
	kro = MissingValue
	wor = MissingValue
	wco = MissingValue
	if MissingValue not in [perm, rt, soirr, swirr, sw, visc_o, visc_w] :
		### Automatic Generation Loop End ###
		if rt == 1 and sw>=swirr:
			sw = sw - sw_corr
			swirr = swirr - swirr_corr
			swirr = limitValue(swirr, 0, 1)
			sw = limitValue(sw, 0, 1)
			krw = krwe1*((sw-swirr)/(1-swirr-soirr))**nw1
			krw =  limitValue(krw, 0.000001, 1)
			kro = kroe1*((1-sw-soirr)/(1-swirr-soirr))**no1
			kro = limitValue(kro, 0.000001, 1)
			kw = krw*perm
			ko = kro*perm
			wco = (kw/visc_w)*(1/((ko/visc_o)+(kw/visc_w)))
			if kro == 0.000001 or kro == MissingValue:
				wco = 1
		elif rt == 2 and sw>=swirr:
			sw = sw - sw_corr
			swirr = swirr - swirr_corr
			swirr = limitValue(swirr, 0, 1)
			sw = limitValue(sw, 0, 1)
			krw = krwe2*((sw-swirr)/(1-swirr-soirr))**nw2
			krw =  limitValue(krw, 0.000001, 1)
			kro = kroe2*((1-sw-soirr)/(1-swirr-soirr))**no2
			kro = limitValue(kro, 0.000001, 1)
			kw = krw*perm
			ko = kro*perm
			wco = (kw/visc_w)*(1/((ko/visc_o)+(kw/visc_w)))
			if kro == 0.000001 or kro == MissingValue:
				wco = 1
		elif rt == 3 and sw>=swirr:
			sw = sw - sw_corr
			swirr = swirr - swirr_corr
			swirr = limitValue(swirr, 0, 1)
			sw = limitValue(sw, 0, 1)
			krw = krwe3*((sw-swirr)/(1-swirr-soirr))**nw3
			krw =  limitValue(krw, 0.000001, 1)
			kro = kroe3*((1-sw-soirr)/(1-swirr-soirr))**no3
			kro = limitValue(kro, 0.000001, 1)
			kw = krw*perm
			ko = kro*perm
			wco = (kw/visc_w)*(1/((ko/visc_o)+(kw/visc_w)))
			if kro == 0.000001 or kro == MissingValue:
				wco = 1
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
