const passwords = ["abc123", "pass2024", "qwerty"];

const [p1, p2, p3] = passwords;

passwords.push("password999");

const [a, b, c, ...rest] = passwords;

console.log(p1, p2, p3);
console.log(rest);