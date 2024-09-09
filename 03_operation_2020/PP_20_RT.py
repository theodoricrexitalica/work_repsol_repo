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
#BName:k
#Family:Permeability
#Unit:mD
#Mode:In
#Description:Description
K = Variable("G-3", "Slb_WLL", "", u"Permeability", u"mD")
parameterDict.update({'K' : Parameter(name='K',bname='k',type='Variable',family='Permeability',measurement='',unit='mD',value='G-3.Slb_WLL.',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:phit
#Family:Total Porosity
#Unit:v/v
#Mode:In
#Description:Description
PhiT = Variable("G-3", "Slb_WLL", "", u"Total Porosity", u"v/v")
parameterDict.update({'PhiT' : Parameter(name='PhiT',bname='phit',type='Variable',family='Total Porosity',measurement='',unit='v/v',value='G-3.Slb_WLL.',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:kphit
#Family:Flow Zone Indicator
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
KPhiT = Variable("G-3", "Slb_WLL", "KPhiT", u"Flow Zone Indicator", u"unitless")
parameterDict.update({'KPhiT' : Parameter(name='KPhiT',bname='kphit',type='Variable',family='Flow Zone Indicator',measurement='',unit='unitless',value='G-3.Slb_WLL.KPhiT',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:sqrt_kphit
#Family:Flow Zone Indicator
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
sqrtKPhiT = Variable("G-3", "Slb_WLL", "sqrtKPhiT", u"Flow Zone Indicator", u"unitless")
parameterDict.update({'sqrtKPhiT' : Parameter(name='sqrtKPhiT',bname='sqrt_kphit',type='Variable',family='Flow Zone Indicator',measurement='',unit='unitless',value='G-3.Slb_WLL.sqrtKPhiT',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:rt
#Family:Petrophysical Group
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
RT = Variable("G-3", "Slb_WLL", "RT", u"Petrophysical Group", u"unitless")
parameterDict.update({'RT' : Parameter(name='RT',bname='rt',type='Variable',family='Petrophysical Group',measurement='',unit='unitless',value='G-3.Slb_WLL.RT',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
rt1_unit = u"unitless"
#Measurement:Coefficient
rt1_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
rt1 = 71
parameterDict.update({'rt1' : Parameter(name='rt1',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='71',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
rt2_unit = u"unitless"
#Measurement:Coefficient
rt2_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
rt2 = 15
parameterDict.update({'rt2' : Parameter(name='rt2',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='15',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
rt3_unit = u"unitless"
#Measurement:Coefficient
rt3_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
rt3 = 0
parameterDict.update({'rt3' : Parameter(name='rt3',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='0',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
### Begin Automatic Generation Loop [LOOP_MVTEST:]###
loopSize = K.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	k = K.value(loopIterator)
	phit = PhiT.value(loopIterator)
	kphit = MissingValue
	sqrt_kphit = MissingValue
	rt = MissingValue
	if MissingValue not in [k, phit] :
		### Automatic Generation Loop End ###
		kphit = k/phit
		sqrt_kphit = sqrt(kphit)
		if kphit >= rt1:
			rt = 1
		elif rt2 <= kphit < rt1:
			rt = 2
		elif kphit < rt2:
			rt = 3
		
	### Begin Automatic Generation EndLoop ###
	KPhiT.setValue(loopIterator, kphit)
	sqrtKPhiT.setValue(loopIterator, sqrt_kphit)
	RT.setValue(loopIterator, rt)
KPhiT.save(True)
sqrtKPhiT.save(True)
RT.save(True)
### Automatic Generation EndLoop End ###
