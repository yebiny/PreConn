#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.0),
    on Fri Mar 27 13:52:51 2020
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
import pandas as pd
from psychopy.hardware import keyboard


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)


sub = sys.argv[1]
sub_dir = '../subjects/%s'%sub
matrix_file = '1_matrix.csv'
matrix_path  = '%s/matrix/%s'%(sub_dir, matrix_file)

matrix = pd.read_csv(matrix_path)
print("* Load Personal Matrix From [%s]"%(matrix_path))
print(matrix)

category_list= matrix.loc[2]
idx_list = matrix.loc[3]
target_list = matrix.loc[4]
# o_list for object images
o_list=[]
for f in os.listdir('./stim/object/'):
    o_list.append(f)

# Store info about the experiment session
psychopyVersion = '2020.1.0'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename ='%s/data/exp_1_%s' % (sub_dir,expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nibey/WorkSpace/preConn/1-FSO_roi/test.py',
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
    ori=0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Resp = keyboard.Keyboard()
Dot = visual.Circle(
    win=win, name='Dot',
    radius=0.007,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "Rest"
RestClock = core.Clock()
rest_dot = visual.Circle(
    win=win, name='rest_dot',
    radius=0.007,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

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
        theseKeys = welcome_resp.getKeys(keyList=['space'], waitRelease=False)
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
        theseKeys = wait_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
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


nBlocks = 12
nImages = 12
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
    print("This is ", i+1, "th Block")
    currentLoop = Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Imgs = data.TrialHandler(nReps=nImages, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Imgs')
    thisExp.addLoop(Imgs)  # add the loop to the experiment
    thisImg = Imgs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisImg.rgb)
    if thisImg != None:
        for paramName in thisImg:
            exec('{} = thisImg[paramName]'.format(paramName))
    
    for j,  thisImg in zip(range(nImages), Imgs):
        idx = i*12+j+1
        
        currentLoop = Imgs
        # abbreviate parameter names if possible (e.g. rgb = thisImg.rgb)
        if thisImg != None:
            for paramName in thisImg:
                exec('{} = thisImg[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Trial"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        
        if target_list[idx] == 1:
            img_idx = int(idx_list[idx-1])
        else: img_idx = int(idx_list[idx])
        
        if category_list[idx] == 1:
            img_dir = './stim/face/face_'
            this_img = img_dir+str(img_idx)
        elif category_list[idx] == 2:
            img_dir = './stim/scene/scene_'
            this_img = img_dir+str(img_idx)
        elif category_list[idx] == 3:
            img_dir = './stim/object/'
            this_img = img_dir+o_list[img_idx]
	
        print(this_img, 'is target? ', int(target_list[idx]))
        Image.setImage(this_img)
        
        Resp.keys = []
        Resp.rt = []
        _Resp_allKeys = []
        # keep track of which components have finished
        TrialComponents = [Image, Resp, Dot]
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
            Dot.fillColor=[-1,-1,-1]
            if Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Image.frameNStart = frameN  # exact frame index
                Image.tStart = t  # local t and not account for scr refresh
                Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Image, 'tStartRefresh')  # time at next scr refresh
                Image.setAutoDraw(True)
            if Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Image.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Image.tStop = t  # not accounting for scr refresh
                    Image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Image, 'tStopRefresh')  # time at next scr refresh
                    Image.setAutoDraw(False)
            
            # *Resp* updates
            waitOnFlip = False
            if Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Resp.frameNStart = frameN  # exact frame index
                Resp.tStart = t  # local t and not account for scr refresh
                Resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Resp, 'tStartRefresh')  # time at next scr refresh
                Resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Resp.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Resp.tStop = t  # not accounting for scr refresh
                    Resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Resp, 'tStopRefresh')  # time at next scr refresh
                    Resp.status = FINISHED
            if Resp.status == STARTED and not waitOnFlip:
                theseKeys = Resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
                _Resp_allKeys.extend(theseKeys)
                if len(_Resp_allKeys):
                    Dot.fillColor=[0,0,0]
                    Resp.keys = _Resp_allKeys[-1].name  # just the last key pressed
                    Resp.rt = _Resp_allKeys[-1].rt
            
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
                if tThisFlipGlobal > Dot.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Dot.tStop = t  # not accounting for scr refresh
                    Dot.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Dot, 'tStopRefresh')  # time at next scr refresh
                    Dot.setAutoDraw(False)
            
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
        # check responses
        if Resp.keys in ['', [], None]:  # No response was made
            Resp.keys = None
        Imgs.addData('Resp.keys',Resp.keys)
        if Resp.keys != None:  # we had a response
            Imgs.addData('Resp.rt', Resp.rt)
        Imgs.addData('Resp.started', Resp.tStartRefresh)
        Imgs.addData('Resp.stopped', Resp.tStopRefresh)
        Imgs.addData('Dot.started', Dot.tStartRefresh)
        Imgs.addData('Dot.stopped', Dot.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 12 repeats of 'Imgs'
    
    
    # ------Prepare to start Routine "Rest"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    RestComponents = [rest_dot]
    for thisComponent in RestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = RestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_dot* updates
        if rest_dot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_dot.frameNStart = frameN  # exact frame index
            rest_dot.tStart = t  # local t and not account for scr refresh
            rest_dot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_dot, 'tStartRefresh')  # time at next scr refresh
            rest_dot.setAutoDraw(True)
        if rest_dot.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_dot.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                rest_dot.tStop = t  # not accounting for scr refresh
                rest_dot.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_dot, 'tStopRefresh')  # time at next scr refresh
                rest_dot.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rest"-------
    for thisComponent in RestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Blocks.addData('rest_dot.started', rest_dot.tStartRefresh)
    Blocks.addData('rest_dot.stopped', rest_dot.tStopRefresh)
    thisExp.nextEntry()
    
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
