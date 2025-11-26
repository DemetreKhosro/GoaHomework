const nums = [1, 2, 2, 3, 4, 5, 5, 6];

const squares = nums.map(n => n ** 2);
const plusFive = nums.map(n => n + 5);

const evens = nums.filter(n => n % 2 === 0);
const uniques = nums.filter(n => nums.indexOf(n) === nums.lastIndexOf(n));

console.log(squares);
console.log(plusFive);
console.log(evens);
console.log(uniques);

