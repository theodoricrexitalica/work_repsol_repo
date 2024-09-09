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
#BName:calcite_flag
#Family:Calcite Flag
#Unit:unitless
#Mode:In
#Description:Description
CALCITE_FLAG = Variable("11R-K03_pilot", "Repsol_PPeval", "Calcite_flag", u"Calcite Flag", u"unitless")
parameterDict.update({'CALCITE_FLAG' : Parameter(name='CALCITE_FLAG',bname='calcite_flag',type='Variable',family='Calcite Flag',measurement='',unit='unitless',value='11R-K03_pilot.Repsol_PPeval.Calcite_flag',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:calcite_filter
#Family:Calcite Flag
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
CALCITE_FILTER = Variable("11R-K03_pilot", "Repsol_PPeval", "Calcite_filter", u"Calcite Flag", u"unitless")
parameterDict.update({'CALCITE_FILTER' : Parameter(name='CALCITE_FILTER',bname='calcite_filter',type='Variable',family='Calcite Flag',measurement='',unit='unitless',value='11R-K03_pilot.Repsol_PPeval.Calcite_filter',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#DeclarationsEnd
### Begin Automatic Generation Loop ###
loopSize = CALCITE_FLAG.referenceSize()
loopRange = xrange(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	calcite_flag = CALCITE_FLAG.value(loopIterator)
	calcite_filter = MissingValue
	### Automatic Generation Loop End ###
	if calcite_flag == 1:
		calcite_filter = -9999
	else:
		calcite_filter = 1
		
	### Begin Automatic Generation EndLoop ###
	CALCITE_FILTER.setValue(loopIterator, calcite_filter)
CALCITE_FILTER.save(True)
### Automatic Generation EndLoop End ###

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-06-21"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""