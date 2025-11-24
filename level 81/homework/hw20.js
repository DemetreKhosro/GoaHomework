const car = {
    make: "Tesla",
    model: "Model 3",
    year: 2023
};

const newCar = { ...car, model: "Model S" };

console.log(newCar);