#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Mon May 11 11:28:55 2020
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
exp = sys.argv[2]
sub_dir = '../subjects/%s'%sub
matrix_file = '2-%s_matrix.csv'%exp
matrix_path  = '%s/matrix/%s'%(sub_dir, matrix_file)
order_path  = '%s/matrix/2_ordering.csv'%(sub_dir)
matrix = pd.read_csv(matrix_path)
order = pd.read_csv(order_path)
order = order.loc[int(exp)-1][1]
if str(order) == "S": thisTrial = "Scene"
elif str(order) == "O": thisTrial = "Object"
o_idx_list = matrix.loc[2]
s_idx_list = matrix.loc[3]
target_list = matrix.loc[4]

print(matrix)
print(order)
print( "* This Trial is [ %s ]"%thisTrial)
''''''''''''''''''''''''''''''''''''''''''''''''''''''
# !-2 INFO SETTING
''''''''''''''''''''''''''''''''''''''''''''''''''''''
stim_dir = 'stim/grayScale/'
nBlocks, nImgs = 12, 12

img_time = 1
dot_time = 1
trial_time = img_time+dot_time
btw_blocks_time = 12

wait_key=['s']
sub_resp_key=['d']
sig_resp_key=['s']

sub_resp_term = 0.3
sig_resp_term = 0.3

dot_size = 0.007
img_size = 0.3

s_opac = 0.3
o_opac = 0.3
''''''''''''''''''''''''''''''''''''''''''''''''''''''
# !-3 OUTPUT FILE
''''''''''''''''''''''''''''''''''''''''''''''''''''''
import csv
f = open('%s/data/2-%s_output.csv'%(sub_dir, exp), 'w', newline='')
writer=csv.writer(f)
writer.writerow(['Block', 'StimNum', 'OImg', 'SceneImg', 'Target', 'TrialStart','ImgStart', 'ImgEnd', 'SubResp', 'SigResp1', 'SigResp2'])
''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Store info about the experiment session
date = data.getDateStr()
expInfo = {
		'Date': date,
		'Participant': sub, 
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=sub)
if dlg.OK == False:
    core.quit()  # user pressed cancel

log_csv = '%s/data/log.csv'%sub_dir
log_f = open(log_csv, 'a', newline='')
log_r = csv.reader(open(log_csv,"r+"))
log_count = len(list(log_r))
session = str(log_count-1).zfill(2)

log_w=csv.writer(log_f)
log_w.writerow(['Session %s'%(session), 'Background Connectivity 2-%s'%(exp)])

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_2-%s_%s' % (sub, exp, date)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=sub, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nibey/Desktop/WorkSpace/preConn/2-SO_connectivity/structure2.py',
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

# Initialize components for Routine "Wait"

if thisTrial == 'Object':
	thisText = '물체'
