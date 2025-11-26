const numbersArr = [12,15,17,12,15,36,23,6,2,6]
console.log(numbersArr.filter(n => n % 2 === 0))

function manualFilter(array, callback) {
    // ცვლადი სადაც შევინახავთ შედეგს
    const result = [];
    // გადავუვლით მასივს for ციკლით
    for (let i = 0; i < array.length; i++) {
        // თუ callback ფუნქციამ true დააბრუნა, მაშინ მიმდინარე ელემენტს შევინახავთ result მასივში
        if (callback(array[i], i, array)) {
            // მიმდინარე ელემენტი result მასივში
            result.push(array[i]);
        }
    }
    // ვაბრუნებთ result-ს
    return result;
}
