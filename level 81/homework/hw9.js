class Animal {
    sound() {
        console.log("Unknown sound");
    }
}

class Dog extends Animal {
    sound() {
        console.log("Bark!");
    }
}

const d = new Dog();
d.sound();