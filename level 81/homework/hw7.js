class BankAccount {
    static accountsCount = 0;

    constructor(owner, balance) {
        this.owner = owner;
        this.balance = balance;
        BankAccount.accountsCount++;
    }

    deposit(amount) {
        this.balance += amount;
    }

    static getAccountsCount() {
        return BankAccount.accountsCount;
    }
}

const acc1 = new BankAccount("Nika", 100);
const acc2 = new BankAccount("Luka", 200);

console.log(BankAccount.getAccountsCount());