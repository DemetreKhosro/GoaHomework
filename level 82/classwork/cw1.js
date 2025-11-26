class Account {
    constructor(fname, lname, email) {
        this.fname = fname;
        this.lname = lname;
        this.email = email;
    }
}

const accounts = [];

const btn = document.getElementById("submitBtn");

btn.onclick = () => {
    const fname = document.getElementById("fname").value;
    const lname = document.getElementById("lname").value;
    const email = document.getElementById("email").value;

    const account = new Account(fname, lname, email);
    accounts.push(account);

    console.log(accounts);
};