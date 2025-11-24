class Account {
    constructor(firstName, lastName, email, password, city) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.password = password;
        this.city = city;
    }

    printDetails() {
        console.log(`${this.firstName} ${this.lastName}, Email: ${this.email}, City: ${this.city}`);
    }
}

const accounts = [];

const formData = {
    firstName: "Demetre",
    lastName: "Khosroshvili",
    email: "deme@example.com",
    password: "12345",
    city: "Tbilisi"
};

const newAccount = new Account(
    formData.firstName,
    formData.lastName,
    formData.email,
    formData.password,
    formData.city
);

accounts.push(newAccount);

accounts[0].printDetails();