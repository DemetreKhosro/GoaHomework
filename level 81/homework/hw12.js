class Car {
    constructor(make, model) {
        this.make = make;
        this.model = model;
    }

    displayInfo() {
        console.log(`${this.make} ${this.model}`);
    }
}

class ElectricCar extends Car {
    constructor(make, model, batteryLevel) {
        super(make, model);
        this.batteryLevel = batteryLevel;
    }

    displayInfo() {
        console.log(`${this.make} ${this.model} - Battery: ${this.batteryLevel}%`);
    }
}


const eCar = new ElectricCar("Tesla", "Model S", 85);
eCar.displayInfo();