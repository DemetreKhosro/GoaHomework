let myfunction = () => {
    let firstArg = 10;
    let otherArgs = [20, 30, 40, 50];

    let numberList = [5, ...otherArgs, firstArg, 60, 70];
    console.log(numberList);
}

myfunction();