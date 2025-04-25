function splitByCharacterLimit(text, charLimit) {
    const words = text.split(/(,\s*|\s+)/); // Split text into words and commas (keeping spaces)
    let result = [];
    let currentLine = "";

    for (let i = 0; i < words.length; i++) {
        let word = words[i];
        let nextWord = words[i + 1] || "";

        // Check if adding the next word exceeds the character limit
        if (currentLine.length + word.length > charLimit) {
            result.push(currentLine.trim()); // Push the current line
            currentLine = word.trim(); // Start a new line with the current word
        } else {
            currentLine += word; // Add the word to the current line
        }

        // If a comma is found and we are within limit, break line
        if (word.includes(",") && currentLine.length <= charLimit) {
            result.push(currentLine.trim());
            currentLine = "";
        }
    }

    // Push the last line if it has content
    if (currentLine.trim()) {
        result.push(currentLine.trim());
    }

    return result;
}


const output1 = splitByCharacterLimit("One Day Lionel Messi went to a rocket science seminar and", 55);
console.log(output1[0])
// console.log("Hi")