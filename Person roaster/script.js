fetch('Joke_data.json')  // Assuming the file is in the same folder
    .then(response => response.json())
    .then(data => {
        // if (data[0]["language"] == "Hindi" && data[0]["random_person_gender"] == "Female") {
        //     TotalImages = ["Mamata Baneerjee", "Priyanka Gandhi"]
        //     TotalImagesHindi = ["ममता बनर्जी", "प्रियंका गांधी"]
        // }
        // else if (data[0]["language"] == "Hindi" && data[0]["random_person_gender"] == "Male") {
        //     TotalImages = ["Akhilesh Yadav", "Arvind Kejriwal", "Rahul Gandhi"]
        //     TotalImagesHindi = ["अखिलेश यादव", "अरविंद केजरीवाल", "राहुल गांधी"]
        // }
        // else if (data[0]["language"] == "English" && data[0]["random_person_gender"] == "Male") {
        //     TotalImages = ["Barack Obama", "Bill Gates", "Cristiano Ronaldo", "Donald Trump", "Elon Musk", "Jeff Bezos", "Joe Biden", "Lionel Messi", "Neymar Jr"]
        //     TotalImagesEnglish = ["Barack Obama", "Bill Gates", "Cristiano Ronaldo", "Donald Trump", "Elon Musk", "Jeff Bezos", "Joe Biden", "Lionel Messi", "Neymar Jr"]
        // }
        // randomnum = Math.floor(Math.random() * TotalImages.length)
        // Name = TotalImages[randomnum]
        // if(data[0]["language"] == "Hindi"){
        //     NameLan = TotalImagesHindi[randomnum]
        // }
        // else{
        //     NameLan = TotalImagesEnglish[randomnum]
        // }
        // console.log(randomnum)
        // console.log(Name,NameLan)
        // Use the received data to update the image
        title = data[0]["title"]
        titlearray = title.split(" ")
        Name = `${titlearray[0]} ${titlearray[1]}`
        // titlenew = titlearray.join(" ")
        // introsentence = data[0]["intro_sentence"]
        // introsentencearray = introsentence.split(" ")
        // introsentencearray[0] = NameLan
        // introsentencenew = introsentencearray.join(" ")
        imgElement = document.querySelector('#image')
        // Find the name from title
        imgElement.src = `PoolImages/${Name}.png`;
        const imagesElement = document.querySelector('#images');
        const headElement = document.querySelector('#heading');
        // headElement.innerText = title  // Set the img src from the JSON data
        const textElement = document.querySelector('#text');
        const ender = document.querySelector('#Ender');
        // console.log(data);  // Log the object data from Python
        // function splitByCharacterLimit(text, charLimit) {
        //     const words = text.split(/(,\s*|\s+)/); // Split text into words and commas (keeping spaces)
        //     let result = [];
        //     let currentLine = "";

        //     for (let i = 0; i < words.length; i++) {
        //         let word = words[i];
        //         let nextWord = words[i + 1] || "";

        //         // Check if adding the next word exceeds the character limit
        //         if (currentLine.length + word.length > charLimit) {
        //             result.push(currentLine.trim()); // Push the current line
        //             currentLine = word.trim(); // Start a new line with the current word
        //         } else {
        //             currentLine += word; // Add the word to the current line
        //         }

        //         // If a comma is found and we are within limit, break line
        //         if (word.includes(",") && currentLine.length <= charLimit) {
        //             result.push(currentLine.trim());
        //             currentLine = "";
        //         }
        //     }

        //     // Push the last line if it has content
        //     if (currentLine.trim()) {
        //         result.push(currentLine.trim());
        //     }

        //     return result;
        // }


        // const output1 = splitByCharacterLimit(data[0]["intro_sentence"], 55);
        // const output2 = splitByCharacterLimit(data[0]["roast_dialogue"], 55);
        // console.log(output1);
        // console.log(output2);

        // Declare voices in global scope
        let hindiVoice = null;
        let englishVoice = null;

        // Unified loadVoices function
        function loadVoices() {
            const voices = window.speechSynthesis.getVoices();
            console.log('Available voices:', voices);

            // Assign Hindi voice
            hindiVoice = voices.find(voice => voice.lang === 'hi-IN');
            if (hindiVoice) {
                console.log('Hindi voice detected:', hindiVoice.name);
            } else {
                console.warn('Hindi voice not found. Please ensure it is installed.');
            }

            // Assign English voice
            englishVoice = voices.find(voice => voice.lang === 'en-US');
            if (englishVoice) {
                console.log('English voice detected:', englishVoice.name);
            } else {
                console.warn('English voice not found. Please ensure it is installed.');
            }
        }

        // Set up voiceschanged event
        if (speechSynthesis.onvoiceschanged !== undefined) {
            speechSynthesis.onvoiceschanged = loadVoices;
        }

        // Load voices initially
        loadVoices();

        // Your speakAsync function (as updated above)
        function speakAsync(text, language) {
            return new Promise((resolve, reject) => {
                if (!text) {
                    reject("No text provided to speak.");
                    return;
                }

                const utterance = new SpeechSynthesisUtterance(text);

                if (language === "Hindi") {
                    if (hindiVoice) {
                        utterance.voice = hindiVoice;
                        utterance.lang = 'hi-IN';
                    } else {
                        console.warn('Hindi voice is not set. Using default voice.');
                    }
                } else if (language === "English") {
                    if (englishVoice) {
                        utterance.voice = englishVoice;
                        utterance.lang = 'en-US';
                    } else {
                        console.warn('English voice is not set. Using default voice.');
                    }
                }

                utterance.onend = () => {
                    console.log(`Finished speaking: "${text}"`);
                    resolve();
                };

                utterance.onerror = (error) => {
                    console.error('Speech synthesis error:', error);
                    reject(error);
                };

                speechSynthesis.speak(utterance);
                console.log('Speaking:', text);
            });
        }

        // Assuming `lan` is determined from your data:
        const lan = data[0]["language"];  // "Hindi" or "English"

        // The asynchronous Speaktext function
        let i = 0;
        async function Speaktext() {
            try {
                if (i == 0) {
                    // textElement.innerText = output1[i];
                    await speakAsync(data[0]["intro_sentence"], lan);
                } else if (i == 1) {
                    imagesElement.src = 'Images/Image2.jpeg';
                    imagesElement.onerror = function () {
                        imagesElement.src = 'Images/I.jpeg';
                    }
                    imgElement.src = '';
                    // textElement.innerText = output2[i - output1.length];
                    await speakAsync(data[0]["roast_dialogue"], lan);
                }

                if (i < 1) {
                    i++;
                    await Speaktext();
                } else {
                    ender.style.left = "700px";
                }

            } catch (error) {
                console.error("Error during speech:", error);
            }
        }

        // Start the speaking process once voices are loaded
        const checkVoicesLoaded = setInterval(() => {
            if (hindiVoice || englishVoice) {
                clearInterval(checkVoicesLoaded);

                async function waitForJSONFile(url, interval = 2000) {
                    console.log(`Waiting for ${url}...`);
                    while (true) {
                        try {
                            const response = await fetch(url);
                            if (response.ok) {
                                console.log('File found!');
                                const datae = await response.json();
                                console.log('JSON Data:', datae);
                                handleData(datae);
                                Speaktext();
                                break;
                            } else {
                                console.log(`File not available (status: ${response.status}), retrying...`);
                            }
                        } catch (error) {
                            console.log('File not available yet, retrying...');
                        }
                        await new Promise(resolve => setTimeout(resolve, interval));
                    }
                }

                waitForJSONFile('./Recording_Started.json');

                function handleData(datae) {
                    console.log('Processing Data:', datae);
                    // Your data processing logic here
                }
            }
        }, 100);







    })
    .catch(error => {
        console.log(error)
        ender.style.backgroundColor = "rgb(115,115,115)"
        ender.style.left = "700px";
    });

















// // try {
// //     const nodeVersion = process.version;
// //     console.log(`Node.js is installed. Version: ${nodeVersion}`);
// // } catch (error) {
// //     console.error('Node.js is not installed or accessible.');
// // }
// const fs = require('fs');
// const path = require('path');
// let name = ""

// // List of specific image names to check
// const specificImages = ['Rahul Gandhi.png', 'Akhilesh Yadav.png', 'Arvind Kejriwal.png', 'Mamata Banerjee.png', 'Priyanka Gandhi.png'];

// // Path to the 'Image' folder relative to the current script
// const imagesFolderPath = path.join(__dirname, 'Images');

// // Check for the presence of each image
//     // Read all files in the 'Image' folder
//     const filesInFolder = fs.readdirSync(imagesFolderPath);

//     // Find which images from the list are present in the folder
//     const copiedImage = specificImages.filter(image => filesInFolder.includes(image));

//     // console.log('Copied images:', copiedImages);
//     name = copiedImage
//     imgElement = document.querySelector('.image')
//     imgElement.src = `Images/${imageName}`
//     console.log(imgElement.src)

//     // Find missing images (optional)
//     // console.log('Missing images:', missingImages);
