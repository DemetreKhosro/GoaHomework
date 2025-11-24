const key = "uid";

const user = {
    [key]: 1,
    username: "asdasd",
    email: "qweqwe@gmail.com",
    score: 0,
    
    increaseScore(amount) {
        this.score += amount;
    }
};

user.increaseScore(5);
console.log(user.score);