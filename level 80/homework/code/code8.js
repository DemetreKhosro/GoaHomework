// https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/javascript
// Simple Pig Latin

function pigIt(str) {
    const words = str.split(' ');
    const result = [];

    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        const firstChar = word[0];
        if ((firstChar >= 'A' && firstChar <= 'Z') || (firstChar >= 'a' && firstChar <= 'z')) {
            result.push(word.slice(1) + firstChar + 'ay');
        } else {
            result.push(word);
        }
    }

    return result.join(' ');
}