else: thisText = '배경'
WaitClock = core.Clock()
wait_text = visual.TextStim(win=win, name='wait_text',
    text= '이번 시행에서는 %s 이미지에 집중해 주시고 %s 이미지가 반복되면 버튼을 눌러주세요.'%(thisText, thisText), 
    font='AppleMyungjo',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wait_resp = keyboard.Keyboard()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Object = visual.ImageStim(
    win=win,
    name='Object', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(img_size, img_size),
    color=[1,1,1], colorSpace='rgb', opacity=o_opac,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Scene = visual.ImageStim(
    win=win,
    name='Scene', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(img_size, img_size),
    color=[1,1,1], colorSpace='rgb', opacity=s_opac,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Dot = visual.Circle(
    win=win, name='Dot',
    radius=dot_size,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
sub_resp = keyboard.Keyboard()
sig_resp = keyboard.Keyboard()

# Initialize components for Routine "Rest"
RestClock = core.Clock()
sig_resp_2 = keyboard.Keyboard()

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
        
        # ------Prepare to start Routine "Trial"-------
        continueRoutine = True
        routineTimer.add(trial_time + sig_resp_term)
        # update component parameters for each repeat
        
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''
        # !-3 SET IMAGES
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''
        idx = i*12+j+1
        s_img = s_idx_list[idx]
        o_img = o_idx_list[idx]
        if thisTrial == 'Scene' and target_list[idx] ==1:
            s_img = s_idx_list[idx-1]
        if thisTrial == 'Object' and target_list[idx] ==1:
            o_img = o_idx_list[idx-1]
        s_img = '%s/scene/%i.jpg'%(stim_dir, s_img)
        o_img = '%s/object/%i.jpg'%(stim_dir, o_img)
        Object.setImage(o_img)
        Scene.setImage(s_img)
        ''''''''''''''''''''''''''''''''''''''''''''''''''''''

        sub_resp.keys = []
        sub_resp.rt = []
        _sub_resp_allKeys = []
        sig_resp.keys = []
        sig_resp.rt = []
        _sig_resp_allKeys = []
        # keep track of which components have finished
        TrialComponents = [Object, Scene, Dot, sub_resp, sig_resp]
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
            
            # *Object* updates
            if Object.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Object.frameNStart = frameN  # exact frame index
                Object.tStart = t  # local t and not account for scr refresh
                Object.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Object, 'tStartRefresh')  # time at next scr refresh
                Object.setAutoDraw(True)
            if Object.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Object.tStartRefresh + img_time-frameTolerance:
                    # keep track of stop time/frame for later
                    Object.tStop = t  # not accounting for scr refresh
                    Object.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Object, 'tStopRefresh')  # time at next scr refresh
                    Object.setAutoDraw(False)
            
            # *Scene* updates
            if Scene.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Scene.frameNStart = frameN  # exact frame index
                Scene.tStart = t  # local t and not account for scr refresh
                Scene.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Scene, 'tStartRefresh')  # time at next scr refresh
                Scene.setAutoDraw(True)
            if Scene.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Scene.tStartRefresh + img_time-frameTolerance:
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
                if tThisFlipGlobal > Dot.tStartRefresh + trial_time+sig_resp_term-frameTolerance:
                    # keep track of stop time/frame for later
                    Dot.tStop = t  # not accounting for scr refresh
                    Dot.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Dot, 'tStopRefresh')  # time at next scr refresh
                    Dot.setAutoDraw(False)
            
            # *sub_resp* updates
            Dot.fillColor=[-1,-1,-1]
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
                    Dot.fillColor=[0,0,0]

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
                if tThisFlipGlobal > sig_resp.tStartRefresh + (sig_resp_term)*2-frameTolerance:
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
        Imgs.addData('Object.started', Object.tStartRefresh)
        Imgs.addData('Object.stopped', Object.tStopRefresh)
        Imgs.addData('Scene.started', Scene.tStartRefresh)
        Imgs.addData('Scene.stopped', Scene.tStopRefresh)
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
        if type(sig_resp.rt) == float:
            sig_resp_time = trial_time-sig_resp_term+sig_resp.rt
        else: sig_resp_time = trial_time+sig_resp_term
        
        img_start, img_end = Object.tStartRefresh, Object.tStopRefresh
        dataInfo = [i, j, o_img, s_img, target_list[idx], img_start, 0, img_end-img_start,  sub_resp.rt, sig_resp_time,  []]
        writer.writerow(dataInfo)
        
    # completed 1 repeats of 'Imgs'
    
    
    # ------Prepare to start Routine "Rest"-------
    continueRoutine = True
    routineTimer.add(btw_blocks_time+sig_resp_term)
    # update component parameters for each repeat
    sig_resp_2.keys = []
    sig_resp_2.rt = []
    _sig_resp_2_allKeys = []
    # keep track of which components have finished
    RestComponents = [Dot, sig_resp_2]
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
            if tThisFlipGlobal > Dot.tStartRefresh + (btw_blocks_time)-frameTolerance:
                # keep track of stop time/frame for later
                Dot.tStop = t  # not accounting for scr refresh
                Dot.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Dot, 'tStopRefresh')  # time at next scr refresh
                Dot.setAutoDraw(False)
        
        # *sig_resp_2* updates
        waitOnFlip = False
        if sig_resp_2.status == NOT_STARTED and tThisFlip >= (btw_blocks_time-sig_resp_term)-frameTolerance:
            # keep track of start time/frame for later
            sig_resp_2.frameNStart = frameN  # exact frame index
            sig_resp_2.tStart = t  # local t and not account for scr refresh
            sig_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sig_resp_2, 'tStartRefresh')  # time at next scr refresh
            sig_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sig_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sig_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sig_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sig_resp_2.tStartRefresh + (sig_resp_term*2)-frameTolerance:
                # keep track of stop time/frame for later
                sig_resp_2.tStop = t  # not accounting for scr refresh
                sig_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sig_resp_2, 'tStopRefresh')  # time at next scr refresh
                sig_resp_2.status = FINISHED
        if sig_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = sig_resp_2.getKeys(keyList=sig_resp_key, waitRelease=False)
            _sig_resp_2_allKeys.extend(theseKeys)
            if len(_sig_resp_2_allKeys):
                sig_resp_2.keys = _sig_resp_2_allKeys[-1].name  # just the last key pressed
                sig_resp_2.rt = _sig_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    Blocks.addData('Dot.started', Dot.tStartRefresh)
    Blocks.addData('Dot.stopped', Dot.tStopRefresh)
    # check responses
    if sig_resp_2.keys in ['', [], None]:  # No response was made
        sig_resp_2.keys = None
    Blocks.addData('sig_resp_2.keys',sig_resp_2.keys)
    if sig_resp_2.keys != None:  # we had a response
        Blocks.addData('sig_resp_2.rt', sig_resp_2.rt)
    Blocks.addData('sig_resp_2.started', sig_resp_2.tStartRefresh)
    Blocks.addData('sig_resp_2.stopped', sig_resp_2.tStopRefresh)

    dataInfo = [[],[],[],[],[], Dot.tStartRefresh, 0, Dot.tStopRefresh, [], [], sig_resp_2.rt]
    writer.writerow(dataInfo)

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
