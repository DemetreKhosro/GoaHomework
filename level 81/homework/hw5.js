function calcSum(first, ...numbers) {
    let sum = 0;
    for (let num of numbers) {
        sum += num;
    }
    console.log(first, sum);
}

calcSum(5, 10, 20, 30);