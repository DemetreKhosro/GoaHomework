let promiseStatus = "pending";

const internetPromise = new Promise((resolve, reject) => {
    const internetRequest = true;

    setTimeout(() => {
        if (internetRequest === true) {
            resolve("Internet Connected");
        } else {
            reject("No Internet");
        }
    }, 3000);
});

const interval = setInterval(() => {
    console.log("Promise status:", promiseStatus);
}, 500);

// promise არის ობიექტი რომელიც ასინქრონულ ოპერაციებს უშვებს და საშუალებას გვაძლევს რო გავაკონტროლოთ მათი შედეგი.
