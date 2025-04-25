fetch('Joke_data.json')  // Assuming the file is in the same folder
    .then(response => response.json())
    .then(data => {

        // Use the received data to update the image
        const imgElement = document.querySelector('#image');
        // const imgagesElement = document.querySelector('#images');
        const headElement = document.querySelector('#heading');
        headElement.innerText = data[0][1]  // Set the img src from the JSON data
        const ender = document.querySelector('#Ender');
        const EmojiElement = document.querySelector('#Emoji')
        const charactername = document.querySelector('#charactername')
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

        // for (i = 2; i < data[0].length; i++) {
        //     const output = splitByCharacterLimit(data[0][i][1], 110);

        //     // Find the index of "b"

        //     // Remove "b" and insert String2 elements
        //     data[0][i].splice(1, 1); // Remove "b"
        //     data[0][i].splice(1, 0, ...output);
        // }
        VoiceStore = {
            "Achaloo": ["Prabhat", 2],
            "Gendu": ["Connor", 0.5],
            "Wildi": ["Chilemba", 1.7],
            "Amcha": ["Andrew", 1.4],
            "Polly": ["Roger", 1.6],
            "Eron": ["Ravi", 2]
        }
        // Function to initialize and fetch available voices
        function getMicrosoftVoices() {
            return new Promise((resolve) => {
                let voices = window.speechSynthesis.getVoices();
                if (voices.length) {
                    resolve(voices);
                } else {
                    window.speechSynthesis.onvoiceschanged = () => {
                        voices = window.speechSynthesis.getVoices();
                        resolve(voices);
                    };
                }
            });
        }

        // Function to speak using a specific Microsoft voice and pitch
        async function Speak(name, pitch, dialogue) {
            // Fetch all available voices
            const voices = await getMicrosoftVoices();

            // Find the voice that includes the specified name
            const selectedVoice = voices.find((voice) => voice.name.includes(name));
            if (!selectedVoice) {
                console.error(`Voice "${name}" not found.`);
                return;
            }

            // Create a SpeechSynthesisUtterance object
            const utterance = new SpeechSynthesisUtterance(dialogue);

            // Set the selected voice and pitch
            utterance.voice = selectedVoice;
            utterance.pitch = pitch;
            utterance.rate = 1; // Default rate
            utterance.volume = 1; // Default volume

            // Wait for the speech to finish
            return new Promise((resolve) => {
                utterance.onend = () => resolve();
                window.speechSynthesis.speak(utterance);
            });
        }

        // Wrapper function for Speak
        async function mainspeak(Name, Pitch, Dialogue) {
            await Speak(Name, Pitch, Dialogue);
        }

        // Main Play function
        async function Play() {
            for (let i = 2; i < data[0].length; i++) {
                imgElement.src = `Code/${data[0][i][0]}.png`;
                console.log(`Code/${data[0][i][0]}.png`);
                EmojiElement.src = `Code/Emoji${data[0][i][data[0][i].length - 1]}.png`;
                console.log(`Code/Emoji${data[0][i][data[0][i].length - 1]}.png`);
                charactername.innerText = data[0][i][0]

                    // Await mainspeak to ensure it finishes before continuing
                    await mainspeak(
                        VoiceStore[data[0][i][0]][0],
                        VoiceStore[data[0][i][0]][1],
                        data[0][i][1]
                    )
            }
            ender.style.left = "700px";
        }
        async function waitForJSONFile(url, interval = 2000) {
            console.log(`Waiting for ${url}...`);
            while (true) {
                try {
                    const response = await fetch(url);
                    if (response.ok) {
                        console.log('File found!');
                        const datae = await response.json();
                        console.log('JSON Data:', datae);
                        Play();
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
        // Execute Play function



        // async function waitForJSONFile(url, interval = 2000) {
        //     console.log(`Waiting for ${url}...`);

        //     while (true) {
        //         try {
        //             const response = await fetch(url);

        //             if (response.ok) {
        //                 console.log('File found!');
        //                 // const datae = await response.json(); // Use 'datae' instead of 'data'
        //                 // console.log('JSON Data:', datae);
        //                 // Process the JSON data as needed
        //                 // handleData(datae);

        //                 // Speaktext()
        //                 break;
        //             } else {
        //                 console.log(`File not available (status: ${response.status}), retrying...`);
        //             }
        //         } catch (error) {
        //             console.log('File not available yet, retrying...');
        //         }

        //         // Wait for the next check
        //         await new Promise(resolve => setTimeout(resolve, interval));
        //     }
        // }

        // waitForJSONFile('./Recording_Started.json');
        // Function to handle the data
        // function handleData(datae) {
        //     console.log('Processing Data:', datae);
        //     // Add your data processing logic here
        // }
    }).catch(error => {
        console.log(error)
        ender.style.backgroundColor = "rgb(115,115,115)"
        ender.style.left = "700px";
    });
