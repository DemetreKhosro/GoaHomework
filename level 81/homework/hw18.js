const school = {
    name: "118 Public School",
    director: {
        firstName: "Demetre",
        lastName: "Khosroshvili"
    }
};

const { director: { firstName, lastName } } = school;
console.log(`${firstName} ${lastName}`);