// rest შეაგროვებს ყველა ელემენტს მასივში

function sumAll(...numbers) {
    let sum = 0;
    numbers.forEach(num => sum += num);
    return sum;
}

console.log(sumAll(5, 10))