class WashingMachine {
    constructor(brand) {
        this.brand = brand;
    }
}

class SmartWashingMachine extends WashingMachine {
    quickWash() {
        console.log("Quick wash started");
    }
}

const wm = new SmartWashingMachine("LG");
wm.quickWash();
