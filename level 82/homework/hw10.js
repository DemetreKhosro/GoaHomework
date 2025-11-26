const numbersArr = [12,15,17,12,15,36,23,6,2,6];

function manualReduce(array, callback, initialValue) {
    let accumulator = initialValue;
    for (let i = 0; i < array.length; i++) {
        accumulator = callback(accumulator, array[i], i, array);
    }
    return accumulator;
}

const manualMax = manualReduce(numbersArr, (acc, cur) => (cur > acc ? cur : acc), numbersArr[0]);
console.log(manualMax);

const builtInMax = numbersArr.reduce((acc, cur) => (cur > acc ? cur : acc), numbersArr[0]);
console.log(builtInMax);
