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
#Unit:unitless
#Mode:In
#Description:Description
RT = Variable("G-3", "Slb_WLL", "RT", u"Petrophysical Group", u"unitless")
parameterDict.update({'RT' : Parameter(name='RT',bname='rt',type='Variable',family='Petrophysical Group',measurement='',unit='unitless',value='G-3.Slb_WLL.RT',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swir_syn
#Family:Irreducible Water Saturation
#Unit:v/v
#Mode:Out
#Description:Description
#Format:auto
SWIR_SYN = Variable("G-3", "Slb_WLL", "SWIR_SYN", u"Irreducible Water Saturation", u"v/v")
parameterDict.update({'SWIR_SYN' : Parameter(name='SWIR_SYN',bname='swir_syn',type='Variable',family='Irreducible Water Saturation',measurement='',unit='v/v',value='G-3.Slb_WLL.SWIR_SYN',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:v/v
swi_1_unit = u"v/v"
#Measurement:Coefficient
swi_1_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
swi_1 = 0.49  
parameterDict.update({'swi_1' : Parameter(name='swi_1',bname='',type='Number',family='',measurement='Coefficient',unit='v/v',value='0.49  ',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:v/v
swi_2_unit = u"v/v"
#Measurement:Coefficient
swi_2_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
swi_2 = 0.44 
parameterDict.update({'swi_2' : Parameter(name='swi_2',bname='',type='Number',family='',measurement='Coefficient',unit='v/v',value='0.44 ',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:v/v
swi_3_unit = u"v/v"
#Measurement:Coefficient
swi_3_measurement = u"Coefficient"
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
swi_3 = 0.65 
parameterDict.update({'swi_3' : Parameter(name='swi_3',bname='',type='Number',family='',measurement='Coefficient',unit='v/v',value='0.65 ',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
loopSize = RT.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	rt = RT.value(loopIterator)
	swir_syn = MissingValue
	if MissingValue not in [rt] :
		### Automatic Generation Loop End ###
		if rt == 1:
			swir_syn = swi_1
		elif rt ==2:
			swir_syn = swi_2
		elif rt == 3:
			swir_syn = swi_3
		
	### Begin Automatic Generation EndLoop ###
	SWIR_SYN.setValue(loopIterator, swir_syn)
SWIR_SYN.save(True)
### Automatic Generation EndLoop End ###
