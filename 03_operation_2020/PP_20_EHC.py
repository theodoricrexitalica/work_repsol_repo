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
#BName:perf
#Family:Perforation
#Unit:unitless
#Mode:In
#Description:Description
Perf = Variable("G-1", "Slb_WLL", "Perf", u"Perforation", u"unitless")
parameterDict.update({'Perf' : Parameter(name='Perf',bname='perf',type='Variable',family='Perforation',measurement='',unit='unitless',value='G-1.Slb_WLL.Perf',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:vsh
#Family:Shale Volume
#Unit:v/v
#Mode:In
#Description:Description
VSH = Variable("G-1", "Slb_WLL", "CMR_VSH", u"Shale Volume", u"v/v")
parameterDict.update({'VSH' : Parameter(name='VSH',bname='vsh',type='Variable',family='Shale Volume',measurement='',unit='v/v',value='G-1.Slb_WLL.CMR_VSH',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:phit
#Family:Total Porosity
#Unit:v/v
#Mode:In
#Description:Description
PHIT = Variable("G-1", "Slb_WLL", "PHIT_D_tbu_clean", u"Total Porosity", u"v/v")
parameterDict.update({'PHIT' : Parameter(name='PHIT',bname='phit',type='Variable',family='Total Porosity',measurement='',unit='v/v',value='G-1.Slb_WLL.PHIT_D_tbu_clean',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:swt
#Family:Water Saturation
#Unit:v/v
#Mode:In
#Description:Description
SWT = Variable("G-1", "Slb_WLL", "SWT_n179_v2", u"Water Saturation", u"v/v")
parameterDict.update({'SWT' : Parameter(name='SWT',bname='swt',type='Variable',family='Water Saturation',measurement='',unit='v/v',value='G-1.Slb_WLL.SWT_n179_v2',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:ehc
#Family:Productivity Index
#Unit:
#Mode:Out
#Description:Description
#Format:auto
EHC = Variable("G-1", "Slb_WLL", "EHC", u"Productivity Index", u"")
parameterDict.update({'EHC' : Parameter(name='EHC',bname='ehc',type='Variable',family='Productivity Index',measurement='',unit='',value='G-1.Slb_WLL.EHC',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2021-03-25"""
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
credits = 0
def add_credits(x):
	global credits
	credits = credits + x
	return credits 

### Begin Automatic Generation Loop [LOOP_INV_MVTEST:]###
loopSize = Perf.referenceSize()
loopRange = range(loopSize)
for loopIterator in reversed(loopRange):
	datasetIterator = loopIterator
	perf = Perf.value(loopIterator)
	vsh = VSH.value(loopIterator)
	phit = PHIT.value(loopIterator)
	swt = SWT.value(loopIterator)
	ehc = MissingValue
	if MissingValue not in [perf, vsh, phit, swt] :
		### Automatic Generation Loop End ###
		if perf == 1:
			ehc_calc = ((1-vsh)*phit*swt)
			ehc = add_credits(ehc_calc)
			print(ehc)
	### Begin Automatic Generation EndLoop ###
	EHC.setValue(loopIterator, ehc)
EHC.save(True)
### Automatic Generation EndLoop End ###
