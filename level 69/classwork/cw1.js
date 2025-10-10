//1) შექმენით ვებგვერდი რომელზეც გექნებათ სარეგისტრაციო ფორმა სახელის, ემაილისა და პაროლის შესატანი ველებით, ასევე დამდასტურებელი ღილაკით. როდესაც მომხმარებელი გააგზავნის ინფორმაციას ღილაკზე დაჭერით, თქვენ ეს ინფორმაცია უნდა შეინახოთ (პირობითად) dataBase სიაში ობიექტის სახით, ესეიგი წამოღეთ ყველა HTML-ის ელემენტი javascript-ში შემდეგ ღილაკზე onclick მოვლენისას შექმენით ახალი ანგარიშის (account) ობიექტი რომელშიც მოცემუილი იქნება მომხარებლის სახელი, ემაილი და პაროლი. დამატების შემდეგ გვერდზე გაასუფთავეთ შესატანი ველები, თითოეული account ობიექტი დაამატეთ dataBase მასივში. დაამატეთ კიდევ ერთი ღილაკი ტექსტით print data რომელზე დაჭერისასაც დაიბეჭდება dataBase მასივი

const form = document.querySelector('form');
const submitBtn = document.getElementById('submitBtn');

const name = form.elements.username;
const email = form.elements.email;
const password = form.elements.password;

let dataBase = [];

submitBtn.onclick = function() {
    const account = {
        username: name.value,
        email: email.value,
        password: password.value
    }

    name.value = '';
    email.value = '';
    password.value = '';

    dataBase.push(account)
}

printData.onclick = function() {
    console.log(dataBase)
}