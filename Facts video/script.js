fetch('Joke_data.json')  // Assuming the file is in the same folder
    .then(response => response.json())
    .then(data => {

        // Use the received data to update the image
        const imgElement1 = document.querySelector('#image1');
        const imgElement2 = document.querySelector('#image2');
        const Chav = document.querySelector('#Chav')
        // const imgagesElement = document.querySelector('#images');
        const headElement = document.querySelector('#heading');
        headElement.innerText = data[0][0]
        const ender = document.querySelector('#Ender');
        function loadVoices() {
            const voices = window.speechSynthesis.getVoices();
            console.log('Available voices:', voices);

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

        function speakAsync(text) {
            return new Promise((resolve, reject) => {
                if (!text) {
                    reject("No text provided to speak.");
                    return;
                }

                const utterance = new SpeechSynthesisUtterance(text);
                if (englishVoice) {
                    utterance.voice = englishVoice;
                    utterance.lang = 'en-US';
                } else {
                    console.warn('English voice is not set. Using default voice.');
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

        async function Speaktext() {
            try {
                const animations = ['fade-out', 'slide-up', 'shrink', 'flip-out'];
                await speakAsync(data[0][0][0])
                Chav.src = ''
                for (let i = 1; i < data[0].length; i++) {
                    await speakAsync(data[0][i][0]);
                    // Set the source of the upper image
                    imgElement1.src = `Images/Image${i}.jpeg`;

                    if ((data[0].length - i) > 1) {
                        // Set the source of the lower image
                        imgElement2.src = `Images/Image${i + 1}.jpeg`;

                        // Randomly select an animation class
                        const randomAnimation = animations[Math.floor(Math.random() * animations.length)];
                        imgElement1.classList.add(randomAnimation);

                        // Wait for the animation to complete
                        await new Promise(resolve => {
                            imgElement1.addEventListener('transitionend', function handleTransitionEnd() {
                                // Remove the animation class after it completes
                                imgElement1.src = `Images/Image${i + 1}.jpeg`
                                imgElement1.classList.remove(randomAnimation);
                                imgElement1.removeEventListener('transitionend', handleTransitionEnd);
                                resolve();
                            });
                        });
                    }
                }
                ender.style.left = "700px"


            } catch (error) {
                console.error("Error during speech:", error);
            }
        }

        const checkVoicesLoaded = setInterval(() => {
            if (englishVoice) {
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
                                console.log("speaking")
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
    }).catch(error => {
        console.log(error)
        ender.style.backgroundColor = "rgb(115,115,115)"
        ender.style.left = "700px";
    });