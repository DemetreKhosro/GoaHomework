const numbersArr = [12,15,17,12,15,36,23,6,2,6];

// ჯამი reduce-ით
const sum = numbersArr.reduce((acc, value) => acc + value, 0);
console.log(sum);

// გამრავლება reduce-ით
const product = numbersArr.reduce((acc, value) => acc * value, 1);
console.log(product);


function manualReduce(array, callback, initialValue) {
    let accumulator = initialValue;
    for (let i = 0; i < array.length; i++) {
        accumulator = callback(accumulator, array[i], i, array);
    }
    return accumulator;
}

const manualSum = manualReduce(numbersArr, (acc, value) => acc + value, 0);
console.log(manualSum);

const manualProduct = manualReduce(numbersArr, (acc, value) => acc * value, 1);
console.log(manualProduct);