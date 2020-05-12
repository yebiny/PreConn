#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Mon May 11 14:34:54 2020
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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

''''''''''''''''''''''''''''''''''''''''''''''''''''''
# !-1 PERSONAL MATIRIX
''''''''''''''''''''''''''''''''''''''''''''''''''''''
import pandas as pd
sub = sys.argv[1]
sub_dir = '../subjects/%s'%sub
matrix_path = '%s/matrix/1_matrix.csv'%(sub_dir)
matrix = pd.read_csv(matrix_path)
category_list = matrix.loc[2]
idx_list = matrix.loc[3]
target_list = matrix.loc[4]
print(matrix)
''''''''''''''''''''''''''''''''''''''''''''''''''''''
# !-2 INFO SETTING
''''''''''''''''''''''''''''''''''''''''''''''''''''''
nBlocks, nImgs = 12, 12
stim_categories=['face', 'scene', 'object']

img_time = 1
dot_time = 1
trial_time = img_time+dot_time
btw_blocks_time = 12

welcome_key=['space']
wait_key=['s']
sig_resp_key=['s']
sub_resp_key=['c']

sub_resp_term = 0.3
sig_resp_term = 0.3

dot_size = 0.007
img_size = 0.3
opacity = 0.3
''''''''''''''''''''''''''''''''''''''''''''''''''''''
# !-3 OUTPUT FILE
''''''''''''''''''''''''''''''''''''''''''''''''''''''
import csv
f = open('%s/data/1_output.csv'%(sub_dir), 'w', newline='')
writer=csv.writer(f)
writer.writerow(['Block', 'StimNum', 'Img', 'Target', 'Trial Start', 'Trial End', 'SubResp', 'SigResp1', 'SigResp2'])
''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nibey/Desktop/WorkSpace/preConn/1-FSO_localizer/structure2.py',
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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Welcome!\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_resp = keyboard.Keyboard()

