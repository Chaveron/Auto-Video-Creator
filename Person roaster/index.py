import pyautogui
import time
import json

# lastlanguage = "English"
dataCollected = False
Joke = []
import threading
import keyboard
import signal
import os
import math
import random

def stop_on_keypress():
    keyboard.wait('alt')  # Wait until 'alt' is pressed
    print("\n[INFO] 'alt' detected! Stopping the script immediately...")
    os.kill(os.getpid(), signal.SIGTERM)  # Kill the process

# Start the listener in a separate daemon thread
threading.Thread(target=stop_on_keypress, daemon=True).start()

# Note!! Changes the pixels locations according to your screen
MicrosoftEdgeTab = {"x":1017,"y":1050}
Copilotopen = {"x":685,"y":930}
Copilotcopycode = {"x":1312,"y":505}
VSCodeopen = {"x":1457,"y":1050}
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
RecordingStartpoint = {"x":752,"y":175}
RecordingEndpoint = {"x":1165,"y":950}
Recordingstart = {"x":833,"y":42}
Ending = {"x":882,"y":961}
Recordingend = {"x":878,"y":38}
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



if(dataCollected == False):
   print()
   time.sleep(3)
#    MicrosoftEdge
   pyautogui.moveTo(MicrosoftEdgeTab['x'],MicrosoftEdgeTab['y'])
   time.sleep(1)
   pyautogui.leftClick()
   time.sleep(1)

   # ChatGPT
   pyautogui.moveTo(Copilotopen['x'],Copilotopen['y'])
   time.sleep(1)
   pyautogui.leftClick()
   time.sleep(1)
   pyautogui.typewrite(".")
   time.sleep(1)
   pyautogui.hotkey('enter')
   time.sleep(15)
   Copyfound = False
   pyautogui.moveTo(Copilotcopycode["x"],Copilotcopycode["y"])
   while(Copyfound == False):
       if(pyautogui.pixelMatchesColor(Copilotcopycode["x"],Copilotcopycode["y"],(47,45,44))):
           Copyfound = True
       else:
           pyautogui.moveTo(Copilotcopycode["x"],Copilotcopycode["y"])
           Copilotcopycode["y"] += 1
   pyautogui.leftClick()
   time.sleep(1)

   # VS Code
   pyautogui.moveTo(VSCodeopen['x'],VSCodeopen['y'])
   time.sleep(1)
   pyautogui.leftClick()
   time.sleep(1)
   pyautogui.moveTo(Donechange['x'],Donechange['y'])
   time.sleep(1)
   pyautogui.doubleClick()
   time.sleep(1)
   pyautogui.typewrite("True")
   time.sleep(1)
   pyautogui.hotkey('enter')
   time.sleep(1)
   pyautogui.moveTo(Jokepaste['x'],Jokepaste['y'])
   time.sleep(1)
   pyautogui.leftClick()
   time.sleep(1)
   pyautogui.hotkey('ctrl', 'v')
   time.sleep(1)
   pyautogui.leftClick()
   time.sleep(1)
   pyautogui.hotkey('ctrl','s')
   time.sleep(1)
   pyautogui.moveTo(CodeRunner['x'],CodeRunner['y'])
   time.sleep(1)
   pyautogui.leftClick()

