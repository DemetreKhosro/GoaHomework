const words = ["apple", "banana", "apple", "cherry", "banana", "apple"];

const wordCount = {};

words.forEach(word => {
    if (wordCount[word]) {
        wordCount[word]++;
    } else {
        wordCount[word] = 1;
    }
});

console.log(wordCount);