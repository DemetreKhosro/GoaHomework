//1) ვებგვერდზე მომხმარებელს prompt-ის გამოყენებით შემოტანინეთ თაივსი გამოცდისა და აქტიურობის ქულები, შემდეგ გარდაქმენით ისინი რიცხვებად Numbert ან ParseInt ფუნქციების გამოყენებით, შემდეგ შეკრიბეთ და შეამოწმეთ თუ როემლ კატეროგიაში მოხვდა ეს ქულა, რის მიხედვითაც გამოუტანთ მოსწავლეს შეფასბეას

// -A 90-100
// -B 80-90
// -C 70-80
// -D 50-70
// -E 30-50
// F <30

function checkGrade() {
    let exam = Number(prompt("Enter exam score"))
    let activity = Number(prompt("Enter activity score"))

    let total = exam + activity
    let grade

    if (total >= 90 && total <=100) {
        grade = 'A'
    } else if (total >= 80 && total < 90) {
        grade = 'B'
    } else if (total >= 70 && total < 80) {
        grade = 'C'
    } else if (total >= 50 && total < 70) {
        grade = "D";
    } else if (total >= 30 && total < 50) {
        grade = "E";
    } else {
        grade = "F";
    }
}