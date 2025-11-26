const people = [
    {name: "Luka", age: 16},
    {name: "Ana", age: 21},
    {name: "Gio", age: 17},
    {name: "Nino", age: 25}
];

const underagePeople = people.filter(person => person.age < 18);
const adultPeople = people.filter(person => person.age >= 18);

console.log(underagePeople);
console.log(adultPeople);