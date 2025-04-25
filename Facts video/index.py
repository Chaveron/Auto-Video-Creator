import pyautogui
import time
import json
#

# dataCollected = False
Joke = []
import threading
import keyboard
import signal
import os
import math
import random

# Note!! Changes the pixels locations according to your screen
MicrosoftEdgeTab = {"x":994,"y":1048}
Copilotopen = {"x":747,"y":873}
Copilotcopycode = {"x":1518,"y":465}
VSCodeopen = {"x":1380,"y":1054}

Jokepaste = {"x":432,"y":269}
Donechange = {"x":530,"y":245}
CodeRunner = {"x":1807,"y":63}
Copilot = {"x":290,"y":15}
FileExplorer = {"x":1129,"y":1050}
ImageCreatoropen = {"x":611,"y":17}
ImageCreatorprompt = {"x":435,"y":338}
ImageCreatorimage = {"x":890,"y":579}
ImageCreatorimagesave = {"x":997,"y":653}
ImageCreatorDesktop = {"x":265,"y":69}
ImageCreatorAutoVideoCreator = {"x":288,"y":234}
ImageCreatorimageImages = {"x":277,"y":193}
ImageCreatorimageName = {"x":305,"y":413}
AutoVideoCreatoropen = {"x":633,"y":70}
Imagesopen = {"x":300,"y":217}
GoLive = {"x":1828,"y":1006}
Recordingpoint = {"x":912,"y":45}
RecordingStartpoint = {"x":742,"y":173}
RecordingEndpoint = {"x":1154,"y":950}
Recordingstart = {"x":833,"y":42}
Ending = {"x":882,"y":961}
Recordingend = {"x":878,"y":38}
# Image1del = {"x":281,"y":235}
# Image2del = {"x":,"y":}
YoutubeOpen = {"x":866,"y":11}
YoutubeChannelIcon = {"x":1865,"y":176}
YoutubeSwitchAccount = {"x":1641,"y":427}
YoutubeChangeChannel = {"x":1637,"y":574}
YoutubeCreateOpen = {"x":1762,"y":178}
YoutubeUploadOpen = {"x":1694,"y":229}
YoutubeSelectFile = {"x":958,"y":721}
Videos = {"x":103,"y":404}
ScreenRecordings = {"x":428,"y":232}
Recordings = {"x":292,"y":221}
Lastlanguage = {"x":539,"y":220}
ReUseDetails = {"x":1013,"y":406}
ChooseVideoDetails = {"x":716,"y":494}
ConfirmDetails = {"x":1323,"y":913}
VideoTitle = {"x":440,"y":490}
MadeForKids = {"x":432,"y":622}
ShowMore = {"x":470,"y":741}
Next = {"x":1487,"y":912}
Public = {"x":497,"y":720}



if(len(Joke) == 0):
  print()
# MicrosoftEdge
  pyautogui.moveTo(MicrosoftEdgeTab['x'],MicrosoftEdgeTab['y'])
  time.sleep(1)
  pyautogui.leftClick()
  time.sleep(1)

# Copilot
  pyautogui.moveTo(Copilotopen['x'],Copilotopen['y'])
  time.sleep(1)
  pyautogui.leftClick()
  time.sleep(1)
  pyautogui.typewrite("#")
  time.sleep(1)
  pyautogui.hotkey('enter')
  time.sleep(10)
  pyautogui.moveTo(Copilotcopycode['x'],Copilotcopycode['y'])
  time.sleep(1)
  pyautogui.leftClick()
  time.sleep(1)
  # pyautogui.moveTo(1329,482)
  # time.sleep(1)
  # pyautogui.leftClick()
  # time.sleep(1)

# VS Code
  pyautogui.moveTo(VSCodeopen['x'],VSCodeopen['y'])
  time.sleep(1)
  pyautogui.leftClick()
  time.sleep(1)
  pyautogui.moveTo(Jokepaste['x'],Jokepaste['y'])
  time.sleep(1)
  pyautogui.leftClick()
  time.sleep(1)
  pyautogui.hotkey('ctrl', 'v')
  time.sleep(1)
  pyautogui.moveTo(CodeRunner['x'],CodeRunner['y'])
  time.sleep(1)
  pyautogui.leftClick()

else:
 print()
 with open('Joke_data.json', 'w') as json_file:
       json.dump(Joke, json_file)
# Microsoft Edge
 time.sleep(1)
 pyautogui.moveTo(MicrosoftEdgeTab['x'],MicrosoftEdgeTab['y'])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 
