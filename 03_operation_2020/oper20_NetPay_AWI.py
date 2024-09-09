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
#BName:flag_res
#Family:Net Reservoir Flag
#Unit:unitless
#Mode:In
#Description:Description
FLAG_RES = Variable("11R-K03_ST3", "LWD", "FLAG_RES", u"Net Reservoir Flag", u"unitless")
parameterDict.update({'FLAG_RES' : Parameter(name='FLAG_RES',bname='flag_res',type='Variable',family='Net Reservoir Flag',measurement='',unit='unitless',value='11R-K03_ST3.LWD.FLAG_RES',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:flag_hpay
#Family:Net Flag
#Unit:unitless
#Mode:In
#Description:Description
FLAG_HPAY = Variable("11R-K03_ST3", "LWD", "FLAG_HPAY", u"Net Flag", u"unitless")
parameterDict.update({'FLAG_HPAY' : Parameter(name='FLAG_HPAY',bname='flag_hpay',type='Variable',family='Net Flag',measurement='',unit='unitless',value='11R-K03_ST3.LWD.FLAG_HPAY',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:flag_st
#Family:General Flag
#Unit:unitless
#Mode:In
#Description:Description
FLAG_ST = Variable("11R-K03_ST3", "LWD", "FLAG_ST", u"General Flag", u"unitless")
parameterDict.update({'FLAG_ST' : Parameter(name='FLAG_ST',bname='flag_st',type='Variable',family='General Flag',measurement='',unit='unitless',value='11R-K03_ST3.LWD.FLAG_ST',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Number
#Unit:m
Sample_rate_unit = u"m"
#Measurement:
Sample_rate_measurement = u""
#Mode:In
#Description:Sampling rate of dataset in terms of MD
#Minimum:
#Maximum:
#List:
Sample_rate = 0.1
parameterDict.update({'Sample_rate' : Parameter(name='Sample_rate',bname='',type='Number',family='',measurement='',unit='m',value='0.1',mode='In',description='Sampling rate of dataset in terms of MD',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#DeclarationsEnd
cc1 = 0
cc2 = 0
cc3 = 0
wn = FLAG_RES.wellName()

### Begin Automatic Generation Loop ###
loopSize = FLAG_RES.referenceSize()
loopRange = xrange(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	flag_res = FLAG_RES.value(loopIterator)
	flag_hpay = FLAG_HPAY.value(loopIterator)
	flag_st = FLAG_ST.value(loopIterator)
	### Automatic Generation Loop End ###
	if flag_st == 1:
		cc1 =cc1+1
	if flag_res == 1 and flag_st == 1:
		cc2 =cc2+1
	if flag_res == 1 and flag_st == 1 and flag_hpay == 1:
		cc3 =cc3+1
	### Begin Automatic Generation EndLoop ###
### Automatic Generation EndLoop End ###
print wn
print "Total ST:", cc1*Sample_rate, "m"
print "Total res:", cc2*Sample_rate, "m"
print "Best res:", cc3*Sample_rate, "m"

print "Effectivness ST:", round(((cc3*Sample_rate)/(cc2*Sample_rate))*100,0), "%"


__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-06-12"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""