const myArr = ["AB", "CD", "ED"];

const newArr = myArr.map((value, index, arr) => {
    return value + "#" + index;
});

console.log(newArr);


function manualMap(array, callback) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        result.push(callback(array[i], i, array));
    }
    return result;
}

const manualArr = manualMap(myArr, (value, index, arr) => {
    return value + "#" + index;
});

console.log(manualArr);

// value - მიმდინარე ელემენტი
// index - მიმდინარე ელემენტის ინდექსი
// arr - მასივი რომელზეც ხდება ოპერაცია