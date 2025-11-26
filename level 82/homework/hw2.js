const user = {
    name: 'Demetre',
    age: 14
}

const details = {
    country: 'Georgia',
    city: 'Tbilisi'
}

const fullUser = { 
    ...user,
    ...details 
};

// ...  ამატებს ობიექტების მნიშვნელობებს fullUser-ში

console.log(fullUser);