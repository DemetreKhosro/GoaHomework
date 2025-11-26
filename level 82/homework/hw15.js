const books = [
    {title: "Pride and Prejudice", author: "Jane Austen"},
    {title: "The Great Gatsby", author: "F. Scott Fitzgerald"},
    {title: "Moby Dick", author: "Herman Melville"}
];

const formattedBooks = books.map(book => `${book.title} by ${book.author}`);

console.log(formattedBooks);