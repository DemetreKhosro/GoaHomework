//3) შექმენით რიცხვების მასივსი და გამოიყენეთ მომცეული მეთოდებიდან ყველა თან ახსენით როგორ მუშაობენ

//pop
//shift
//unshift
//slice
//splice
//indefOf
//lastIndexOf
//includes
//find
//findIndex

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

// pop შლის მასივის ბოლო ელემენტს
console.log(numbers.pop())

// shift შლის მასივის პირველ ელემენტს
console.log(numbers.shift())

// unshift ამატებს ელემენტს დასაწყისში
console.log(numbers.unshift(0))

// slice ქმნის ახალ მასივს მითითებული დიაპაზონიდან (არ ცვლის ორიგინალს)
console.log(numbers.slice(5, 10))

// splice შლის ან ამატებს ელემენტებს მითითებულ ადგილას (ცვლის ორიგინალს)
console.log(numbers.splice(2, 3, 'A', 'B', 'C'))

// indexOf აბრუნებს ელემენტის პირველ ინდექსს
console.log(numbers.indexOf('B'))

// lastIndexOf აბრუნებს ელემენტის ბოლო ინდექსს
console.log(numbers.lastIndexOf(10))

// includes ამოწმებს შეიცავს თუ არა მასივი კონკრეტულ მნიშვნელობას
console.log(numbers.includes(10))

// find აბრუნებს პირველ ელემენტს, რომელიც აკმაყოფილებს პირობას
console.log(numbers.find(num => typeof num === 'number' && num > 10))

// findIndex აბრუნებს პირველ ელემენტს ინდექსის პირობის მიხედვით
console.log(numbers.findIndex(num => typeof num === 'number' && num > 10))