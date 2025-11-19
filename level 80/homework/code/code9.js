// https://www.codewars.com/kata/51edd51599a189fe7f000015/train/javascript
// Mean Square Error

const solution = function (firstArray, secondArray) {
    let sum = 0;
    for (let i = 0; i < firstArray.length; i++) {
        const diff = firstArray[i] - secondArray[i];
        sum += diff * diff;
    }
    return sum / firstArray.length;
};