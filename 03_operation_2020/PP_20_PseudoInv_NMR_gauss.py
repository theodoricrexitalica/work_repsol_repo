# -*- coding: utf-8 -*-
from __future__ import division
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
#BName:rsand
#Family:Resistivity
#Unit:ohmm
#Mode:In
#Description:Description
RSAND = Variable("11R-K03_pilot", "Slb_WLL", "RSAND", u"Resistivity", u"ohmm")
parameterDict.update({'RSAND' : Parameter(name='RSAND',bname='rsand',type='Variable',family='Resistivity',measurement='',unit='ohmm',value='11R-K03_pilot.Slb_WLL.RSAND',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:unitless
gausswind_unit = u"unitless"
#Measurement:
gausswind_measurement = u""
#Mode:In
#Description:Description
#Minimum:
#Maximum:
#List:
gausswind = -9999
parameterDict.update({'gausswind' : Parameter(name='gausswind',bname='',type='Number',family='',measurement='',unit='unitless',value='-9999',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:rsand_gaus
#Family:Resistivity
#Unit:ohmm
#Mode:Out
#Description:Description
#Format:auto
RSAND_gaus = Variable("11R-K03_pilot", "Slb_WLL", "RSAND_gauss", u"Resistivity", u"ohmm")
parameterDict.update({'RSAND_gaus' : Parameter(name='RSAND_gaus',bname='rsand_gaus',type='Variable',family='Resistivity',measurement='',unit='ohmm',value='11R-K03_pilot.Slb_WLL.RSAND_gauss',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#DeclarationsEnd
### Begin Automatic Generation Loop ###
loopSize = RSAND.referenceSize()
loopRange = xrange(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	rsand = RSAND.value(loopIterator)
	rsand_gaus = MissingValue
	### Automatic Generation Loop End ###
	import TechlogStat as ts
	rsand=ts.gaussianSmooth(rsand,gausswind)
	### Begin Automatic Generation EndLoop ###
	RSAND_gaus.setValue(loopIterator, rsand_gaus)
RSAND_gaus.save(True)
### Automatic Generation EndLoop End ###

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-06-12"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""