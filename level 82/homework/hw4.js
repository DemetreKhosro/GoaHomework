class Account {
    static count = 0;

    firstname;
    lastname;
    #password;

    constructor(firstname, lastname, password) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.#password = password;
        Account.objectCount();
    }

    get password() {
        return this.#password;
    }

    set password(newPass) {
        if (newPass.length >= 4) {
            this.#password = newPass;
        }
    }

    showInfo() {
        console.log(this.firstname + " " + this.lastname);
        this.#logAccess();
    }

    #logAccess() {
        console.log("logged in");
    }

    static objectCount() {
        Account.count++;
    }
}

const user1 = new Account("Demetre", "Khosroshvili", "khosro123");

console.log(Account.count);

console.log(user1.password);

user1.password = "khosrokhosro";

user1.showInfo();