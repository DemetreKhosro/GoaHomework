//1) შექმენით task ობიექტის კონსტრუქტორი რომელსაც ექნება 5 კუთვნილება: title, desc, state, deadline, complete (მეთოდი), შექმენით მინიმუმ 3 ობიექტი და თითოეულზე გამოიძახეთ complete მეთოდი, საბოლოოდ გამოიტანეთ ყველა, კომენტარებით ახსენით რა არის ობიექტი და ჩამოწერეთ მისი 3-ვე ტიპის თვისება

function Task(title, desc, state, deadline) {
    this.title = title,
    this.desc = desc,
    this.state = state,
    this.deadline = deadline,
    this.complete = function() {
        this.state = !this.state
    }
}

let classwork = new Task('Classwork', 'Group 64 level 70 web-dev', true, '12-10-2025');
let homework = new Task('Homework', 'Group 64 level 70 web-dev', false, '14-10-2025');
let practice = new Task('Practice', 'Codewars', false, '14-10-2025')

classwork.complete()
homework.complete()
practice.complete()

console.log(classwork)
console.log(homework)
console.log(practice)

// ობიექტი არის მონაცემთა სტრუქტურა რომელიც ინახავს მონაცემებს და ფუნქციებს
// თვისებები აღწერენ ობიექტის მდგომარეობას, ხოლო მეთოდები - მის მოქმედებებს