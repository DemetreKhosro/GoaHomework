class Animal {
    constructor(name) {
        this.name = name;
    }
}

class SmartAnimal extends Animal {
    constructor(name, intelligenceLevel) {
        super(name);
        this.intelligenceLevel = intelligenceLevel;
    }

    describe() {
        console.log(this.name, this.intelligenceLevel);
    }
}

const sa = new SmartAnimal("Dolphin", "High");
sa.describe();