# Initialize components for Routine "Wait"
WaitClock = core.Clock()
wait_text = visual.TextStim(win=win, name='wait_text',
    text='Waiting\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wait_resp = keyboard.Keyboard()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Image = visual.ImageStim(
    win=win,
    name='Image', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(img_size, img_size),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Dot = visual.Circle(
    win=win, name='Dot',
    radius=dot_size,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
sub_resp = keyboard.Keyboard()
sig_resp = keyboard.Keyboard()

# Initialize components for Routine "Rest"
TermClock = core.Clock()
rest_resp= keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_resp.keys = []
welcome_resp.rt = []
_welcome_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [welcome_text, welcome_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *welcome_resp* updates
    waitOnFlip = False
    if welcome_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.tStart = t  # local t and not account for scr refresh
        welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
        welcome_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_resp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_resp.getKeys(keyList=welcome_key, waitRelease=False)
        _welcome_resp_allKeys.extend(theseKeys)
        if len(_welcome_resp_allKeys):
            welcome_resp.keys = _welcome_resp_allKeys[-1].name  # just the last key pressed
            welcome_resp.rt = _welcome_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)
# check responses
if welcome_resp.keys in ['', [], None]:  # No response was made
    welcome_resp.keys = None
thisExp.addData('welcome_resp.keys',welcome_resp.keys)
if welcome_resp.keys != None:  # we had a response
    thisExp.addData('welcome_resp.rt', welcome_resp.rt)
thisExp.addData('welcome_resp.started', welcome_resp.tStartRefresh)
thisExp.addData('welcome_resp.stopped', welcome_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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

# set up handler to look after randomisation of conditions etc
Blocks = data.TrialHandler(nReps=nBlocks, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Blocks')
thisExp.addLoop(Blocks)  # add the loop to the experiment
thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for i, thisBlock in zip(range(nBlocks), Blocks):
    currentLoop = Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Imgs = data.TrialHandler(nReps=nImgs, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Imgs')
    thisExp.addLoop(Imgs)  # add the loop to the experiment
    thisImg = Imgs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisImg.rgb)
    if thisImg != None:
        for paramName in thisImg:
            exec('{} = thisImg[paramName]'.format(paramName))
    
    for j, thisImg in zip(range(nImgs), Imgs):
        currentLoop = Imgs
        # abbreviate parameter names if possible (e.g. rgb = thisImg.rgb)
        if thisImg != None:
            for paramName in thisImg:
                exec('{} = thisImg[paramName]'.format(paramName))
        
		# !-4.
        idx = i*12+j+1
        if target_list[idx] == 1:
            img_idx= int(idx_list[idx-1])
        else: img_idx = int(idx_list[idx])

        stim_category = stim_categories[int(category_list[idx])-1]
        this_img = './stim/%s/%i.jpg'%(stim_category, img_idx)
        Image.setImage(this_img)

        # ------Prepare to start Routine "Trial"-------
        continueRoutine = True
        routineTimer.add(trial_time+sig_resp_term)
        # update component parameters for each repeat
        sub_resp.keys = []
        sub_resp.rt = []
        _sub_resp_allKeys = []
        sig_resp.keys = []
        sig_resp.rt = []
        _sig_resp_allKeys = []
        # keep track of which components have finished
        TrialComponents = [Image, Dot, sub_resp, sig_resp]
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
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Image* updates
            if Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Image.frameNStart = frameN  # exact frame index
                Image.tStart = t  # local t and not account for scr refresh
                Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Image, 'tStartRefresh')  # time at next scr refresh
                Image.setAutoDraw(True)
            if Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Image.tStartRefresh + img_time-frameTolerance:
                    # keep track of stop time/frame for later
                    Image.tStop = t  # not accounting for scr refresh
                    Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Image, 'tStopRefresh')  # time at next scr refresh
                    Image.setAutoDraw(False)
            
            # *Dot* updates
            if Dot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Dot.frameNStart = frameN  # exact frame index
                Dot.tStart = t  # local t and not account for scr refresh
                Dot.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Dot, 'tStartRefresh')  # time at next scr refresh
                Dot.setAutoDraw(True)
            if Dot.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Dot.tStartRefresh + (trial_time+sig_resp_term)-frameTolerance:
                    # keep track of stop time/frame for later
                    Dot.tStop = t  # not accounting for scr refresh
                    Dot.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Dot, 'tStopRefresh')  # time at next scr refresh
                    Dot.setAutoDraw(False)
           
            # !-4 DOT Fill COLOR SETTING
            Dot.fillColor = [-1,-1,-1]
            # *sub_resp* updates
            waitOnFlip = False
            if sub_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sub_resp.frameNStart = frameN  # exact frame index
                sub_resp.tStart = t  # local t and not account for scr refresh
                sub_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sub_resp, 'tStartRefresh')  # time at next scr refresh
                sub_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(sub_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(sub_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if sub_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sub_resp.tStartRefresh + (img_time+sub_resp_term)-frameTolerance:
                    # keep track of stop time/frame for later
                    sub_resp.tStop = t  # not accounting for scr refresh
                    sub_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sub_resp, 'tStopRefresh')  # time at next scr refresh
                    sub_resp.status = FINISHED
            if sub_resp.status == STARTED and not waitOnFlip:
                theseKeys = sub_resp.getKeys(keyList=sub_resp_key, waitRelease=False)
                _sub_resp_allKeys.extend(theseKeys)
                if len(_sub_resp_allKeys):
                    sub_resp.keys = _sub_resp_allKeys[-1].name  # just the last key pressed
                    sub_resp.rt = _sub_resp_allKeys[-1].rt
                    Dot.fillColor = [0,0,0]
            # *sig_resp* updates
            waitOnFlip = False
            if sig_resp.status == NOT_STARTED and tThisFlip >= (trial_time-sig_resp_term)-frameTolerance:
                # keep track of start time/frame for later
                sig_resp.frameNStart = frameN  # exact frame index
                sig_resp.tStart = t  # local t and not account for scr refresh
                sig_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sig_resp, 'tStartRefresh')  # time at next scr refresh
                sig_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(sig_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(sig_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if sig_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sig_resp.tStartRefresh + (sig_resp_term*2)-frameTolerance:
                    # keep track of stop time/frame for later
                    sig_resp.tStop = t  # not accounting for scr refresh
                    sig_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sig_resp, 'tStopRefresh')  # time at next scr refresh
                    sig_resp.status = FINISHED
            if sig_resp.status == STARTED and not waitOnFlip:
                theseKeys = sig_resp.getKeys(keyList=sig_resp_key, waitRelease=False)
                _sig_resp_allKeys.extend(theseKeys)
                if len(_sig_resp_allKeys):
                    sig_resp.keys = _sig_resp_allKeys[-1].name  # just the last key pressed
                    sig_resp.rt = _sig_resp_allKeys[-1].rt
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
        Imgs.addData('Image.started', Image.tStartRefresh)
        Imgs.addData('Image.stopped', Image.tStopRefresh)
        Imgs.addData('Dot.started', Dot.tStartRefresh)
        Imgs.addData('Dot.stopped', Dot.tStopRefresh)
        # check responses
        if sub_resp.keys in ['', [], None]:  # No response was made
            sub_resp.keys = None
        Imgs.addData('sub_resp.keys',sub_resp.keys)
        if sub_resp.keys != None:  # we had a response
            Imgs.addData('sub_resp.rt', sub_resp.rt)
        Imgs.addData('sub_resp.started', sub_resp.tStartRefresh)
        Imgs.addData('sub_resp.stopped', sub_resp.tStopRefresh)
        # check responses
        if sig_resp.keys in ['', [], None]:  # No response was made
            sig_resp.keys = None
        Imgs.addData('sig_resp.keys',sig_resp.keys)
        if sig_resp.keys != None:  # we had a response
            Imgs.addData('sig_resp.rt', sig_resp.rt)
        Imgs.addData('sig_resp.started', sig_resp.tStartRefresh)
        Imgs.addData('sig_resp.stopped', sig_resp.tStopRefresh)
        thisExp.nextEntry()
        
        # !-
        dataInfo = [i, j, this_img, target_list[idx], Image.tStartRefresh, Image.tStopRefresh, sub_resp.rt, sig_resp.rt, []]
        writer.writerow(dataInfo)
    # completed 5 repeats of 'Imgs'
    
    
    # ------Prepare to start Routine "Term"-------
    continueRoutine = True
    routineTimer.add(btw_blocks_time+sig_resp_term)
    # update component parameters for each repeat
    rest_resp.keys = []
    rest_resp.rt = []
    _rest_resp_allKeys = []
    # keep track of which components have finished
    TermComponents = [Dot, rest_resp]
    for thisComponent in TermComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TermClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Term"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TermClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TermClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Dot* updates
        if Dot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Dot.frameNStart = frameN  # exact frame index
            Dot.tStart = t  # local t and not account for scr refresh
            Dot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Dot, 'tStartRefresh')  # time at next scr refresh
            Dot.setAutoDraw(True)
        if Dot.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Dot.tStartRefresh + btw_blocks_time-frameTolerance:
                # keep track of stop time/frame for later
                Dot.tStop = t  # not accounting for scr refresh
                Dot.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Dot, 'tStopRefresh')  # time at next scr refresh
                Dot.setAutoDraw(False)
        
        # *rest_resp* updates
        waitOnFlip = False
        if rest_resp.status == NOT_STARTED and tThisFlip >= (btw_blocks_time-sig_resp_term)-frameTolerance:
            # keep track of start time/frame for later
            rest_resp.frameNStart = frameN  # exact frame index
            rest_resp.tStart = t  # local t and not account for scr refresh
            rest_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_resp, 'tStartRefresh')  # time at next scr refresh
            rest_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rest_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rest_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rest_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_resp.tStartRefresh + (sig_resp_term*2)-frameTolerance:
                # keep track of stop time/frame for later
                rest_resp.tStop = t  # not accounting for scr refresh
                rest_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_resp, 'tStopRefresh')  # time at next scr refresh
                rest_resp.status = FINISHED
        if rest_resp.status == STARTED and not waitOnFlip:
            theseKeys = rest_resp.getKeys(keyList=sig_resp_key, waitRelease=False)
            _rest_resp_allKeys.extend(theseKeys)
            if len(_rest_resp_allKeys):
                rest_resp.keys = _rest_resp_allKeys[-1].name  # just the last key pressed
                rest_resp.rt = _rest_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TermComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Term"-------
    for thisComponent in TermComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Blocks.addData('Dot.started', Dot.tStartRefresh)
    Blocks.addData('Dot.stopped', Dot.tStopRefresh)
    # check responses
    if rest_resp.keys in ['', [], None]:  # No response was made
        rest_resp.keys = None
    Blocks.addData('rest_resp.keys',rest_resp.keys)
    if rest_resp.keys != None:  # we had a response
        Blocks.addData('rest_resp.rt', rest_resp.rt)
    Blocks.addData('rest_resp.started', rest_resp.tStartRefresh)
    Blocks.addData('rest_resp.stopped', rest_resp.tStopRefresh)
    thisExp.nextEntry()
    
    # !-
    dataInfo = ['TERM', [], [], [], Dot.tStartRefresh, Dot.tStopRefresh, [], [], rest_resp.rt]
    writer.writerow(dataInfo)
# completed 1 repeats of 'Blocks'


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
