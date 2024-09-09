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
#BName:soir
#Family:Irreducible Oil Saturation
#Unit:v/v
#Mode:In
#Description:
SOIR = Variable("well", "dataset", "", u"Irreducible Oil Saturation", u"v/v")
parameterDict.update({'SOIR' : Parameter(name='SOIR',bname='soir',type='Variable',family='Irreducible Oil Saturation',measurement='',unit='v/v',value='11R-K03_pilot..',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swir
#Family:Irreducible Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
SWIR = Variable("well", "dataset", "", u"Irreducible Water Saturation", u"v/v")
parameterDict.update({'SWIR' : Parameter(name='SWIR',bname='swir',type='Variable',family='Irreducible Water Saturation',measurement='',unit='v/v',value='11R-K03_pilot..',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:sw
#Family:Water Saturation
#Unit:v/v
#Mode:In
#Description:
SW = Variable("well", "dataset", "", u"Water Saturation", u"v/v")
parameterDict.update({'SW' : Parameter(name='SW',bname='sw',type='Variable',family='Water Saturation',measurement='',unit='v/v',value='11R-K03_pilot..',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swm
#Family:Water Fraction
#Unit:v/v
#Mode:Out
#Description:
#Format:auto
SWM = Variable("well", "dataset", "", u"Water Fraction", u"v/v")
parameterDict.update({'SWM' : Parameter(name='SWM',bname='swm',type='Variable',family='Water Fraction',measurement='',unit='v/v',value='11R-K03_pilot..SWM',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:shm
#Family:Oil Fraction
#Unit:v/v
#Mode:Out
#Description:
#Format:auto
SHM = Variable("well", "dataset", "", u"Oil Fraction", u"v/v")
parameterDict.update({'SHM' : Parameter(name='SHM',bname='shm',type='Variable',family='Oil Fraction',measurement='',unit='v/v',value='11R-K03_pilot..SHM',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-11-23"""
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
loopSize = SOIR.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	soir = SOIR.value(loopIterator)
	swir = SWIR.value(loopIterator)
	sw = SW.value(loopIterator)
	swm = MissingValue
	shm = MissingValue
	if MissingValue not in [soir, swir, sw] :
		### Automatic Generation Loop End ###
		sh = 1 - sw
		shm = sh - soir
		shm = limitValue(shm, 0, 1)
		swm = 1 - swir - shm - soir
		swm = limitValue(swm,0,1)
	### Begin Automatic Generation EndLoop ###
	SWM.setValue(loopIterator, swm)
	SHM.setValue(loopIterator, shm)
SWM.save(True)
SHM.save(True)
### Automatic Generation EndLoop End ###
