const movie = {
    title: "Blade Runner 2049",
    director: "Denis Villeneuve",
    year: 2017,
    country: "USA"
};

const { year, country, ...details } = movie;
console.log(year, country);
console.log(details);