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
import csv

# Setting 

direction = +1

Rec_size = 0.23
RecM_size= 0.085
Rec_gap  = 0.045
Rec_color= 'white'

Dia_size = 0.2
Dia_color= 'white'
Dia_line_width = 18
Dia_pos = 0
Dia_v = 0.0015
resp_key = ['c', 'd']
wait_key = ['s']

timer = 432

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)


# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name='train', version='',
    extraInfo=None, runtimeInfo=None,
    originPath='/Users/nibey/Desktop/WorkSpace/preConn/3-Dia/untitled_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=None)
# save a log file for detail verbose info

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

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Wait"
WaitClock = core.Clock()
wait_text = visual.TextStim(win=win, name='wait_text',
    text='Train..',
    font='AppleMyungjo',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='black', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
wait_resp = keyboard.Keyboard()

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
    opacity=0.9, depth=-1.0, interpolate=True)
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
Rec_D = visual.Rect(
    win=win, name='Rec_D',
    width=1, height=0.3,
    ori=0, pos=(0, -0.292),
    lineWidth=1, lineColor=Rec_color, lineColorSpace='rgb',
    fillColor=Rec_color, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Opac_more = keyboard.Keyboard()
Opac_less = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Wait"-------
continueRoutine = True
# update component parameters for each repeat
wait_resp.keys = []
wait_resp.rt = []
_wait_resp_allKeys = []
# keep track of which components have finished
WaitComponents = [wait_text, wait_resp]
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

    # *wait_text* updates
    if wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_text.frameNStart = frameN  # exact frame index
        wait_text.tStart = t  # local t and not account for scr refresh
        wait_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_text, 'tStartRefresh')  # time at next scr refresh
        wait_text.setAutoDraw(True)

    # *wait_resp* updates
    waitOnFlip = False
    if wait_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_resp.frameNStart = frameN  # exact frame index
        wait_resp.tStart = t  # local t and not account for scr refresh
        wait_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_resp, 'tStartRefresh')  # time at next scr refresh
        wait_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(wait_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(wait_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if wait_resp.status == STARTED and not waitOnFlip:
        theseKeys = wait_resp.getKeys(keyList=wait_key, waitRelease=False)
        _wait_resp_allKeys.extend(theseKeys)
        if len(theseKeys)!=0:
            Rec_M.opacity+=-0.02
        if len(_wait_resp_allKeys):
            wait_resp.keys = _wait_resp_allKeys[-1].name  # just the last key pressed
            wait_resp.rt = _wait_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
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
thisExp.addData('wait_text.started', wait_text.tStartRefresh)
thisExp.addData('wait_text.stopped', wait_text.tStopRefresh)
# check responses
if wait_resp.keys in ['', [], None]:  # No response was made
    wait_resp.keys = None
thisExp.addData('wait_resp.keys',wait_resp.keys)
if wait_resp.keys != None:  # we had a response
    thisExp.addData('wait_resp.rt', wait_resp.rt)
thisExp.addData('wait_resp.started', wait_resp.tStartRefresh)
thisExp.addData('wait_resp.stopped', wait_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# ------Prepare to start Routine "Trial"-------
continueRoutine = True
# update component parameters for each repeat
Opac_more.keys = []
Opac_more.rt = []
_Opac_more_allKeys = []
Opac_less.keys = []
Opac_less.rt = []
_Opac_less_allKeys = []
# keep track of which components have finished
TrialComponents = [Dia,Rec_M, Rec_R, Rec_L, Rec_D, Opac_more, Opac_less]
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
    if Dia.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Dia.tStartRefresh + timer-frameTolerance:
            # keep track of stop time/frame for later
            Dia.tStop = t  # not accounting for scr refresh
            Dia.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Dia, 'tStopRefresh')  # time at next scr refresh
            Dia.setAutoDraw(False) 
    # *Rec_M* updates
    if Rec_M.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rec_M.frameNStart = frameN  # exact frame index
        Rec_M.tStart = t  # local t and not account for scr refresh
        Rec_M.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rec_M, 'tStartRefresh')  # time at next scr refresh
        Rec_M.setAutoDraw(True)
    if Rec_M.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Rec_M.tStartRefresh + timer-frameTolerance:
            # keep track of stop time/frame for later
            Rec_M.tStop = t  # not accounting for scr refresh
            Rec_M.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Rec_M, 'tStopRefresh')  # time at next scr refresh
            Rec_M.setAutoDraw(False)    
    # *Rec_R* updates
    if Rec_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rec_R.frameNStart = frameN  # exact frame index
        Rec_R.tStart = t  # local t and not account for scr refresh
        Rec_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rec_R, 'tStartRefresh')  # time at next scr refresh
        Rec_R.setAutoDraw(True)
    if Rec_R.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Rec_R.tStartRefresh + timer-frameTolerance:
            # keep track of stop time/frame for later
            Rec_R.tStop = t  # not accounting for scr refresh
            Rec_R.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Rec_R, 'tStopRefresh')  # time at next scr refresh
            Rec_R.setAutoDraw(False)    
    
    # *Rec_L* updates
    if Rec_L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rec_L.frameNStart = frameN  # exact frame index
        Rec_L.tStart = t  # local t and not account for scr refresh
        Rec_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rec_L, 'tStartRefresh')  # time at next scr refresh
        Rec_L.setAutoDraw(True)
    if Rec_L.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Rec_L.tStartRefresh + timer-frameTolerance:
            # keep track of stop time/frame for later
            Rec_L.tStop = t  # not accounting for scr refresh
            Rec_L.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Rec_L, 'tStopRefresh')  # time at next scr refresh
            Rec_L.setAutoDraw(False)    
    # *Rec_D* updates
    if Rec_D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rec_D.frameNStart = frameN  # exact frame index
        Rec_D.tStart = t  # local t and not account for scr refresh
        Rec_D.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rec_D, 'tStartRefresh')  # time at next scr refresh
        Rec_D.setAutoDraw(True)
    if Rec_D.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Rec_D.tStartRefresh + timer-frameTolerance:
            # keep track of stop time/frame for later
            Rec_D.tStop = t  # not accounting for scr refresh
            Rec_D.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Rec_D, 'tStopRefresh')  # time at next scr refresh
            Rec_D.setAutoDraw(False)    
    
    # *Opac_more* updates
    waitOnFlip = False
    if Opac_more.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Opac_more.frameNStart = frameN  # exact frame index
        Opac_more.tStart = t  # local t and not account for scr refresh
        Opac_more.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Opac_more, 'tStartRefresh')  # time at next scr refresh
        Opac_more.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Opac_more.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Opac_more.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Opac_more.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Opac_more.tStartRefresh + timer-frameTolerance:
            # keep track of stop time/frame for later
            Opac_more.tStop = t  # not accounting for scr refresh
            Opac_more.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Opac_more, 'tStopRefresh')  # time at next scr refresh
            Opac_more.setAutoDraw(False)    
    if Opac_more.status == STARTED and not waitOnFlip:
        theseKeys = Opac_more.getKeys(keyList=['right'], waitRelease=False)
        _Opac_more_allKeys.extend(theseKeys)
        
        if len(theseKeys)!=0:
            Rec_M.opacity+=0.02
        if len(_Opac_more_allKeys):
            Opac_more.keys = [key.name for key in _Opac_more_allKeys]  # storing all keys
            Opac_more.rt = [key.rt for key in _Opac_more_allKeys]

            #Opac_more.keys = _Opac_more_allKeys[-1].name  # just the last key pressed
            #Opac_more.rt = _Opac_more_allKeys[-1].rt
    # *Opac_less* updates
    waitOnFlip = False
    if Opac_less.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Opac_less.frameNStart = frameN  # exact frame index
        Opac_less.tStart = t  # local t and not account for scr refresh
        Opac_less.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Opac_less, 'tStartRefresh')  # time at next scr refresh
        Opac_less.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Opac_less.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Opac_less.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Opac_less.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Opac_less.tStartRefresh + timer-frameTolerance:
            # keep track of stop time/frame for later
            Opac_less.tStop = t  # not accounting for scr refresh
            Opac_less.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Opac_less, 'tStopRefresh')  # time at next scr refresh
            Opac_less.setAutoDraw(False)    
    if Opac_less.status == STARTED and not waitOnFlip:
        theseKeys = Opac_less.getKeys(keyList=['left'], waitRelease=False)
        _Opac_less_allKeys.extend(theseKeys)
        if len(theseKeys)!=0:
            Rec_M.opacity+=-0.1
        if len(_Opac_less_allKeys):
            Opac_less.keys = _Opac_less_allKeys[-1].name  # just the last key pressed
            Opac_less.rt = _Opac_less_allKeys[-1].rt
            # a response ends the routine
#continueRoutine = False
    

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
thisExp.addData('Rec_D.started', Rec_D.tStartRefresh)
thisExp.addData('Rec_D.stopped', Rec_D.tStopRefresh)
# check responses
if Opac_more.keys in ['', [], None]:  # No response was made
    Opac_more.keys = None
thisExp.addData('Opac_more.keys',Opac_more.keys)
if Opac_more.keys != None:  # we had a response
    thisExp.addData('Opac_more.rt', Opac_more.rt)
thisExp.addData('Opac_more.started', Opac_more.tStartRefresh)
thisExp.addData('Opac_more.stopped', Opac_more.tStopRefresh)
thisExp.nextEntry()
# check responses
if Opac_less.keys in ['', [], None]:  # No response was made
    Opac_less.keys = None
thisExp.addData('Opac_less.keys',Opac_less.keys)
if Opac_less.keys != None:  # we had a response
    thisExp.addData('Opac_less.rt', Opac_less.rt)
thisExp.addData('Opac_less.started', Opac_less.tStartRefresh)
thisExp.addData('Opac_less.stopped', Opac_less.tStopRefresh)
thisExp.nextEntry()
# the Routine "Trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
