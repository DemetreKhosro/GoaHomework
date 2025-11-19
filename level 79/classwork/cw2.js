/* 
2) შექმენით getProducts ფუნქცია, რომელიც წამოათრევს ინფორმაციას მოცემული api-იდან, თქვენ მოგეცემათ სია 20 პროდუქტის ობიექტით, თქვენი დავალებაა თითოეული პროდუქტის
სათაური, კატეგორია და სურათი დაარენდეროთ ცალ-ცალკე დივებად products container-ში (div), თქვენი სიტყვებით დაწერეთ async & await-ზე
*/

const productsContainer = document.getElementById("products");

const getProducts = async () => {
    try {
        const response = await fetch("https://fakestoreapi.com/products");
        const data = await response.json();

        data.forEach(product => {
            const div = document.createElement("div");
            div.classList.add("product");

            div.innerHTML = `
                <h3>${product.title}</h3>
                <p>${product.category}</p>
                <img src="${product.image}" width="120">
            `;

            productsContainer.appendChild(div);
        });

    } catch (error) {
        console.log(error);
    }
};

getProducts();