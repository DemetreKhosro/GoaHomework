//1) შექმენით 3 product კლასის მქონე div ელემენტი, პირველ ელემენტს მიანიჭეთ ასევე გასნხვავბული id და ჩაწერეთ მასში 2 თქვენთვის სასურველი ელემენტი, შემდეგ გამოიყეენთ ყველა ეს document-ის მეთოდი: getElementsByTagName, getElementsByClassName, previousElementSibling, nextgElementSibling, firstChild, lastChild და კომენტარებით ახსენით როგორ მუშაობს თითოეული, ასევე დაწერეთ თუ რა არის DOM

const headers = document.getElementsByClassName('headers');
console.log(headers);

const h1 = document.querySelector('.headers');
console.log(h1.previousElementSibling)
console.log(h1.nextElementSibling)

const container = document.getElementById('container');
console.log(container.firstChild)
console.log(container.lastChild)

// DOM - html მონაცემების სტრუქტურა ობიექტების სახით (ობიექტების ხე)