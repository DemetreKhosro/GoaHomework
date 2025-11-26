const products = [
    {name: "apple", price: 2},
    {name: "banana", price: 1},
    {name: "cherry", price: 3},
    {name: "watermelon", price: 5}
];

const cheapProducts = products.filter(product => product.price <= 3);

console.log(cheapProducts);