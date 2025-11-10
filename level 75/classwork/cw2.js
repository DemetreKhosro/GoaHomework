const productsContainer = document.getElementById('productsContainer');
const productCart = document.getElementById('productCart');

const products = [
    {name: 'product1', price: 100, desc: 'asdasdasd'},
    {name: 'product2', price: 200, desc: 'asdaswdasd'},
    {name: 'product3', price: 300, desc: 'adfgefsdf'},
    {name: 'product4', price: 400, desc: 'asdxcvbxcb'},
]

for (let i = 0; i < products.length; i++) {
    const product = products[i];

    productsContainer.innerHTML += `
    <div class="product">
        <h2>${product.name}</h2>
        <p>${product.desc}</p>
        <p>Price: $${product.price}</p>
        <button>Buy</button>
        <hr>
    </div>
    `;
}