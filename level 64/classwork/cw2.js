//2) შექმენით ფორმა, რომელშიც სახელის, ემაილისა და პაროლის input-თან ერთად გექნებათ პრიბოების დამადასტურებელი checbox, როდესაც მოხდება ღილაკზე დაჭერა confirm ფუნქციით მომხმარებელს კითხეთ "Are you sure?" შემდეგ ამ ფუნქციიდან დაბრუნებული console-ში გამოიტანეთ

const btn = document.getElementById("btn")
const checkbox = document.getElementById("checkbox")
console.dir(checkbox)

btn.onclick = function() {
    console.dir(checkbox)
    let response = confirm("confirm to send information")
    console.log(response)
}