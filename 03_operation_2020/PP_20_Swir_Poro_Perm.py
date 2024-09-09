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
#BName:phit
#Family:Total Porosity
#Unit:v/v
#Mode:In
#Description:Description
PhiT = Variable("G-3", "Slb_WLL", "", u"Total Porosity", u"v/v")
parameterDict.update({'PhiT' : Parameter(name='PhiT',bname='phit',type='Variable',family='Total Porosity',measurement='',unit='v/v',value='G-3.Slb_WLL.',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swir
#Family:Irreducible Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
Swirr = Variable("G-3", "Slb_WLL", "", u"Irreducible Water Saturation", u"v/v")
parameterDict.update({'Swirr' : Parameter(name='Swirr',bname='swir',type='Variable',family='Irreducible Water Saturation',measurement='',unit='v/v',value='G-3.Slb_WLL.',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:perm
#Family:Permeability
#Unit:mD
#Mode:Out
#Description:Description
#Format:auto
Perm = Variable("G-3", "Slb_WLL", "Perm_swireg", u"Permeability", u"mD")
parameterDict.update({'Perm' : Parameter(name='Perm',bname='perm',type='Variable',family='Permeability',measurement='',unit='mD',value='G-3.Slb_WLL.Perm_swireg',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

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
import math as mt

### Begin Automatic Generation Loop [LOOP_MVTEST:]###
loopSize = PhiT.referenceSize()
loopRange = range(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	phit = PhiT.value(loopIterator)
	swir = Swirr.value(loopIterator)
	perm = MissingValue
	if MissingValue not in [phit, swir] :
		### Automatic Generation Loop End ###
		if swir >= 0.7:
			perm =10**(6.169275 * mt.log10(phit) + 3.331224)
		elif 0.6 <= swir <0.7:
			perm = 10**(6.087876 * mt.log10(phit) + 3.581742)
		elif 0.5 <= swir <0.6:
			perm = 10**(6.216577 * mt.log10(phit) + 4.040152)
		elif swir < 0.5:
			perm= 10**(6.236368 * mt.log10(phit) + 4.561522)
	### Begin Automatic Generation EndLoop ###
	Perm.setValue(loopIterator, perm)
Perm.save(True)
### Automatic Generation EndLoop End ###
