class Product {
    constructor(name, price) {
        this.name = name;
        this.price = price;
    }
}

export function printName(product) {
    console.log("Name:", product.name);
}

export function printPrice(product) {
    console.log("Price:", product.price);
}

export default Product;
