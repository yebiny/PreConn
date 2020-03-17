#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.0),
    on Mon Mar  9 11:35:02 2020
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

# Store info about the experiment session
psychopyVersion = '2020.1.0'
expName = 'transparent'  # from the Builder filename that created this script
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
    originPath='/Users/nibey/Desktop/psycopy_ex/trp_ex/transparent.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation
window_size = (2560, 1440)
#window_size = (1024, 768 )

# Setup the Window
win = visual.Window(
    size=window_size, fullscr=True, screen=0, 
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

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Welcome!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_key = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
rest_polygon = visual.Circle(
    win=win, name='rest_polygon',
    radius=0.007,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
rest_text = visual.TextStim(win=win, name='rest_text',
    text='Start soon\n\n\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
face = visual.ImageStim(
    win=win,
    name='face', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
scene = visual.ImageStim(
    win=win,
    name='scene', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=0.2,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
polygon = visual.Circle(
    win=win, name='polygon',
    radius=0.007,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_key.keys = []
welcome_key.rt = []
_welcome_key_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_text, welcome_key]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
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
        if tThisFlipGlobal > welcome_text.tStartRefresh + 100.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_text.tStop = t  # not accounting for scr refresh
            welcome_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome_text, 'tStopRefresh')  # time at next scr refresh
            welcome_text.setAutoDraw(False)
    
    # *welcome_key* updates
    waitOnFlip = False
    if welcome_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_key.frameNStart = frameN  # exact frame index
        welcome_key.tStart = t  # local t and not account for scr refresh
        welcome_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_key, 'tStartRefresh')  # time at next scr refresh
        welcome_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_key.status == STARTED and not waitOnFlip:
        theseKeys = welcome_key.getKeys(keyList=['space'], waitRelease=False)
        _welcome_key_allKeys.extend(theseKeys)
        if len(_welcome_key_allKeys):
            welcome_key.keys = _welcome_key_allKeys[-1].name  # just the last key pressed
            welcome_key.rt = _welcome_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)
# check responses
if welcome_key.keys in ['', [], None]:  # No response was made
    welcome_key.keys = None
thisExp.addData('welcome_key.keys',welcome_key.keys)
if welcome_key.keys != None:  # we had a response
    thisExp.addData('welcome_key.rt', welcome_key.rt)
thisExp.addData('welcome_key.started', welcome_key.tStartRefresh)
thisExp.addData('welcome_key.stopped', welcome_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Trial = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('files/rowlist.csv'),
    seed=None, name='Trial')
thisExp.addLoop(Trial)  # add the loop to the experiment
thisTrial = Trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

###################### Random image ########################
import random
def select_random_number():
  while True:
    num_overlap_list = [1,2,2,2,3,3]
    overlap_list = random.sample(range(1,11),random.choice(num_overlap_list))
    if len(overlap_list) == 2:
      if abs(overlap_list[0]-overlap_list[1]) > 1:
        return overlap_list
        break
    elif len(overlap_list) == 3:
      if abs(overlap_list[0]-overlap_list[1]) > 1 and abs(overlap_list[0]-overlap_list[2]) > 1 and abs(overlap_list[1]-overlap_list[2]) > 1:
        return overlap_list
        break
    else:
      return overlap_list
      break

Trial_overlap_list = []
for i in range(12): Trial_overlap_list.append(select_random_number())
Trial_subject_list = []
for i in range(6): Trial_subject_list.append("Face_Trial")
for i in range(6): Trial_subject_list.append("Scene_Trial")
random.shuffle(Trial_subject_list)

############################################################

for i, thisTrial in zip(range(12), Trial):
    print("This is ", Trial_subject_list[i])
    print("Overlaped imgs are : ", Trial_overlap_list[i])
    currentLoop = Trial
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    routineTimer.add(18.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    rest_text.text = "This is "+Trial_subject_list[i]+"\n\n\n\n"
    restComponents = [rest_polygon, rest_text]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_polygon* updates
        if rest_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_polygon.frameNStart = frameN  # exact frame index
            rest_polygon.tStart = t  # local t and not account for scr refresh
            rest_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_polygon, 'tStartRefresh')  # time at next scr refresh
            rest_polygon.setAutoDraw(True)
        if rest_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_polygon.tStartRefresh + 18.0-frameTolerance:
                # keep track of stop time/frame for later
                rest_polygon.tStop = t  # not accounting for scr refresh
                rest_polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_polygon, 'tStopRefresh')  # time at next scr refresh
                rest_polygon.setAutoDraw(False)
        
        # *rest_text* updates
        if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_text.frameNStart = frameN  # exact frame index
            rest_text.tStart = t  # local t and not account for scr refresh
            rest_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
            rest_text.setAutoDraw(True)
        if rest_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_text.tStartRefresh + 18.0-frameTolerance:
                # keep track of stop time/frame for later
                rest_text.tStop = t  # not accounting for scr refresh
                rest_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_text, 'tStopRefresh')  # time at next scr refresh
                rest_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trial.addData('rest_polygon.started', rest_polygon.tStartRefresh)
    Trial.addData('rest_polygon.stopped', rest_polygon.tStopRefresh)
    Trial.addData('rest_text.started', rest_text.tStartRefresh)
    Trial.addData('rest_text.stopped', rest_text.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    Block = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('files/imglist.csv', selection=row),
        seed=None, name='Block')
    thisExp.addLoop(Block)  # add the loop to the experiment
    thisBlock = Block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    for j, thisBlock in zip(range(12), Block):
        currentLoop = Block
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
              if Trial_subject_list[i] == "Face_Trial":
                if paramName == "face_image" and j in Trial_overlap_list[i]:
                  print("skip")
                else: exec('{} = thisBlock[paramName]'.format(paramName))
              elif Trial_subject_list[i] == "Scene_Trial":
                if paramName == "scene_image" and j in Trial_overlap_list[i]:
                  print("skip")
                else: exec('{} = thisBlock[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        face.setImage(face_image)
        scene.setImage(scene_image)
        key.keys = []
        key.rt = []
        _key_allKeys = []
        # keep track of which components have finished
        trialComponents = [face, scene, polygon, key]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *face* updates
            if face.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                face.frameNStart = frameN  # exact frame index
                face.tStart = t  # local t and not account for scr refresh
                face.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(face, 'tStartRefresh')  # time at next scr refresh
                face.setAutoDraw(True)
            if face.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > face.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    face.tStop = t  # not accounting for scr refresh
                    face.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(face, 'tStopRefresh')  # time at next scr refresh
                    face.setAutoDraw(False)
            
            # *scene* updates
            if scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                scene.frameNStart = frameN  # exact frame index
                scene.tStart = t  # local t and not account for scr refresh
                scene.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(scene, 'tStartRefresh')  # time at next scr refresh
                scene.setAutoDraw(True)
            if scene.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > scene.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    scene.tStop = t  # not accounting for scr refresh
                    scene.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(scene, 'tStopRefresh')  # time at next scr refresh
                    scene.setAutoDraw(False)
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # *key* updates
            waitOnFlip = False
            if key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key.frameNStart = frameN  # exact frame index
                key.tStart = t  # local t and not account for scr refresh
                key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key, 'tStartRefresh')  # time at next scr refresh
                key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key.clock.reset)  # t=0 on next screen flip
            if key.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    key.tStop = t  # not accounting for scr refresh
                    key.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key, 'tStopRefresh')  # time at next scr refresh
                    key.status = FINISHED
            if key.status == STARTED and not waitOnFlip:
                theseKeys = key.getKeys(keyList=['space'], waitRelease=False)
                _key_allKeys.extend(theseKeys)
                if len(_key_allKeys):
                    key.keys = _key_allKeys[-1].name  # just the last key pressed
                    key.rt = _key_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Block.addData('face.started', face.tStartRefresh)
        Block.addData('face.stopped', face.tStopRefresh)
        Block.addData('scene.started', scene.tStartRefresh)
        Block.addData('scene.stopped', scene.tStopRefresh)
        Block.addData('polygon.started', polygon.tStartRefresh)
        Block.addData('polygon.stopped', polygon.tStopRefresh)
        # check responses
        if key.keys in ['', [], None]:  # No response was made
            key.keys = None
        Block.addData('key.keys',key.keys)
        if key.keys != None:  # we had a response
            Block.addData('key.rt', key.rt)
        Block.addData('key.started', key.tStartRefresh)
        Block.addData('key.stopped', key.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Block'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'Trial'


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
