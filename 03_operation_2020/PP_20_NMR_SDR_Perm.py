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
#BName:t2lm
#Family:NMR T2 Logarithmic Mean
#Unit:ms
#Mode:In
#Description:
T2LM = Variable("well", "dataset", "", u"NMR T2 Logarithmic Mean", u"ms")
parameterDict.update({'T2LM' : Parameter(name='T2LM',bname='t2lm',type='Variable',family='NMR T2 Logarithmic Mean',measurement='',unit='ms',value='11R-K03_pilot..',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:mpr
#Family:NMR Porosity
#Unit:v/v
#Mode:In
#Description:
CMR_MRP = Variable("well", "dataset", "", u"NMR Porosity", u"v/v")
parameterDict.update({'CMR_MRP' : Parameter(name='CMR_MRP',bname='mpr',type='Variable',family='NMR Porosity',measurement='',unit='v/v',value='11R-K03_pilot..',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
A_unit = u"unitless"
#Measurement:Coefficient
A_measurement = u"Coefficient"
#Mode:In
#Description:1st coeff
#Minimum:
#Maximum:
#List:
A = 4
parameterDict.update({'A' : Parameter(name='A',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='4',mode='In',description='1st coeff',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
B_unit = u"unitless"
#Measurement:Coefficient
B_measurement = u"Coefficient"
#Mode:In
#Description:power of t2lm
#Minimum:
#Maximum:
#List:
B = 2
parameterDict.update({'B' : Parameter(name='B',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='2',mode='In',description='power of t2lm',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
C_unit = u"unitless"
#Measurement:Coefficient
C_measurement = u"Coefficient"
#Mode:In
#Description:power of phit
#Minimum:
#Maximum:
#List:
C = 4
parameterDict.update({'C' : Parameter(name='C',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='4',mode='In',description='power of phit',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:perm
#Family:Permeability
#Unit:mD
#Mode:Out
#Description:
#Format:auto
PERM_SDR = Variable("well", "dataset", "", u"Permeability", u"mD")
parameterDict.update({'PERM_SDR' : Parameter(name='PERM_SDR',bname='perm',type='Variable',family='Permeability',measurement='',unit='mD',value='11R-K03_pilot..PERM_SDR',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
loopSize = T2LM.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	t2lm = T2LM.value(loopIterator)
	mpr = CMR_MRP.value(loopIterator)
	perm = MissingValue
	if MissingValue not in [t2lm, mpr] :
		### Automatic Generation Loop End ###
		if t2lm > 0 and mpr > 0:
			perm=A*((mpr)**C)*((t2lm)**B)
	### Begin Automatic Generation EndLoop ###
	PERM_SDR.setValue(loopIterator, perm)
PERM_SDR.save(True)
### Automatic Generation EndLoop End ###