# Data Collected
if(dataCollected == True):
    if (Joke[0]["language"] == "English" and Joke[0]["random_person_gender"] == "Male"):
            TotalImages = ["Barack Obama", "Bill Gates", "Cristiano Ronaldo", "Donald Trump", "Elon Musk", "Jeff Bezos", "Joe Biden", "Lionel Messi", "Neymar Jr"]
            TotalImagesEnglish = ["Barack Obama", "Bill Gates", "Cristiano Ronaldo", "Donald Trump", "Elon Musk", "Jeff Bezos", "Joe Biden", "Lionel Messi", "Neymar Jr"]
    randomnum = math.floor(random.random() * len(TotalImages))
    Name = TotalImages[randomnum]
    if(Joke[0]["language"] == "Hindi"):
            NameLan = TotalImagesHindi[randomnum]
    else:
            NameLan = TotalImagesEnglish[randomnum]
        # console.log(randomnum)
        # console.log(Name,NameLan)
        # // Use the received data to update the image
    title = Joke[0]["title"]
    titlearray = title.split(" ")
    titlearray[0] = Name
    titlenew = " ".join(titlearray)  # Corrected join syntax

    introsentence = Joke[0]["intro_sentence"]
    introsentencearray = introsentence.split(" ")
    if(Joke[0]["language"] == "English"):
     introsentencearray[0] = "One day " + NameLan
    else:
     introsentencearray[0] = "एक दिन " + NameLan
    introsentencenew = " ".join(introsentencearray)  # Corrected join syntax

    Joke[0]["intro_sentence"] = introsentencenew
    Joke[0]["title"] = titlenew
    if(Joke[0]["language"] == "English"):
      replacement_words = ["Filthy Pig","Stinking Rat","Rotten Dog","Vile Monkey","Dirty Weasel","Scabby Mutt","Slimy Snake","Gross Vulture","Lousy Hyena","Foul Crow","Creeping Cockroach","Wretched Maggot","Repulsive Slug","Abhorrent Worm","Sordid Scum","Pitiful Vermin","Disgusting Brute","Insolent Scum","Crummy Scoundrel","Loathsome Trash","Dismal Wretch","Despicable Bastard","Brainless Moron","Pitiful Imbecile","Mindless Dullard","Worthless Cretin","Pathetic Buffoon","Idiot Scum","Dumb Ass","Foolish Twit","Moronic Loser","Vile Scum","Repugnant Wretch","Grimy Slob","Nasty Slimeball","Crusty Scum","Broken Trash","Filthy Lowlife","Wretched Vermin","Disgusting Rat","Stinking Mutt","Rotten Swine","Grimy Pig","Foul Hound","Vicious Cur","Sordid Dog","Cursed Cur","Vile Stray","Scummy Mutant","Abysmal Beast","Savage Wolf","Brutal Tiger","Raging Lion","Feral Hyena","Rabid Dog","Gnarly Boar","Spiteful Jackal","Mean Donkey","Crabby Crab","Vicious Viper","Bitter Crow","Hostile Hawk","Foul-mouthed Gull","Rancid Seal","Scornful Shark","Malicious Eagle","Merciless Falcon","Pitiless Python","Ruthless Bear","Cynical Lobster","Bile-Spitting Lizard","Venomous Scorpion","Malevolent Stingray","Odious Octopus","Revolting Squid","Abominable Alligator","Hateful Crocodile","Fetid Ferret","Grotesque Goat","Insidious Snake","Horrid Opossum","Craven Weasel","Sordid Skunk","Gruesome Ferret","Loathsome Mink","Disdainful Badger","Repulsive Raccoon","Horrific Possum","Morose Mole","Sour Ferret","Gutter Rat","Scavenging Vulture","Grimy Buzzard","Noxious Magpie","Putrid Parrot","Decrepit Robin","Fallen Sparrow","Crumbled Falcon","Defiled Dove","Vile Canary","Rotting Finch","Shattered Pigeon","Broken Dove","Decaying Pigeon","Tattered Crow","Mangled Raven","Dreary Egret","Drab Swan","Stained Goose","Soiled Turkey","Sour Chicken","Foul Pheasant","Haggard Quail","Feeble Owl","Dismal Buzzard","Dank Cormorant","Rotten Heron","Fetid Kingfisher","Spoiled Parakeet","Moldy Macaw","Decayed Cockatoo","Foul-mouthed Parrot","Toxic Toucan","Poisonous Finch","Barren Sparrow","Wretched Lark","Sour Starling","Lousy Oriole","Vile Warbler","Ugly Wren","Cursed Finch","Broken Bunting","Cracked Pipit","Splintered Thrush","Shattered Robin","Rusty Redstart","Fallen Grosbeak","Worn Woodpecker","Scuffed Kingfisher","Dilapidated Jay","Cracked Crow","Crumbling Magpie","Deteriorated Chickadee","Worn Warbler","Tattered Titmouse","Damaged Dove","Shredded Finch","Frayed Canary","Ripped Raven","Fractured Falcon","Cracked Eagle","Smashed Hawk","Crumbled Osprey","Broken Kite","Splintered Kestrel","Dented Merlin","Faded Sparrowhawk","Worn Buzzard","Faded Vulture","Torn Condor","Fractured Raptor","Crushed Eagle","Damaged Osprey","Ruined Hawk","Fallen Hawk","Splintered Hawk","Cracked Owl","Battered Barn Owl","Frayed Screech Owl","Crumbling Tawny Owl","Deteriorated Snowy Owl","Worn Eagle Owl","Tattered Horned Owl","Damaged Scops Owl","Mangled Pygmy Owl","Cursed Kiwi","Sour Emu","Rotten Cassowary","Vile Ostrich","Filthy Rhea","Stinking Penguin","Scummy Albatross","Nasty Puffin","Gross Tern","Rotten Seagull","Vile Gull","Foul Pelican","Disgusting Cormorant","Rotten Booby","Noxious Frigatebird","Repulsive Shearwater","Fetid Storm Petrel","Moldy Skua","Putrid Gull","Dismal Ibis","Vile Spoonbill","Gross Flamingo","Foul Heron","Rotten Crane","Scabby Stork","Disgusting Egret","Mucky Bittern","Sordid Rail","Grimy Rail","Dirty Swallow","Stained Swift","Filthy Swift","Foul Martin","Nasty Swift","Vile Kingfisher","Rancid Roller","Putrid Motmot","Filthy Jacamar","Sour Trogon","Vile Quetzal","Stinking Parrot","Rotten Macaw","Foul Cockatoo","Nasty Lorikeet","Gross Conure","Scummy Lovebird","Filthy Budgerigar","Vile Cockatiel","Stinking Finch","Rotten Canary","Foul Parakeet","Nasty Lory","Gross Lorikeet","Scummy Parrotlet","Vile Tanager","Rotten Oriole","Foul Warbler","Nasty Wren","Gross Pipit","Scummy Snipe","Vile Sandpiper","Rotten Plover","Foul Oystercatcher","Nasty Auk","Gross Puffin","Scummy Guillemot","Vile Razorbill","Rotten Murre","Foul Guillemot","Nasty Booby","Gross Shearwater","Scummy Petrel","Vile Storm Petrel","Rotten Albatross","Foul Tern","Nasty Skua","Gross Gannet","Scummy Cormorant","Vile Anhinga","Rotten Jacana","Foul Sunbittern","Nasty Kingfisher","Gross Osprey","Scummy Falcon","Vile Harrier","Rotten Kite","Foul Buzzard","Nasty Hawk","Gross Eagle","Scummy Owl","Vile Nightjar","Rotten Swift","Foul Hummingbird","Nasty Bee","Gross Wasp","Scummy Hornet","Vile Yellowjacket","Rotten Ant","Foul Termite","Nasty Cockroach","Gross Silverfish","Scummy Moth","Vile Beetle","Rotten Earwig","Foul Spider","Nasty Tarantula","Gross Scorpion","Scummy Centipede","Vile Millipede","Rotten Worm","Foul Leech","Nasty Maggot","Gross Mite","Scummy Tick","Vile Flea","Rotten Louse","Foul Pest","Nasty Vermin","Gross Pest","Scummy Rat","Vile Mouse","Rotten Squirrel","Foul Raccoon","Nasty Possum","Gross Opossum","Scummy Skunk","Vile Ferret","Rotten Weasel","Foul Mink","Nasty Badger","Gross Mole","Scummy Shrew","Vile Hedgehog","Rotten Squirrel","Foul Chipmunk","Nasty Prairie Dog","Gross Groundhog","Scummy Rabbit","Vile Hare","Rotten Hound","Foul Cur","Nasty Mutt","Gross Dog","Scummy Pooch","Vile Canine","Rotten Wolf","Foul Coyote","Nasty Fox","Gross Jackal","Scummy Hyena","Vile Wildcat","Rotten Lion","Foul Tiger","Nasty Leopard","Gross Panther","Scummy Cougar","Vile Jaguar","Rotten Cheetah","Foul Lynx","Nasty Puma","Gross Bobcat","Scummy Serval","Vile Ocelot","Rotten Caracal","Foul Lynx","Nasty Otter","Gross Beaver","Scummy Mole","Vile Muskrat","Rotten Porcupine","Foul Hedgehog","Nasty Armadillo","Gross Sloth","Scummy Lemur","Vile Monkey","Rotten Baboon","Foul Ape","Nasty Gorilla","Gross Chimp","Scummy Orangutan","Vile Gibbon","Rotten Mandrill","Foul Marmoset","Nasty Tamarin","Gross Capuchin","Scummy Squirrel Monkey","Vile Howler","Rotten Spider Monkey","Foul Woolly Monkey","Nasty Macaque","Gross Colobus","Scummy Goral","Vile Goat","Rotten Sheep","Foul Ram","Nasty Lamb","Gross Ewe","Scummy Bull","Vile Ox","Rotten Cow","Foul Steer","Nasty Calf","Gross Buffalo","Scummy Bison","Vile Antelope","Rotten Deer","Foul Elk","Nasty Moose","Gross Caribou","Scummy Reindeer","Vile Gazelle","Rotten Impala","Foul Springbok","Nasty Wildebeest","Gross Zebu","Scummy Yak","Vile Camel","Rotten Llama","Foul Alpaca","Nasty Donkey","Gross Mule","Scummy Horse","Vile Pony","Rotten Stallion","Foul Colt","Nasty Filly","Gross Mare","Scummy Roan","Vile Appaloosa","Rotten Quarter Horse","Foul Thoroughbred","Nasty Mustang","Gross Brumby","Scummy Clydesdale","Vile Percheron","Rotten Shire","Foul Draft Horse","Nasty Draft","Gross Heavyweight","Scummy Racehorse","Vile Trackster","Rotten Winner","Foul Champion","Nasty Loser","Gross Runner","Scummy Finisher","Vile Last-place","Rotten Underdog","Foul Dreamer","Nasty Opportunist","Gross Pretender","Scummy Faker","Vile Wannabe","Rotten Reject","Foul Exile","Nasty Castaway","Gross Outcast","Scummy Misfit","Vile Pariah","Rotten Leech","Foul Parasite","Nasty Bloodsucker","Gross Tick","Scummy Louse","Vile Scavenger","Rotten Freeloader","Foul Mooch","Nasty Bum","Gross Slacker","Scummy Deadbeat","Vile Bum","Rotten Wastrel","Foul Trash","Nasty Garbage","Gross Refuse","Scummy Debris","Vile Scrap","Rotten Rubbish","Foul Junk","Nasty Clutter","Gross Litter","Scummy Waste","Vile Remnant","Rotten Residue","Foul Detritus","Nasty Fodder","Gross Rot","Scummy Decay","Vile Spoil","Rotten Garbage","Foul Scum","Nasty Sludge","Gross Gunk","Scummy Crud","Vile Muck","Rotten Filth","Foul Dirt","Nasty Soil","Gross Grime","Scummy Smudge","Vile Stain","Rotten Smear","Foul Blotch","Nasty Splotch","Gross Smudge","Scummy Mark","Vile Speck","Rotten Spot","Foul Dot","Nasty Stain","Gross Splat","Scummy Drip","Vile Dribble","Rotten Drool","Foul Slop","Nasty Crud","Gross Residue","Scummy Remnant","Vile Excrement","Rotten Feces","Foul Dung","Nasty Manure","Gross Sludge","Scummy Excreta","Vile Excretion"]





    def replace_buddy(sentence):
       words = sentence.split()  # Split sentence into words
       if "'Buddy," in words:
        index = words.index("'Buddy,")  # Find the index of 'Buddy'
        words[index] = random.choice(replacement_words)  # Replace with a random word
        return " ".join(words)  # Convert back to string

