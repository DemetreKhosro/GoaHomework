const numArr = [1,2,3,4,5,6,7,8];

function isPrime(n) {
    if (n < 2) return false;
    // 2-დან ვიწყებთ შემოწმებას და ვუმატებთ i-ს ერთს სანამ n მეტია i-ზე
    for (let i = 2; i < n; i++) {
        // თუ n იყოფა i-ზე, მაშინ n არ არის პრაიმი
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const primesWithFilter = numArr.filter(isPrime);
console.log(primesWithFilter);

// manualFilter ფუნქცია
function manualFilter(array, callback) {
    // ცვლადი შედეგისთვის
    const result = [];
    // გადავუვლით მასივს
    for (let i = 0; i < array.length; i++) {
        // გადამოწმება callback ფუნქციით
        if (callback(array[i], i, array)) {
            result.push(array[i]); // ელემენტის დამატება შედეგში
        }
    }
    return result;
}