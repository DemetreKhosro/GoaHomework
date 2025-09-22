//1) შექმენით სახელისა და პაროლის შესტანი ველი და დამადასტურებელი ღილაკი. როდესაც ღილაკზე მოხდება დაჭერა (გამოიყენეთ onclick ატრიბუტი external javascript-ში) წამოიღეთ მომხარებლის სახელი და და პაროლი, გააერთიანეთ ისინი და გამოიტანეთ კონსოლში, კომენტარებით ახსენით კოდის ყველაა ნაწილს, ასევ დაიცავით საუკეთესო პრაქტიკები

// ვქმნით ცვლადებს
const username = document.getElementById("username")
const password = document.getElementById("password")
const submitButton = document.getElementById("btn")

// ვქმნით ფუნქციას რომ დამადასტურებელ ღილაკზე დაჭერის შემდეგ console-ში გამოვიდეს ინფორმაცია
submitButton.onclick = function() {
    console.log(username.value)
    console.log(password.value)
}