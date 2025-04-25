IMPORTANT Information!!
This code only works for Laptops/PC and not for mobile currently.
PLEASE Read the whole README before running the code on your device as it is not easy to run it on your device smoothly.
This code as 3 main folders. 1 generates a video in which a random person is roasted. 2nd one generates a video in which there is a funny conversation between some characters and the last one generates a video in which there are answers to some What if questions of hypothetical scenarios.
1) This code works using pyautogui and goes to specific locations on your screen using mouse clicks. Therefore re-check or change the pixels location of the codes for your screen using location.py file present in all 3 codes.
2) There is also some commented code in each file. Please dont un-comment them or it will cause errors.
3) This code works by making an AI model ; Copilot in this case about the specific format for the videos.


Person Roaster
{
  "language": "English",
  "title": "TheGuyWho went to a {Place}",
  "background_prompt": Prompt of the background image,
  "intro_sentence": "someone went to a place and ......",
  "random_person_image": Image of the {random person} who will speak the roast,
  "random_person_gender": Gender of the character,
  "roast_dialogue": "The {random_person} replied, 'Buddy, roast.."
}
Give this format to the AI model
NOTE:
In the above format. I used someone in intro_sentence as a fixed word because it will replaced by a random person present in the code and the word Buddy will be replaced any 1 one of the funny words present in the code.


Funny Conversation format
[
  [Place name],

  [Title],

  [Character1, Dialogue, Emoji],

  [Character2, Dialogue, Emoji],

  [Character3, Dialogue, Emoji]

]
You can even tell the AI to give more dialogues to 1 character.
This format should be given to the AI model and you should even tell him about all the emojis you use and about the characters.


Facts Video format
[
[Title],
[Sentence spoken, Image prompt of that sentece],
[Sentence spoken, Image prompt of that sentece],
[Sentence spoken, Image prompt of that sentece],
.......
]


Example of this


[
  [
    "What if All Animals Could Talk?"
  ],
  [
    "How would the world change if every animal on Earth suddenly gained the ability to communicate with humans? Imagine a reality where humans could understand their thoughts, emotions, and perspectives.",
    "A vibrant scene of animals speaking to humans in parks, farms, and homes, with expressions of curiosity, wisdom, and humor on their faces."
  ],
  [
    "Human-animal relationships would transform entirely, with pets and wildlife expressing their needs and desires directly.",
    "An image of a dog explaining its preferences for food to its owner, while wild birds share migration stories with fascinated humans."
  ],
  [
    "The study of animal behavior would take on new dimensions, as scientists work to understand the depth of intelligence and emotion across species.",
    "A depiction of researchers in a laboratory, listening intently as dolphins share complex insights about underwater ecosystems."
  ],
  [
    "Ethical dilemmas might arise, as animals debate their roles in society and ask questions about their treatment and environments.",
    "An emotional image of farm animals conversing with humans about their living conditions, prompting thoughtful changes in agriculture."
  ],
  [
    "Would humanity embrace the wisdom and companionship of animals, or struggle to adapt to a world where every creature has a voice?",
    "A hopeful scene of humans and animals collaborating to protect nature, with elephants, wolves, and bees actively contributing to conservation efforts."
  ]
]




 Thankyou very much for using it.
