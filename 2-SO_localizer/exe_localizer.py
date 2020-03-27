#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Thu Mar 26 14:24:39 2020
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
exp = sys.argv[2]
sub_dir = '../subjects/%s'%sub
matrix_file = '2-%s_matrix.csv'%exp
matrix_path  = '%s/matrix/%s'%(sub_dir, matrix_file)
order_path  = '%s/matrix/2_ordering.csv'%(sub_dir)

matrix = pd.read_csv(matrix_path)
print("* Load Personal Matrix From [%s]"%(matrix_path))
print(matrix)

order = pd.read_csv(order_path)
print("* Load Ordering Matrix From [%s]"%(order_path))
print(order)

order = order.loc[int(exp)-1][1]
if str(order) == "S": thisTrial = "Scene"
elif str(order) == "O": thisTrial = "Object"
else: print("ERROR!!!!!!!!")

print( "* This Trial is [ %s ]"%thisTrial)

f_img_dir = './stim/face/'
s_img_dir = './stim/scene/'
f_idx_list = matrix.loc[2]
s_idx_list = matrix.loc[3]	
target_ness = matrix.loc[4]

nBlock = 12
nStim = 12

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'exp_2-%s'%(exp)  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = '%s/data/%s_%s_%s' % (sub_dir, expName, expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nibey/WorkSpace/preConn/2-SO_localizer/test.py',
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
    text='Welcome !',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_resp = keyboard.Keyboard()

# Initialize components for Routine "Wait"
WaitClock = core.Clock()
wait_text = visual.TextStim(win=win, name='wait_text',
    text='This is %s Trial. Focus on %s Image! '%(thisTrial,thisTrial),
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wait_resp = keyboard.Keyboard()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Face = visual.ImageStim(
    win=win,
    name='Face', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Scene = visual.ImageStim(
    win=win,
    name='Scene', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=0.4,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Dot = visual.Circle(
    win=win, name='Dot',
    radius=(0.007),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
Resp = keyboard.Keyboard()

# Initialize components for Routine "Rest"
RestClock = core.Clock()
rest_dot = visual.Circle(
    win=win, name='rest_dot',
    radius=(0.007),
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
    if welcome_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_text.tStartRefresh + 12-frameTolerance:
            # keep track of stop time/frame for later
            welcome_text.tStop = t  # not accounting for scr refresh
            welcome_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_text, 'tStopRefresh')  # time at next scr refresh
            welcome_text.setAutoDraw(False)
    
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
        theseKeys = wait_resp.getKeys(keyList=['space'], waitRelease=False)
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
Blocks = data.TrialHandler(nReps=nBlock, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Blocks')
thisExp.addLoop(Blocks)  # add the loop to the experiment
thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))


for i, thisBlock in zip(range(nBlock), Blocks):
    print("This is ", i+1, "th Block")
    currentLoop = Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Imgs = data.TrialHandler(nReps=nStim, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Imgs')
    thisExp.addLoop(Imgs)  # add the loop to the experiment
    thisImg = Imgs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisImg.rgb)
    if thisImg != None:
        for paramName in thisImg:
            exec('{} = thisImg[paramName]'.format(paramName))
    
    for j, thisImg in zip(range(nStim), Imgs):
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
        f_img = f_idx_list[idx]
        s_img = s_idx_list[idx]
        if thisTrial == 'Object' and target_ness[idx] ==1:
            f_img = f_idx_list[idx-1]
            print('target')
        if thisTrial == 'Scene' and target_ness[idx] ==1:
            s_img = s_idx_list[idx-1]
            print('target')
        f_img = f_img_dir+'face_'+str(int(f_img))
        s_img = s_img_dir+'scene_'+str(int(s_img))
        print(f_img, s_img)
        Face.setImage(f_img)
        Scene.setImage(s_img)
        Resp.keys = []
        Resp.rt = []
        _Resp_allKeys = []
        # keep track of which components have finished
        TrialComponents = [Face, Scene, Dot, Resp]
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
            
            # *Face* updates
            if Face.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Face.frameNStart = frameN  # exact frame index
                Face.tStart = t  # local t and not account for scr refresh
                Face.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Face, 'tStartRefresh')  # time at next scr refresh
                Face.setAutoDraw(True)
            if Face.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Face.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Face.tStop = t  # not accounting for scr refresh
                    Face.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Face, 'tStopRefresh')  # time at next scr refresh
                    Face.setAutoDraw(False)
            
            # *Scene* updates
            Dot.fillColor=[-1, -1, -1]
            if Scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Scene.frameNStart = frameN  # exact frame index
                Scene.tStart = t  # local t and not account for scr refresh
                Scene.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Scene, 'tStartRefresh')  # time at next scr refresh
                Scene.setAutoDraw(True)
            if Scene.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Scene.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Scene.tStop = t  # not accounting for scr refresh
                    Scene.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Scene, 'tStopRefresh')  # time at next scr refresh
                    Scene.setAutoDraw(False)
            
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
                win.callOnFlip(Resp.clearEvents, eventType='keyboard')
            if Resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Resp.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Resp.tStop = t  # not accounting for scr refresh
                    Resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Resp, 'tStopRefresh')  # time at next scr refresh
                    Resp.status = FINISHED
            if Resp.status == STARTED and not waitOnFlip:
                theseKeys = Resp.getKeys(keyList=['space'], waitRelease=False)
                _Resp_allKeys.extend(theseKeys)
                if len(_Resp_allKeys):
                    Dot.fillColor=[0, 0, 0]
                    Resp.keys = _Resp_allKeys[-1].name  # just the last key pressed
                    Resp.rt = _Resp_allKeys[-1].rt
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
        Imgs.addData('Face.started', Face.tStartRefresh)
        Imgs.addData('Face.stopped', Face.tStopRefresh)
        Imgs.addData('Scene.started', Scene.tStartRefresh)
        Imgs.addData('Scene.stopped', Scene.tStopRefresh)
        Imgs.addData('Dot.started', Dot.tStartRefresh)
        Imgs.addData('Dot.stopped', Dot.tStopRefresh)
        # check responses
        if Resp.keys in ['', [], None]:  # No response was made
            Resp.keys = None
        Imgs.addData('Resp.keys',Resp.keys)
        if Resp.keys != None:  # we had a response
            Imgs.addData('Resp.rt', Resp.rt)
        Imgs.addData('Resp.started', Resp.tStartRefresh)
        Imgs.addData('Resp.stopped', Resp.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Imgs'
    
    
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
