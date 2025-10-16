//2) for ციკლის მეშვეობით გადაუარეთ რიცხვებს 1-იდან 10-მდე, თითოეული რიცხვისთვის ობიექტის კონსტრუქტორით (აიღეთ კონსტრუქტორი for ციკლის გაშვებამდე) შექმენით ობიექტი რომელსაც ექნება 2 კუთვნილება რიცხვი და even (ან ლუწია თუ კენტი) თუ რიცხვი ლუწი იქნება მაშინ even კუთვნილების მნიშვნელობა უნდა იყოს true ხოლო სხვა შემთხვევაში false, ეს ყველა ობიექტი უნდა დაამატოთ nubmers მასივში

const numbers = []

function numberObj(number, even) {
    this.number = number,
    this.even = number % 2 === 0
}

for (let i = 1; i <= 10; i++) {
    const numbObj = new numberObj(i);
    numbers.push(numbObj)
}

console.log(numbers)