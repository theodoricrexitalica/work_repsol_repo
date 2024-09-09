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
#BName:log
#Family:
#Unit:
#Mode:In
#Description:
Input = Variable("well", "dataset", "", u"", u"")
parameterDict.update({'Input' : Parameter(name='Input',bname='log',type='Variable',family='',measurement='',unit='',value='Well10..Input',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:logIndex
#Family:Normalization Factor
#Unit:unitless
#Mode:Out
#Description:
#Format:auto
Result = Variable("well", "dataset", "", u"Normalization Factor", u"unitless")
parameterDict.update({'Result' : Parameter(name='Result',bname='logIndex',type='Variable',family='Normalization Factor',measurement='',unit='unitless',value='Well10..LogNorm',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
Log_min_unit = u"unitless"
#Measurement:Dimensionless
Log_min_measurement = u"Dimensionless"
#Mode:In
#Description:
#Minimum:
#Maximum:
#List:
Log_min = 0
parameterDict.update({'Log_min' : Parameter(name='Log_min',bname='',type='Number',family='',measurement='Dimensionless',unit='unitless',value='0',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
Log_maх_unit = u"unitless"
#Measurement:Dimensionless
Log_maх_measurement = u"Dimensionless"
#Mode:In
#Description:
#Minimum:
#Maximum:
#List:
Log_maх = 1
parameterDict.update({'Log_maх' : Parameter(name='Log_maх',bname='',type='Number',family='',measurement='Dimensionless',unit='unitless',value='1',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__doc__ = """Example of Shale Computation with several methods


©Schlumberger 2018

Software Integrated Solutions
Montpellier Technology Center
Parc Industriel et Technologique de la Pompignane
895 Rue de la Vieille poste
34006 Montpellier France

All rights reserved.
"""
__author__ = """©Schlumberger"""
__date__ = """2006"""
__version__ = """1.0.0"""
__link__ = """http://www.slb.com/techlog"""
__pyVersion__ = """3"""
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
loopSize = Input.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	log = Input.value(loopIterator)
	logIndex = MissingValue
	### Automatic Generation Loop End ###
	logIndex = (log - Log_min) / (Log_maх - Log_min)
	logIndex = limitValue(logIndex, 0, 1)

	
	### Begin Automatic Generation EndLoop ###
	Result.setValue(loopIterator, logIndex)
Result.save(True)
### Automatic Generation EndLoop End ###
