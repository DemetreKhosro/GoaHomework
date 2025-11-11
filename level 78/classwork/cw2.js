// 2) შექმენით მარტივი img slider პროექტი, რომელშიც გექნებათ 2 ღიალკი: prev, next წინა სურათზე დაბრუნებისა და შემდეგ სურათზე გადასვლისთვის, ღილაკებზე დაჭერით შესაბამისად უნდა გამოიტანოთ მომდევნო და უკანასკნელი სურათი

const images = [
    "http://www.sololearn.com/uploads/slider/1.jpg", 
    "http://www.sololearn.com/uploads/slider/2.jpg", 
    "http://www.sololearn.com/uploads/slider/3.jpg"
]; 

let imagesNumber = 0;
const img = document.getElementById('slider');
const nextBtn = document.getElementById('next');
const prevBtn = document.getElementById('prev');

function nextHandler() {
    imagesNumber++;

    if (index >= images.length) {
        index = 0;
    }
    img.src = images.index
}

function prevHandler() {
    imagesNumber--;

    index--;
    if (index < 0) {
        index = images.length - 1;
    }
    img.src = images[index];
}