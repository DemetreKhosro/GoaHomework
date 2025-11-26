const numbersArr = [12,15,17,12,15,36,23,6,2,6];

function manualMap(array, callback) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        result.push(callback(array[i], i, array));
    }
    return result;
}

const manualMapped = manualMap(numbersArr, n => n * 2);
console.log(manualMapped);

const mapped = numbersArr.map(n => n * 2);
console.log(mapped);