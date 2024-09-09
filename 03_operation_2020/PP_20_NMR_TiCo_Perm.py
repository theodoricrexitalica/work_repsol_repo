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
#BName:ffv16
#Family:NMR Free Fluids
#Unit:v/v
#Mode:In
#Description:
CMR_FFV_16MS = Variable("well", "dataset", "", u"NMR Free Fluids", u"v/v")
parameterDict.update({'CMR_FFV_16MS' : Parameter(name='CMR_FFV_16MS',bname='ffv16',type='Variable',family='NMR Free Fluids',measurement='',unit='v/v',value='11R-K03_pilot.Slb_WLL.',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:mpr
#Family:NMR Porosity
#Unit:v/v
#Mode:In
#Description:
CMR_MRP = Variable("well", "dataset", "", u"NMR Porosity", u"v/v")
parameterDict.update({'CMR_MRP' : Parameter(name='CMR_MRP',bname='mpr',type='Variable',family='NMR Porosity',measurement='',unit='v/v',value='11R-K03_pilot.Slb_WLL.',mode='In',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
A_unit = u"unitless"
#Measurement:Coefficient
A_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
A = 1
parameterDict.update({'A' : Parameter(name='A',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='1',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
B_unit = u"unitless"
#Measurement:Coefficient
B_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
B = 4
parameterDict.update({'B' : Parameter(name='B',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='4',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
C_unit = u"unitless"
#Measurement:Coefficient
C_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
C = 2
parameterDict.update({'C' : Parameter(name='C',bname='',type='Number',family='',measurement='Coefficient',unit='unitless',value='2',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:perm
#Family:Permeability
#Unit:mD
#Mode:Out
#Description:
#Format:auto
PERM_TiCo = Variable("11R-K03_pilot", "Slb_WLL", "PERM_TiCo", u"Permeability", u"mD")
parameterDict.update({'PERM_TiCo' : Parameter(name='PERM_TiCo',bname='perm',type='Variable',family='Permeability',measurement='',unit='mD',value='11R-K03_pilot.Slb_WLL.PERM_TiCo',mode='Out',description='',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
loopSize = CMR_FFV_16MS.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	ffv16 = CMR_FFV_16MS.value(loopIterator)
	mpr = CMR_MRP.value(loopIterator)
	perm = MissingValue
	if MissingValue not in [ffv16, mpr] :
		### Automatic Generation Loop End ###
		if ffv16 > 0 or mpr > 0:
			perm=A*(10**4)*(mpr**B)*((ffv16/(mpr-ffv16))**C)
	### Begin Automatic Generation EndLoop ###
	PERM_TiCo.setValue(loopIterator, perm)
PERM_TiCo.save(True)
### Automatic Generation EndLoop End ###
