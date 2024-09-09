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
#BName:fsand
#Family:Sand Volume Fraction
#Unit:v/v
#Mode:In
#Description:Description
FSAND = Variable("well", "dataset", "", u"Sand Volume Fraction", u"v/v")
parameterDict.update({'FSAND' : Parameter(name='FSAND',bname='fsand',type='Variable',family='Sand Volume Fraction',measurement='',unit='v/v',value='11R-K03_pilot..',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:at90
#Family:Formation Resistivity
#Unit:ohmm
#Mode:In
#Description:Description
AT90 = Variable("well", "dataset", "", u"Formation Resistivity", u"ohmm")
parameterDict.update({'AT90' : Parameter(name='AT90',bname='at90',type='Variable',family='Formation Resistivity',measurement='',unit='ohmm',value='11R-K03_pilot..',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:fshale
#Family:Shale Volume
#Unit:v/v
#Mode:In
#Description:Sampling rate of dataset in terms of MD
VSH = Variable("well", "dataset", "", u"Shale Volume", u"v/v")
parameterDict.update({'VSH' : Parameter(name='VSH',bname='fshale',type='Variable',family='Shale Volume',measurement='',unit='v/v',value='11R-K03_pilot..',mode='In',description='Sampling rate of dataset in terms of MD',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:ohmm
rshale_unit = u"ohmm"
#Measurement:
rshale_measurement = u""
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
rshale = -9999
parameterDict.update({'rshale' : Parameter(name='rshale',bname='',type='Number',family='',measurement='',unit='ohmm',value='-9999',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:v/v
vshale_corr_unit = u"v/v"
#Measurement:
vshale_corr_measurement = u""
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
vshale_corr = 0.1
parameterDict.update({'vshale_corr' : Parameter(name='vshale_corr',bname='',type='Number',family='',measurement='',unit='v/v',value='0.1',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:rsand
#Family:Resistivity
#Unit:ohmm
#Mode:Out
#Description:Description
#Format:auto
RSAND = Variable("well", "dataset", "", u"Resistivity", u"ohmm")
parameterDict.update({'RSAND' : Parameter(name='RSAND',bname='rsand',type='Variable',family='Resistivity',measurement='',unit='ohmm',value='11R-K03_pilot..Rsand',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-06-12"""
__version__ = """1.0"""
__pyVersion__ = """2"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__applyMode__ = """0"""
__awiEngine__ = """v1"""
__layoutTemplateMode__ = """"""
__includeMissingValues__ = """True"""
__keepPreviouslyComputedValues__ = """True"""
__areInputDisplayed__ = """True"""
__useMultiWellLayout__ = """True"""
__idForHelp__ = """"""
__executionGranularity__ = """full"""
#DeclarationsEnd
### Begin Automatic Generation Loop ###
loopSize = FSAND.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	fsand = FSAND.value(loopIterator)
	at90 = AT90.value(loopIterator)
	fshale = VSH.value(loopIterator)
	rsand = MissingValue
	### Automatic Generation Loop End ###
	rsand = ((fsand+vshale_corr)*at90*rshale)/(rshale - at90*(fshale-vshale_corr))
	### Begin Automatic Generation EndLoop ###
	RSAND.setValue(loopIterator, rsand)
RSAND.save(True)
### Automatic Generation EndLoop End ###
