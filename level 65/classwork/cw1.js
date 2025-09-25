//1)  შექმენით 3 ობიექტი: მებრძოლის, პროდუქტის და პიროვნების. თითეულში უნდა იყოს მინიუმუმ 3 კუთვნილება და 1 მეთოდი, კომენტარებით დაწერეთ რა არის ობიექტი, როგორ იქმება და რაში ვიყენებთ. ასევე ახსენით თქვენი სიტყვებით docment-ის ობიექტი

const fighter = {
    name: 'Samurai',
    health: 100,
    stamina: 200,
    isAlive: true,
    enemyHealth: 30,
    damage: 30,
    attack: function (opponent) {
        console.log('Slash dealt 30 damage')
        console.enemyHealth = console.enemyHealth - console.damage 
        console.log('Enemy eliminated')
    }
}

const product = {
    name: 'PC',
    price: '1000$',
    inStock: true,
    info: function() {
        console.log(this.name + " ღირს " + this.price + " ლარი.")
    }
}

const person = {
    name: "Demetre",
    age: 14,
    city: "Tbilisi",
    info: function() {
        console.log(`${person.name} lives in ${person.city} and is ${person.age} years old`)
    }
}

// დოკუმენტი არის ობიექტი ბრაუზერში რომელიც წარმოადგენს მთლიან ვებგვერდს
// მას ვიყენებთ რომ HTML ელემენტები ვმართოთ JS-ით მაგალითად getElementById