# Example usage
    Joke[0]["roast_dialogue"] = replace_buddy(Joke[0]["roast_dialogue"])
    with open('Joke_data.json', 'w') as json_file:
       json.dump(Joke, json_file)
# Microsoft Edge
    pyautogui.moveTo(MicrosoftEdgeTab['x'],MicrosoftEdgeTab['y'])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)

# Image Creator
    pyautogui.moveTo(ImageCreatoropen['x'],ImageCreatoropen['y'])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(ImageCreatorprompt['x'],ImageCreatorprompt['y'])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.typewrite(Joke[0]["background_prompt"])
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
    time.sleep(3)
    pyautogui.typewrite("Image1")
    time.sleep(3)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.moveTo(ImageCreatorprompt['x'],ImageCreatorprompt['y'])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.typewrite(Joke[0]["random_person_image"])
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
    time.sleep(3)
    pyautogui.typewrite("Image2")
    time.sleep(3)
    pyautogui.hotkey('enter')
    time.sleep(1)

# VS Code
    pyautogui.moveTo(VSCodeopen["x"],VSCodeopen["y"])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(GoLive["x"],GoLive["y"])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(3)

# # Microsoft Edge
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
    time.sleep(3.7)

    with open('Recording_Started.json', 'w') as json_file:
       json.dump("Hello", json_file)
    End = False
    while(End == False):
       if(pyautogui.pixelMatchesColor(Ending["x"],Ending["y"], (0, 0, 100))):
          print(pyautogui.pixel(Ending["x"],Ending["y"]))
          End = True
          pyautogui.moveTo(Recordingend["x"],Recordingend["y"])
          time.sleep(1)
          pyautogui.leftClick()
          time.sleep(1)
          pyautogui.moveTo(1485,1049)
          time.sleep(1)
          pyautogui.rightClick()
          time.sleep(1)
          pyautogui.moveTo(1410,984)
          time.sleep(1)
          pyautogui.leftClick()
          time.sleep(1)
          pyautogui.leftClick()
          time.sleep(1)
          pyautogui.hotkey('ctrl','w')
        #   time.sleep(1)
        #   pyautogui.moveTo(Copilot['x'],Copilot['y'])
        #   time.sleep(1)
        #   pyautogui.leftClick()
        #   time.sleep(1)
       if(pyautogui.pixelMatchesColor(Ending["x"],Ending["y"], (115, 115, 115))):
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
    pyautogui.moveTo(Donechange['x'],Donechange['y'])
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.typewrite("False")
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.moveTo(141,158)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.hotkey('delete')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.hotkey('delete')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.moveTo(140,241)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.hotkey('delete')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.moveTo(139,264)
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.hotkey('delete')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
# Microsoft Edge
    pyautogui.moveTo(MicrosoftEdgeTab["x"],MicrosoftEdgeTab["y"])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    #  pyautogui.moveTo(YoutubeOpen["x"],YoutubeOpen["y"])
    #  time.sleep(1)
    #  pyautogui.leftClick()
    #  time.sleep(1)
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
    # pyautogui.moveTo(Videos["x"],Videos["y"])
    # time.sleep(1)
    # pyautogui.leftClick()
    # time.sleep(1)
    # pyautogui.moveTo(ScreenRecordings["x"],ScreenRecordings["y"])
    # time.sleep(1)
    # pyautogui.doubleClick()
    # time.sleep(1)
    pyautogui.moveTo(Recordings["x"],Recordings["y"])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.hotkey('delete')
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(10)
    pyautogui.moveTo(ReUseDetails["x"],ReUseDetails["y"])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(ChooseVideoDetails["x"],ChooseVideoDetails["y"])
    time.sleep(1)
    if (pyautogui.pixelMatchesColor(ChooseVideoDetails["x"],ChooseVideoDetails["y"], (255, 255, 255))):
     pyautogui.moveTo(505,501)    
     pyautogui.leftClick()
    else:
     pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(ConfirmDetails["x"],ConfirmDetails["y"])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(VideoTitle["x"],VideoTitle["y"])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.typewrite(Joke[0]["title"])
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
    # print("Video Created and Published succesfully")

# To reset the code cycle
    pyautogui.moveTo(CodeRunner['x'],CodeRunner['y'])
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)


    

    





# pyautogui.moveTo(['x'],['y'])
# pyautogui.leftClick()


# Doing something else


