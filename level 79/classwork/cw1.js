/*
1) დაწერეთ რა არის ES6, მოიყვანეთ თითოეული მისი დამატებული ფუნქციონალის მაგალითი და აღწერეთ

ცვლადები
string
for loop
arrow function
*/ 

// EcmaScript 6 ES6 -  JS-ის განახლებული ვერსია რომელსაც დაემატა ახალი ჩაშენებული ფუნქციები და აქვს უფრო ადვილი სინტაქსი.
// დაემატა კლასები, ანონიმური ფუნქციები, map, filter და ა.შ.

// ცვლადები - EC6-მდე მათ ქმნიდნენ var keyword-ით, EC6-ის სინტაქსში დაემატა let რომელიც უკეთესია

// for loop - უფრო ადვილი სინტაქსი
// ძველი
for (let i = 0; i < 10; i ++) {
    console.log(i)
}

// ახალი
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for (const num of numbers) {
    console.log(num)
}

// arrow function - ანონიმური ფუნქცია
const doubledNumbers = numbers.map(n => n * 2)

const greet = () => "Hello!";

const getInfo = (name, age) => {
    return `Name: ${name}, Age: ${age}`;
};

// სტრინგებისთვის დაემატა backtick, როგორც F სტრინგი პითონში და ცვლადის შესატანად ვიყენებთ დოლარის ნიშანს ${name}