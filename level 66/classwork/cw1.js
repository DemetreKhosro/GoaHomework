//1) შექმენით ლოგიკური ოპერაციების ტესტიერების გვერდი, რომელზეც გექნებათ და ლოგიკური ოპერაცია, უნდა გქონდეთ 2 შესატანი checkbox boolean მნიშვნლობებისთვის, დამადასტურებელი ღილაკი და შედეგის საჩვენებელი პარაგრაფი, ყველა ეს ელემენტი შეინახეთ javascript-ის ცვლლადში და როდესაც მოხდება ღილაკზე დაჭერა მომხამრებლის შემოტანილი მნიშვნელობებს შორის შეასრულეთ და ლოგიკური ოპერაცია და გამოიტანეთ პარაგრაფის შედეგად

let checkbox1 = document.getElementById("value1")
let checkbox2 = document.getElementById('value2')
let button = document.getElementById('checkBtn')
let resultPara = document.getElementById('result')

button.onclick = function() {
    let val1 = checkbox1.checked
    let val2 = checkbox2.checked
    let result = val1 && val2

    resultPara.textContent = 'result: ' + result
}