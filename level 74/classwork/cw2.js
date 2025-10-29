const productsContainer = document.getElementById('productsContainer');
const productCart = document.getElementById('productCart');

const products = [
    {name: 'product1', price: 100, desc: 'asdasdasd'},
    {name: 'product2', price: 200, desc: 'asdaswdasd'},
    {name: 'product3', price: 300, desc: 'adfgefsdf'},
    {name: 'product4', price: 400, desc: 'asdxcvbxcb'},
]

/*
function addToCart(pointerevent, product) {
    console.log(product)
    const newItem = document.createElement('li')
    newItem.textContent = `Product name: ${product.name}, price: ${product.price}`
    productCart.appendChild(newItem)
}
*/

for (let i = 0; i < products.length; i++) {
    let currentProduct = products[i];

    let productDiv = document.createElement('div');
    let productTitle = document.createElement('h2');
    productTitle.textContent = currentProduct.name
    
    let productDesc = document.createElement('p')
    productDesc.textContent = currentProduct.desc

    let price = document.createElement('p')
    price.textContent = `Price: ${currentProduct.price}`

    let addBtn = document.createElement('button')
    addBtn.textContent = 'Add To Cart'

    addBtn.onclick = function() {
        const newItem = document.createElement('li')
        newItem.textContent = `Product name: ${currentProduct.name}, price: ${currentProduct.price}`
        productCart.appendChild(newItem)
    }
    
    let productImg = document.createElement('img')
    productImg.width = '200px';
    productImg.height = '200px';

    productDiv.appendChild(productTitle)
    productDiv.appendChild(productDesc)
    productDiv.appendChild(price)
    productDiv.appendChild(addBtn)
    productDiv.appendChild(productImg)

    

    productDiv.style.border = '1px solid grey'

    productsContainer.appendChild(productDiv)
}