# Image Creator
 pyautogui.moveTo(ImageCreatoropen['x'],ImageCreatoropen['y'])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 for i in range(1, len(Joke[0])):
  pyautogui.moveTo(ImageCreatorprompt['x'],ImageCreatorprompt['y'])
  time.sleep(1)
  pyautogui.leftClick()
  time.sleep(1)
  pyautogui.hotkey('ctrl','a')
  time.sleep(1)
  pyautogui.typewrite(Joke[0][i][1])
  time.sleep(1)
  pyautogui.hotkey('enter')
  time.sleep(25)
  pyautogui.moveTo(ImageCreatorimage['x'],ImageCreatorimage['y'])
  time.sleep(1)
  pyautogui.rightClick()
  time.sleep(1)
  pyautogui.moveTo(ImageCreatorimagesave['x'],ImageCreatorimagesave['y'])
  time.sleep(1)
  pyautogui.leftClick()
  time.sleep(1) 
  pyautogui.typewrite(f"Image{i}.jpeg")
  time.sleep(3)
  pyautogui.hotkey('enter')
  time.sleep(1)

#  VS Code
 pyautogui.moveTo(VSCodeopen["x"],VSCodeopen["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(GoLive["x"],GoLive["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(3)

# Microsoft Edge
 pyautogui.hotkey('printscreen')
 time.sleep(1)
 pyautogui.moveTo(Recordingpoint["x"],Recordingpoint["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(RecordingStartpoint["x"],RecordingStartpoint["y"])
 time.sleep(1)
 pyautogui.mouseDown()
 time.sleep(1)
 pyautogui.dragTo(RecordingEndpoint["x"],RecordingEndpoint["y"],2)
 time.sleep(1)
 pyautogui.mouseUp()
 time.sleep(1)
 pyautogui.moveTo(Recordingstart["x"],Recordingstart["y"])
 time.sleep(1)
 pyautogui.doubleClick()
 time.sleep(3.3)
 with open('Recording_Started.json', 'w') as json_file:
       json.dump("Hello", json_file)
 time.sleep(5)
 End = False
#  End = False
 while(End == False):
      #  if(True):
       if(pyautogui.pixelMatchesColor(Ending["x"],Ending["y"], (0, 0, 100))):
          End = True
          pyautogui.moveTo(Recordingend["x"],Recordingend["y"])
          time.sleep(1)
          pyautogui.leftClick()
          time.sleep(1)
          pyautogui.moveTo(1455,1047)
          time.sleep(1)
          pyautogui.rightClick()
          time.sleep(1)
          pyautogui.moveTo(1388,987)
          time.sleep(1)
          pyautogui.leftClick()
          time.sleep(1)
          pyautogui.leftClick()
          time.sleep(1)
          pyautogui.hotkey('ctrl','w')
          time.sleep(1)
          # time.sleep(1)
       elif(pyautogui.pixelMatchesColor(Ending["x"],Ending["y"], (115, 115, 115))):
          print("Hello")
          pyautogui.moveTo(Recordingend["x"],Recordingend["y"])
          time.sleep(1)
          pyautogui.leftClick()
          time.sleep(1)
          os.kill(os.getpid(), signal.SIGTERM)
       else:
          time.sleep(1)
# VS Code
 pyautogui.moveTo(VSCodeopen["x"],VSCodeopen["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(GoLive["x"],GoLive["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(1509,165)
 time.sleep(1)
 pyautogui.hotkey('ctrl','z')
 time.sleep(1)
 pyautogui.moveTo(156,132)
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.hotkey('delete')
 time.sleep(1)
 pyautogui.hotkey('enter')
 time.sleep(1)
 pyautogui.moveTo(183,101)
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.typewrite('Images')
 time.sleep(1)
 pyautogui.hotkey('enter')
 time.sleep(1)
 pyautogui.moveTo(135,211)
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.hotkey('delete')
 time.sleep(1)
 pyautogui.hotkey('enter')
 time.sleep(1)
 pyautogui.moveTo(135,238)
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.hotkey('delete')
 time.sleep(1)
 pyautogui.hotkey('enter')
 time.sleep(1)
 pyautogui.moveTo(MicrosoftEdgeTab["x"],MicrosoftEdgeTab["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(YoutubeCreateOpen["x"],YoutubeCreateOpen["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(YoutubeUploadOpen["x"],YoutubeUploadOpen["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(YoutubeSelectFile["x"],YoutubeSelectFile["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(Recordings["x"],Recordings["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.hotkey('delete')
 time.sleep(1)
 pyautogui.doubleClick()
 time.sleep(10)
 pyautogui.moveTo(VideoTitle["x"],VideoTitle["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.hotkey('ctrl','a')
 time.sleep(1)
 pyautogui.typewrite(Joke[0][0][0])
 time.sleep(1)
 pyautogui.moveTo(Next["x"],Next["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(5)
 pyautogui.moveTo(1207,840)
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(Copilot["x"],Copilot["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
 pyautogui.moveTo(VSCodeopen["x"],VSCodeopen["y"])
 time.sleep(1)
 pyautogui.leftClick()
 time.sleep(1)
#  pyautogui.moveTo(CodeRunner['x'],CodeRunner['y'])
#  time.sleep(1)
#  pyautogui.leftClick()
#  time.sleep(1)