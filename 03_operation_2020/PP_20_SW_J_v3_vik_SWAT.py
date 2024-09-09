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
#BName:permx
#Family:Permeability
#Unit:mD
#Mode:In
#Description:Description
PermX = Variable("11-R", "Slb_WLL", "PermX", u"Permeability", u"mD")
parameterDict.update({'PermX' : Parameter(name='PermX',bname='permx',type='Variable',family='Permeability',measurement='',unit='mD',value='11-R.Slb_WLL.PermX',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:kphit
#Family:Flow Zone Indicator
#Unit:unitless
#Mode:In
#Description:Description
KPHIT = Variable("11-R", "Slb_WLL", "KPhiT", u"Flow Zone Indicator", u"unitless")
parameterDict.update({'KPHIT' : Parameter(name='KPHIT',bname='kphit',type='Variable',family='Flow Zone Indicator',measurement='',unit='unitless',value='11-R.Slb_WLL.KPhiT',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:rt_vk1
#Family:Petrophysical Group
#Unit:unitless
#Mode:In
#Description:Description
RT_VK1 = Variable("11-R", "Slb_WLL", "RT_A1", u"Petrophysical Group", u"unitless")
parameterDict.update({'RT_VK1' : Parameter(name='RT_VK1',bname='rt_vk1',type='Variable',family='Petrophysical Group',measurement='',unit='unitless',value='11-R.Slb_WLL.RT_A1',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:tvdss
#Family:True Vertical Depth Sub Sea
#Unit:m
#Mode:In
#Description:Description
TVDSS = Variable("11-R", "Slb_WLL", "TVDSS", u"True Vertical Depth Sub Sea", u"m")
parameterDict.update({'TVDSS' : Parameter(name='TVDSS',bname='tvdss',type='Variable',family='True Vertical Depth Sub Sea',measurement='',unit='m',value='11-R.Slb_WLL.TVDSS',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
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
#BName:swat
#Family:Water Saturation
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
SWAT = Variable("11-R", "Slb_WLL", "SWAT", u"Water Saturation", u"v/v")
parameterDict.update({'SWAT' : Parameter(name='SWAT',bname='swat',type='Variable',family='Water Saturation',measurement='',unit='v/v',value='11-R.Slb_WLL.SWAT',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:sowcr
#Family:Irreducible Oil Saturation
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
Sowcr = Variable("11-R", "Slb_WLL", "SOWCR", u"Irreducible Oil Saturation", u"v/v")
parameterDict.update({'Sowcr' : Parameter(name='Sowcr',bname='sowcr',type='Variable',family='Irreducible Oil Saturation',measurement='',unit='v/v',value='11-R.Slb_WLL.SOWCR',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swl
#Family:Irreducible Water Saturation
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
SWL = Variable("11-R", "Slb_WLL", "SWL", u"Irreducible Water Saturation", u"v/v")
parameterDict.update({'SWL' : Parameter(name='SWL',bname='swl',type='Variable',family='Irreducible Water Saturation',measurement='',unit='v/v',value='11-R.Slb_WLL.SWL',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swat_final
#Family:Water Saturation
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
SWAT_final = Variable("11-R", "Slb_WLL", "SWAT_final", u"Water Saturation", u"v/v")
parameterDict.update({'SWAT_final' : Parameter(name='SWAT_final',bname='swat_final',type='Variable',family='Water Saturation',measurement='',unit='v/v',value='11-R.Slb_WLL.SWAT_final',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
loopSize = PermX.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	permx = PermX.value(loopIterator)
	kphit = KPHIT.value(loopIterator)
	rt_vk1 = RT_VK1.value(loopIterator)
	tvdss = TVDSS.value(loopIterator)
	swat = MissingValue
	sowcr = MissingValue
	swl = MissingValue
	swat_final = MissingValue
	if MissingValue not in [permx, kphit, rt_vk1, tvdss] :
		### Automatic Generation Loop End ###
	
		if FWL-tvdss > 0:
			if rt_vk1 == 1:
				min_sw=0.2553
				swl = 1.039*(sqrt(kphit))**(-0.445)
				swat = ((3.183*(FWL-tvdss)*(rho_w-rho_o)*0.098*sqrt(kphit))/(0.0704*y_cos_theta))**(1/-3.9827)
				swat_final = 1 - (1-swl)/(1-min_sw)*(1-swat)
				sowcr = 1 - swl - (0.0779*log(permx) + 0.3891)*(1-swl)
			elif rt_vk1 == 2:
				min_sw=0.4230
				swl = 1.039*(sqrt(kphit))**(-0.445)
				swat = ((3.183*(FWL-tvdss)*(rho_w-rho_o)*0.098*sqrt(kphit))/(0.126*y_cos_theta))**(1/-4.628)
				swat_final = 1 - (1-swl)/(1-min_sw)*(1-swat)
				sowcr = 1 - swl - (0.0779*log(permx) + 0.3891)*(1-swl)
			elif rt_vk1 == 3:
				min_sw=0.6271
				swl = 1.039*(sqrt(kphit))**(-0.445)
				swat = ((3.183*(FWL-tvdss)*(rho_w-rho_o)*0.098*sqrt(kphit))/(0.1147*y_cos_theta))**(1/-6.758)
				swat_final = 1 - (1-swl)/(1-min_sw)*(1-swat)
				sowcr = 1 - swl - (0.0779*log(permx) + 0.3891)*(1-swl)
	### Begin Automatic Generation EndLoop ###
	SWAT.setValue(loopIterator, swat)
	Sowcr.setValue(loopIterator, sowcr)
	SWL.setValue(loopIterator, swl)
	SWAT_final.setValue(loopIterator, swat_final)
SWAT.save(True)
Sowcr.save(True)
SWL.save(True)
SWAT_final.save(True)
### Automatic Generation EndLoop End ###
