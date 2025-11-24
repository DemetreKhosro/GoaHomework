let p1 = "firstProp";
let p2 = "secondProp";
let dyn = "bal" + "ance";

const account = {
    [p1]: "value1",
    [p2]: "value2",
    [dyn]: 100,
    deposit(amount) {
        this.balance += amount;
    }
};

account.deposit(50);
account.deposit(30);

console.log("account:", account);

const person = {
    name: "Gio",
    age: 22,
    balance: 500
};

console.log("person:", person);

const personAccount = Object.assign({}, account, person);

console.log("personAccount:", personAccount);

const dataArr = [10, 20, 30];

const [a, b, c] = dataArr;

console.log(a, b, c);   