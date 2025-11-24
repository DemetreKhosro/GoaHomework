class User {
    constructor(password) {
        this._password = password;
    }

    get password() {
        return this._password;
    }
}

const u = new User("secret123");
console.log(u.password);