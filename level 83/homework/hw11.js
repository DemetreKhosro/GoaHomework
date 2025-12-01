class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

export function getUserName(user) {
    console.log("name:", user.name);
}

export function getUserAge(user) {
    console.log("age:", user.age);
}

export default User;