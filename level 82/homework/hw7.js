const fruits = ['apple','banana','orange'];

fruits.forEach((value, index, arr) => {
    // value — მიმდინარე ელემენტი ("apple", "banana", "orange")
    // index — მიმდინარე ინდექსი 0, 1, 2
    // arr — მთლიანი მასივი ['apple','banana','orange']
    console.log(value.toUpperCase());
});

// ესე უკეთესია :)
fruits.forEach(n => console.log(n.toUpperCase()));

function manualForEach(array, callback) {
    for (let i = 0; i < array.length; i++) {
        // callback იღებს სამ პარამეტრს — value, index, arr
        callback(array[i], i, array);
    }
}

manualForEach(fruits, (value, index, arr) => {
    console.log(value.toUpperCase());
});

fruits.manualForEach(n => console.log(n.toUpperCase()));