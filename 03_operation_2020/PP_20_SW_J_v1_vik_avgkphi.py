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
#BName:kphit
#Family:
#Unit:unitless
#Mode:In
#Description:Description
KPHIT = Variable("well", "dataset", "", u"", u"unitless")
parameterDict.update({'KPHIT' : Parameter(name='KPHIT',bname='kphit',type='Variable',family='',measurement='',unit='unitless',value='G-3..KPhiT',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:rt_a1
#Family:
#Unit:unitless
#Mode:In
#Description:Description
RT_A1 = Variable("well", "dataset", "", u"", u"unitless")
parameterDict.update({'RT_A1' : Parameter(name='RT_A1',bname='rt_a1',type='Variable',family='',measurement='',unit='unitless',value='G-3..RT_A1',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:tvdss
#Family:True Vertical Depth Sub Sea
#Unit:m
#Mode:In
#Description:Description
TVDSS = Variable("well", "dataset", "", u"True Vertical Depth Sub Sea", u"m")
parameterDict.update({'TVDSS' : Parameter(name='TVDSS',bname='tvdss',type='Variable',family='True Vertical Depth Sub Sea',measurement='',unit='m',value='G-3..TVDSS',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swir
#Family:Irreducible Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
SWIR = Variable("well", "dataset", "", u"Irreducible Water Saturation", u"v/v")
parameterDict.update({'SWIR' : Parameter(name='SWIR',bname='swir',type='Variable',family='Irreducible Water Saturation',measurement='',unit='v/v',value='G-3..SWIR',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:m
FWL_unit = u"m"
#Measurement:Depth
FWL_measurement = u"Depth"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
FWL = 920
parameterDict.update({'FWL' : Parameter(name='FWL',bname='',type='Number',family='',measurement='Depth',unit='m',value='920',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
y_cos_theta_unit = u"unitless"
#Measurement:Coefficient
y_cos_theta_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
y_cos_theta = 13
parameterDict.update({'y_cos_theta' : Parameter(name='y_cos_theta',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='13',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cm3
rho_o_unit = u"g/cm3"
#Measurement:Density
rho_o_measurement = u"Density"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
rho_o = 0.777
parameterDict.update({'rho_o' : Parameter(name='rho_o',bname='',type='Number',family='',measurement='Density',unit='g/cm3',value='0.777',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:g/cm3
rho_w_unit = u"g/cm3"
#Measurement:Density
rho_w_measurement = u"Density"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
rho_w = 1.0116
parameterDict.update({'rho_w' : Parameter(name='rho_w',bname='',type='Number',family='',measurement='Density',unit='g/cm3',value='1.0116',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:H
#Family:Height Above Free Water Level
#Unit:m
#Mode:Out
#Description:Description
#Format:auto
HAFWL = Variable("well", "dataset", "", u"Height Above Free Water Level", u"m")
parameterDict.update({'HAFWL' : Parameter(name='HAFWL',bname='H',type='Variable',family='Height Above Free Water Level',measurement='',unit='m',value='G-3..HAFWL',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swnj
#Family:Water Saturation
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
SWN_J = Variable("well", "dataset", "", u"Water Saturation", u"v/v")
parameterDict.update({'SWN_J' : Parameter(name='SWN_J',bname='swnj',type='Variable',family='Water Saturation',measurement='',unit='v/v',value='G-3..SWN_J',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swj
#Family:Water Saturation
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
SW_J = Variable("well", "dataset", "", u"Water Saturation", u"v/v")
parameterDict.update({'SW_J' : Parameter(name='SW_J',bname='swj',type='Variable',family='Water Saturation',measurement='',unit='v/v',value='G-3..SW_J',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-11-30"""
__version__ = """1.0"""
__pyVersion__ = """3"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__applyMode__ = """0"""
__awiEngine__ = """v2"""
__layoutTemplateMode__ = """"""
__includeMissingValues__ = """True"""
__keepPreviouslyComputedValues__ = """True"""
__areInputDisplayed__ = """True"""
__useMultiWellLayout__ = """True"""
__idForHelp__ = """"""
__executionGranularity__ = """full"""
#DeclarationsEnd
def hafwl(FWL, tvdss):
	return FWL-tvdss
	if FWL-tvdss < 0:
		return -9999

### Begin Automatic Generation Loop [LOOP_MVTEST:]###
loopSize = KPHIT.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	kphit = KPHIT.value(loopIterator)
	rt_a1 = RT_A1.value(loopIterator)
	tvdss = TVDSS.value(loopIterator)
	swir = SWIR.value(loopIterator)
	H = MissingValue
	swnj = MissingValue
	swj = MissingValue
	if MissingValue not in [kphit, rt_a1, tvdss, swir] :
		### Automatic Generation Loop End ###
		if FWL-tvdss > 0:
			if rt_a1 == 1:
				#swnj=10
				swnj = ((3.183*(FWL-tvdss)*(rho_w-rho_o)*0.098*sqrt(kphit))/(0.0704*y_cos_theta))**(1/-3.9827)
			elif rt_a1 == 2:
				#swnj=20
				swnj = ((3.183*(FWL-tvdss)*(rho_w-rho_o)*0.098*sqrt(kphit))/(0.126*y_cos_theta))**(1/-4.628)
			elif rt_a1 == 3:
				#swnj=30
				swnj = ((3.183*(FWL-tvdss)*(rho_w-rho_o)*0.098*sqrt(kphit))/(0.1147*y_cos_theta))**(1/-6.758)
			swj = (1-swir)*swnj + swir
	### Begin Automatic Generation EndLoop ###
	HAFWL.setValue(loopIterator, H)
	SWN_J.setValue(loopIterator, swnj)
	SW_J.setValue(loopIterator, swj)
HAFWL.save(True)
SWN_J.save(True)
SW_J.save(True)
### Automatic Generation EndLoop End ###
