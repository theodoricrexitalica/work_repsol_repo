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
#BName:c1_gzg
#Family:Mud Gas C1
#Unit:ppm
#Mode:In
#Description:Description
C1_GZG = Variable("11R-K03_ST4", "Mudlogs", "C1_GZG", u"Mud Gas C1", u"ppm")
parameterDict.update({'C1_GZG' : Parameter(name='C1_GZG',bname='c1_gzg',type='Variable',family='Mud Gas C1',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.C1_GZG',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:c2_gzg
#Family:Mud Gas C2
#Unit:ppm
#Mode:In
#Description:Description
C2_GZG = Variable("11R-K03_ST4", "Mudlogs", "C2_GZG", u"Mud Gas C2", u"ppm")
parameterDict.update({'C2_GZG' : Parameter(name='C2_GZG',bname='c2_gzg',type='Variable',family='Mud Gas C2',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.C2_GZG',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:c3_gzg
#Family:Mud Gas C3
#Unit:ppm
#Mode:In
#Description:Description
C3_GZG = Variable("11R-K03_ST4", "Mudlogs", "C3_GZG", u"Mud Gas C3", u"ppm")
parameterDict.update({'C3_GZG' : Parameter(name='C3_GZG',bname='c3_gzg',type='Variable',family='Mud Gas C3',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.C3_GZG',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:ic4_gzg
#Family:Mud Gas IC4
#Unit:ppm
#Mode:In
#Description:Description
IC4_GZG = Variable("11R-K03_ST4", "Mudlogs", "iC4_GZG", u"Mud Gas IC4", u"ppm")
parameterDict.update({'IC4_GZG' : Parameter(name='IC4_GZG',bname='ic4_gzg',type='Variable',family='Mud Gas IC4',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.iC4_GZG',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:ic5_gzg
#Family:Mud Gas IC5
#Unit:ppm
#Mode:In
#Description:Description
IC5_GZG = Variable("11R-K03_ST4", "Mudlogs", "iC5_GZG", u"Mud Gas IC5", u"ppm")
parameterDict.update({'IC5_GZG' : Parameter(name='IC5_GZG',bname='ic5_gzg',type='Variable',family='Mud Gas IC5',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.iC5_GZG',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:nc4_gzg
#Family:Mud Gas NC4
#Unit:ppm
#Mode:In
#Description:Description
NC4_GZG = Variable("11R-K03_ST4", "Mudlogs", "nC4_GZG", u"Mud Gas NC4", u"ppm")
parameterDict.update({'NC4_GZG' : Parameter(name='NC4_GZG',bname='nc4_gzg',type='Variable',family='Mud Gas NC4',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.nC4_GZG',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:nc5_gzg
#Family:Mud Gas NC5
#Unit:ppm
#Mode:In
#Description:Description
NC5_GZG = Variable("11R-K03_ST4", "Mudlogs", "nC5_GZG", u"Mud Gas NC5", u"ppm")
parameterDict.update({'NC5_GZG' : Parameter(name='NC5_GZG',bname='nc5_gzg',type='Variable',family='Mud Gas NC5',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.nC5_GZG',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:c1_in
#Family:Mud Gas C1
#Unit:ppm
#Mode:In
#Description:Description
C1_IN = Variable("11R-K03_ST4", "Mudlogs", "C1_In", u"Mud Gas C1", u"ppm")
parameterDict.update({'C1_IN' : Parameter(name='C1_IN',bname='c1_in',type='Variable',family='Mud Gas C1',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.C1_In',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:c2_in
#Family:Mud Gas C2
#Unit:ppm
#Mode:In
#Description:Description
C2_IN = Variable("11R-K03_ST4", "Mudlogs", "C2_In", u"Mud Gas C2", u"ppm")
parameterDict.update({'C2_IN' : Parameter(name='C2_IN',bname='c2_in',type='Variable',family='Mud Gas C2',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.C2_In',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:c3_in
#Family:Mud Gas C3
#Unit:ppm
#Mode:In
#Description:Description
C3_IN = Variable("11R-K03_ST4", "Mudlogs", "C3_In", u"Mud Gas C3", u"ppm")
parameterDict.update({'C3_IN' : Parameter(name='C3_IN',bname='c3_in',type='Variable',family='Mud Gas C3',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.C3_In',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:ic4_in
#Family:Mud Gas IC4
#Unit:ppm
#Mode:In
#Description:Description
IC4_IN = Variable("11R-K03_ST4", "Mudlogs", "iC4_In", u"Mud Gas IC4", u"ppm")
parameterDict.update({'IC4_IN' : Parameter(name='IC4_IN',bname='ic4_in',type='Variable',family='Mud Gas IC4',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.iC4_In',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:ic5_in
#Family:Mud Gas IC5
#Unit:ppm
#Mode:In
#Description:Description
IC5_IN = Variable("11R-K03_ST4", "Mudlogs", "iC5_In", u"Mud Gas IC5", u"ppm")
parameterDict.update({'IC5_IN' : Parameter(name='IC5_IN',bname='ic5_in',type='Variable',family='Mud Gas IC5',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.iC5_In',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:nc4_in
#Family:Mud Gas NC4
#Unit:ppm
#Mode:In
#Description:Description
NC4_IN = Variable("11R-K03_ST4", "Mudlogs", "nC4_In", u"Mud Gas NC4", u"ppm")
parameterDict.update({'NC4_IN' : Parameter(name='NC4_IN',bname='nc4_in',type='Variable',family='Mud Gas NC4',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.nC4_In',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:nc5_in
#Family:Mud Gas NC5
#Unit:ppm
#Mode:In
#Description:Description
NC5_IN = Variable("11R-K03_ST4", "Mudlogs", "nC5_In", u"Mud Gas NC5", u"ppm")
parameterDict.update({'NC5_IN' : Parameter(name='NC5_IN',bname='nc5_in',type='Variable',family='Mud Gas NC5',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.nC5_In',mode='In',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:c1_delta
#Family:Mud Gas C1
#Unit:ppm
#Mode:Out
#Description:Description
#Format:auto
C1_DELTA = Variable("11R-K03_ST4", "Mudlogs", "C1_delta", u"Mud Gas C1", u"ppm")
parameterDict.update({'C1_DELTA' : Parameter(name='C1_DELTA',bname='c1_delta',type='Variable',family='Mud Gas C1',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.C1_delta',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:c2_delta
#Family:Mud Gas C2
#Unit:ppm
#Mode:Out
#Description:Description
#Format:auto
C2_DELTA = Variable("11R-K03_ST4", "Mudlogs", "C2_delta", u"Mud Gas C2", u"ppm")
parameterDict.update({'C2_DELTA' : Parameter(name='C2_DELTA',bname='c2_delta',type='Variable',family='Mud Gas C2',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.C2_delta',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:c3_delta
#Family:Mud Gas C3
#Unit:ppm
#Mode:Out
#Description:Description
#Format:auto
C3_DELTA = Variable("11R-K03_ST4", "Mudlogs", "C3_delta", u"Mud Gas C3", u"ppm")
parameterDict.update({'C3_DELTA' : Parameter(name='C3_DELTA',bname='c3_delta',type='Variable',family='Mud Gas C3',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.C3_delta',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:ic4_delta
#Family:Mud Gas IC4
#Unit:ppm
#Mode:Out
#Description:Description
#Format:auto
IC4_DELTA = Variable("11R-K03_ST4", "Mudlogs", "iC4_delta", u"Mud Gas IC4", u"ppm")
parameterDict.update({'IC4_DELTA' : Parameter(name='IC4_DELTA',bname='ic4_delta',type='Variable',family='Mud Gas IC4',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.iC4_delta',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:ic5_delta
#Family:Mud Gas IC5
#Unit:ppm
#Mode:Out
#Description:Description
#Format:auto
IC5_DELTA = Variable("11R-K03_ST4", "Mudlogs", "iC5_delta", u"Mud Gas IC5", u"ppm")
parameterDict.update({'IC5_DELTA' : Parameter(name='IC5_DELTA',bname='ic5_delta',type='Variable',family='Mud Gas IC5',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.iC5_delta',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:nc4_delta
#Family:Mud Gas NC4
#Unit:ppm
#Mode:Out
#Description:Description
#Format:auto
NC4_DELTA = Variable("11R-K03_ST4", "Mudlogs", "nC4_delta", u"Mud Gas NC4", u"ppm")
parameterDict.update({'NC4_DELTA' : Parameter(name='NC4_DELTA',bname='nc4_delta',type='Variable',family='Mud Gas NC4',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.nC4_delta',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:nc5_delta
#Family:Mud Gas NC5
#Unit:ppm
#Mode:Out
#Description:Description
#Format:auto
NC5_DELTA = Variable("11R-K03_ST4", "Mudlogs", "nC5_delta", u"Mud Gas NC5", u"ppm")
parameterDict.update({'NC5_DELTA' : Parameter(name='NC5_DELTA',bname='nc5_delta',type='Variable',family='Mud Gas NC5',measurement='',unit='ppm',value='11R-K03_ST4.Mudlogs.nC5_delta',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:bh_delta
#Family:Mud Gas Balance
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
BH_DELTA = Variable("11R-K03_ST4", "Mudlogs", "Bh_delta", u"Mud Gas Balance", u"unitless")
parameterDict.update({'BH_DELTA' : Parameter(name='BH_DELTA',bname='bh_delta',type='Variable',family='Mud Gas Balance',measurement='',unit='unitless',value='11R-K03_ST4.Mudlogs.Bh_delta',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:wh_delta
#Family:Mud Gas Wetness
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
WH_DELTA = Variable("11R-K03_ST4", "Mudlogs", "Wh_delta", u"Mud Gas Wetness", u"unitless")
parameterDict.update({'WH_DELTA' : Parameter(name='WH_DELTA',bname='wh_delta',type='Variable',family='Mud Gas Wetness',measurement='',unit='unitless',value='11R-K03_ST4.Mudlogs.Wh_delta',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:bh
#Family:Mud Gas Balance
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
BH = Variable("11R-K03_ST4", "Mudlogs", "Bh", u"Mud Gas Balance", u"unitless")
parameterDict.update({'BH' : Parameter(name='BH',bname='bh',type='Variable',family='Mud Gas Balance',measurement='',unit='unitless',value='11R-K03_ST4.Mudlogs.Bh',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#Type:Variable
#BName:wh
#Family:Mud Gas Wetness
#Unit:unitless
#Mode:Out
#Description:Description
#Format:auto
WH = Variable("11R-K03_ST4", "Mudlogs", "Wh", u"Mud Gas Wetness", u"unitless")
parameterDict.update({'WH' : Parameter(name='WH',bname='wh',type='Variable',family='Mud Gas Wetness',measurement='',unit='unitless',value='11R-K03_ST4.Mudlogs.Wh',mode='Out',description='Description',group='',min='',max='',list='',enable='True',iscombocheckbox='False',isused='True')})
#DeclarationsEnd
### Begin Automatic Generation Loop [LOOP_MVTEST:]###
loopSize = C1_GZG.referenceSize()
loopRange = xrange(loopSize)
for loopIterator in loopRange:
	datasetIterator = loopIterator
	c1_gzg = C1_GZG.value(loopIterator)
	c2_gzg = C2_GZG.value(loopIterator)
	c3_gzg = C3_GZG.value(loopIterator)
	ic4_gzg = IC4_GZG.value(loopIterator)
	ic5_gzg = IC5_GZG.value(loopIterator)
	nc4_gzg = NC4_GZG.value(loopIterator)
	nc5_gzg = NC5_GZG.value(loopIterator)
	c1_in = C1_IN.value(loopIterator)
	c2_in = C2_IN.value(loopIterator)
	c3_in = C3_IN.value(loopIterator)
	ic4_in = IC4_IN.value(loopIterator)
	ic5_in = IC5_IN.value(loopIterator)
	nc4_in = NC4_IN.value(loopIterator)
	nc5_in = NC5_IN.value(loopIterator)
	c1_delta = MissingValue
	c2_delta = MissingValue
	c3_delta = MissingValue
	ic4_delta = MissingValue
	ic5_delta = MissingValue
	nc4_delta = MissingValue
	nc5_delta = MissingValue
	bh_delta = MissingValue
	wh_delta = MissingValue
	bh = MissingValue
	wh = MissingValue
	if MissingValue not in [c1_gzg, c2_gzg, c3_gzg, ic4_gzg, ic5_gzg, nc4_gzg, nc5_gzg, c1_in, c2_in, c3_in, ic4_in, ic5_in, nc4_in, nc5_in] :
		### Automatic Generation Loop End ###
		c1_delta = c1_gzg - c1_in
		c2_delta = c2_gzg - c2_in
		c3_delta = c3_gzg - c3_in
		ic4_delta = ic4_gzg - ic4_in
		ic5_delta = ic5_gzg - ic5_in
		nc4_delta = nc4_gzg - nc4_in
		nc5_delta = nc5_gzg - nc5_in
		wh_delta = ((c2_delta + c3_delta + ic4_delta  + ic5_delta + nc4_delta + nc5_delta) / (c1_delta + c2_delta + c3_delta + ic4_delta  + ic5_delta + nc4_delta + nc5_delta))*100
		bh_delta = (c1_delta + c2_delta) / (c3_delta + ic4_delta  + ic5_delta + nc4_delta + nc5_delta)
		#wh = ((c2_gzg + c3_gzg + ic4_gzg  + ic5_gzg + nc4_gzg + nc5_gzg) / (c1_gzg + c2_gzg + c3_gzg + ic4_gzg  + ic5_gzg + nc4_gzg + nc5_gzg))*100
		#bh = (c1_gzg + c2_gzg) / (c3_gzg + ic4_gzg  + ic5_gzg + nc4_gzg + nc5_gzg)
		#print c1_delta, c2_delta, c3_delta, ic4_delta, ic5_delta, nc4_delta, nc5_delta , wh_delta, bh_delta
	### Begin Automatic Generation EndLoop ###
	C1_DELTA.setValue(loopIterator, c1_delta)
	C2_DELTA.setValue(loopIterator, c2_delta)
	C3_DELTA.setValue(loopIterator, c3_delta)
	IC4_DELTA.setValue(loopIterator, ic4_delta)
	IC5_DELTA.setValue(loopIterator, ic5_delta)
	NC4_DELTA.setValue(loopIterator, nc4_delta)
	NC5_DELTA.setValue(loopIterator, nc5_delta)
	BH_DELTA.setValue(loopIterator, bh_delta)
	WH_DELTA.setValue(loopIterator, wh_delta)
	BH.setValue(loopIterator, bh)
	WH.setValue(loopIterator, wh)
C1_DELTA.save(True)
C2_DELTA.save(True)
C3_DELTA.save(True)
IC4_DELTA.save(True)
IC5_DELTA.save(True)
NC4_DELTA.save(True)
NC5_DELTA.save(True)
BH_DELTA.save(True)
WH_DELTA.save(True)
BH.save(True)
WH.save(True)
### Automatic Generation EndLoop End ###

__author__ = """Taras DOLGUSHIN (SE64403)"""
__date__ = """2020-06-12"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__executionGranularity__ = """full"""