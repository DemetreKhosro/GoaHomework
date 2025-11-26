const arr = [
    {id: 123, name: "luka"},
    {id: 456, name: "ana"},
    {id: 789, name: "gio"}
];

const names = arr.map(item => item.name);
console.log(names);

function manualMap(array, callback) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        result.push(callback(array[i], i, array));
    }
    return result;
}

const manualNames = manualMap(arr, item => item.name);
console.log(manualNames);

/*
1. Map საშუალებას გვაძლევს შევქმნათ ახალი მასივი შეცვლილი ელემენტებით
2. შეგვიძლია კონკრეტული ველის არჩევა ან მნიშვნელობის შეცვლა
3. კოდი არის მოკლე და მარტივი
*/