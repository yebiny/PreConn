#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Fri Apr  3 10:56:08 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Setting 

date=200420
direction = +1

Rec_size = 0.23
RecM_size= 0.09
Rec_gap  = 0.045
Rec_color= 'white'

Dia_size = 0.2
Dia_color= 'white'
Dia_line_width = 20
Dia_pos = 0
Dia_v = 0.0015


# Set data
expInfo = {'participant': '', 'session': '001'}
expName = '3-dia'  # from the Builder filename that created this script
expInfo['expName'] = date
expInfo['date'] = 200420  # add a simple timestamp
psychopyVersion = '2020.1.2'
expInfo['psychopyVersion'] = psychopyVersion

sub = sys.argv[1]

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + '../subjects/%s/data/%s_%s' % (sub, expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nibey/Desktop/WorkSpace/preConn/3-Diamond/untitled_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Wait"
WaitClock = core.Clock()
# Initialize components for Routine "Trial"
TrialClock = core.Clock()

Dia = visual.Rect(
    win=win, name='Dia',
    width=Dia_size, height=Dia_size,
    ori=45, pos=(Dia_pos, 0),
    lineWidth=Dia_line_width, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=Dia_color, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
Rec_M = visual.Rect(
    win=win, name='Rec_M',
    width=RecM_size, height=1,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=Rec_color, lineColorSpace='rgb',
    fillColor=Rec_color, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
Rec_R = visual.Rect(
    win=win, name='Rec_R',
    width=Rec_size, height=1,
    ori=0, pos=(0.05+0.5*Rec_size+Rec_gap, 0),
    lineWidth=1, lineColor=Rec_color, lineColorSpace='rgb',
    fillColor=Rec_color, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
Rec_L = visual.Rect(
    win=win, name='Rec_L',
    width=Rec_size, height=1,
    ori=0, pos=(-0.05-0.5*Rec_size-Rec_gap, 0),
    lineWidth=1, lineColor=Rec_color, lineColorSpace='rgb',
    fillColor=Rec_color, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Resp_sub = keyboard.Keyboard()
Resp_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Wait"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
WaitComponents = []
for thisComponent in WaitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Wait"-------
while continueRoutine:
    # get current time
    t = WaitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Wait"-------
for thisComponent in WaitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Trial"-------
continueRoutine = True
# update component parameters for each repeat
Resp_sub.keys = []
Resp_sub.rt = []
_Resp_sub_allKeys = []
Resp_end.keys = []
Resp_end.rt = []
_Resp_end_allKeys = []
# keep track of which components have finished
TrialComponents = [Dia,Rec_M, Rec_R, Rec_L,  Resp_sub, Resp_end]
for thisComponent in TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Trial"-------
while continueRoutine:
    # get current time
    t = TrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Dia* updates

    if Dia_pos > Rec_gap:
        direction = -1
    elif Dia_pos < -Rec_gap:
        direction = +1
   
    Dia_pos = Dia_pos + direction*Dia_v
    Dia.pos = (Dia_pos,0)      
    if Dia.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Dia.frameNStart = frameN  # exact frame index
        Dia.tStart = t  # local t and not account for scr refresh
        Dia.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Dia, 'tStartRefresh')  # time at next scr refresh
        Dia.setAutoDraw(True)
    
    # *Rec_M* updates
    if Rec_M.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rec_M.frameNStart = frameN  # exact frame index
        Rec_M.tStart = t  # local t and not account for scr refresh
        Rec_M.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rec_M, 'tStartRefresh')  # time at next scr refresh
        Rec_M.setAutoDraw(True)
    
    # *Rec_R* updates
    if Rec_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rec_R.frameNStart = frameN  # exact frame index
        Rec_R.tStart = t  # local t and not account for scr refresh
        Rec_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rec_R, 'tStartRefresh')  # time at next scr refresh
        Rec_R.setAutoDraw(True)
    
    # *Rec_L* updates
    if Rec_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rec_L.frameNStart = frameN  # exact frame index
        Rec_L.tStart = t  # local t and not account for scr refresh
        Rec_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rec_L, 'tStartRefresh')  # time at next scr refresh
        Rec_L.setAutoDraw(True)
    
    
    # *Resp_sub* updates
    waitOnFlip = False
    if Resp_sub.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Resp_sub.frameNStart = frameN  # exact frame index
        Resp_sub.tStart = t  # local t and not account for scr refresh
        Resp_sub.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Resp_sub, 'tStartRefresh')  # time at next scr refresh
        Resp_sub.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Resp_sub.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Resp_sub.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Resp_sub.status == STARTED and not waitOnFlip:
        theseKeys = Resp_sub.getKeys(keyList=['left', 'right'], waitRelease=False)
        _Resp_sub_allKeys.extend(theseKeys)
        if len(_Resp_sub_allKeys):
            Resp_sub.keys = [key.name for key in _Resp_sub_allKeys]  # storing all keys
            Resp_sub.rt = [key.rt for key in _Resp_sub_allKeys]    
            #Resp_sub.keys = _Resp_sub_allKeys[-1].name  # just the last key pressed
            #Resp_sub.rt = _Resp_sub_allKeys[-1].rt
    
    # *Resp_end* updates
    waitOnFlip = False
    if Resp_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Resp_end.frameNStart = frameN  # exact frame index
        Resp_end.tStart = t  # local t and not account for scr refresh
        Resp_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Resp_end, 'tStartRefresh')  # time at next scr refresh
        Resp_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Resp_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Resp_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Resp_end.status == STARTED and not waitOnFlip:
        theseKeys = Resp_end.getKeys(keyList=['space'], waitRelease=False)
        _Resp_end_allKeys.extend(theseKeys)
        if len(_Resp_end_allKeys):
            Resp_end.keys = _Resp_end_allKeys[-1].name  # just the last key pressed
            Resp_end.rt = _Resp_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Trial"-------
for thisComponent in TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Dia.started', Dia.tStartRefresh)
thisExp.addData('Dia.stopped', Dia.tStopRefresh)
thisExp.addData('Rec_M.started', Rec_M.tStartRefresh)
thisExp.addData('Rec_M.stopped', Rec_M.tStopRefresh)
thisExp.addData('Rec_R.started', Rec_R.tStartRefresh)
thisExp.addData('Rec_R.stopped', Rec_R.tStopRefresh)
thisExp.addData('Rec_L.started', Rec_L.tStartRefresh)
thisExp.addData('Rec_L.stopped', Rec_L.tStopRefresh)
# check responses
if Resp_sub.keys in ['', [], None]:  # No response was made
    Resp_sub.keys = None
thisExp.addData('Resp_sub.keys',Resp_sub.keys)
if Resp_sub.keys != None:  # we had a response
    thisExp.addData('Resp_sub.rt', Resp_sub.rt)
    print(Resp_sub.keys)
thisExp.addData('Resp_sub.started', Resp_sub.tStartRefresh)
thisExp.addData('Resp_sub.stopped', Resp_sub.tStopRefresh)
thisExp.nextEntry()
# check responses
if Resp_end.keys in ['', [], None]:  # No response was made
    Resp_end.keys = None
thisExp.addData('Resp_end.keys',Resp_end.keys)
if Resp_end.keys != None:  # we had a response
    thisExp.addData('Resp_end.rt', Resp_end.rt)
thisExp.addData('Resp_end.started', Resp_end.tStartRefresh)
thisExp.addData('Resp_end.stopped', Resp_end.tStopRefresh)
thisExp.nextEntry()
# the Routine "Trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
