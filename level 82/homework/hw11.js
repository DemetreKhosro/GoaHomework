const names = ['John','Jane','Mike','Anna'];

const lengthsMap = names.map(name => name.length);
console.log(lengthsMap);

function manualMap(array, callback) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        result.push(callback(array[i], i, array));
    }
    return result;
}

const lengthsManualMap = manualMap(names, name => name.length);
console.log(lengthsManualMap);

const totalLength = lengthsMap.reduce((acc, cur) => acc + cur, 0);
console.log(totalLength);

function manualReduce(array, callback, initialValue) {
    let accumulator = initialValue;
    for (let i = 0; i < array.length; i++) {
        accumulator = callback(accumulator, array[i], i, array);
    }
    return accumulator;
}

const totalLengthManual = manualReduce(lengthsManualMap, (acc, cur) => acc + cur, 0);
console.log(totalLengthManual);

// acc იცვლება ყოველ ნაბიჯზე და ინახავს ჯამს მაგალითად იწყება 0-დან და ემატება პირველი ელემენტის სიგრძეს შემდეგ მეორე ელემენტის სიგრძეს და ა.შ.