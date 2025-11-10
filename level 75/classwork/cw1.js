//1) ახსენით როგორ გესმით ტერმიენბი lexical scope და hoisting, დაწერეთ რა გასნხვავებაა var-ითა და let-ით შექმნილ ცვლადებს შორის მოიყვანეთ ყველაფრის მაგალითები

// lexical scope - სადამდე შეგვძლია მივწვდეთ ცვლადს
// hoisting - როცა javascript ახდენს ყველა ფუნქციის ინციალიზაციას კოდის გაშვებამდე

// var-ით შექმნილი ცვლადი არის გლობალური და ხელმისაწვდომია ყველგან
// let ცვლადი მხოლოდ ხელმისაწვდომია იქ სადაც შევქმნით

function OuterScope() {
    let username = 'demetre'

    function InnerScope() {
        let username = username + 'khosro'
        console.log(username)
    }

    console.log(username)
}
OuterScope()