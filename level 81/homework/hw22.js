class User {
    static userCount = 0;

    #age;

    constructor(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        User.userCount++;
    }

    get age() {
        return this.#age;
    }

    set age(value) {
        if (this.#validateAge(value)) {
            this.#age = value;
        } else {
            throw new Error("invalid age, must be between 1 and 50.");
        }
    }

    #validateAge(value) {
        return typeof value === "number" && value > 0 && value <= 50;
    }

    static getUserCount() {
        return User.userCount;
    }
}

try {
    const user1 = new User("Demetre", "Khosroshvili", 14);
    console.log(user1.age);

    const user2 = new User("John", "Smith", 55);
} catch (error) {
    console.error(error.message);
}

console.log(User.getUserCount());
