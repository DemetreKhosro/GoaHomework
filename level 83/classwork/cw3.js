fetch("https://jsonplaceholder.typicode.com/todos")
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        let output = "";

        data.forEach(function(item) {
            output += `
                <p>
                    ID: ${item.id}<br>
                    Title: ${item.title}<br>
                    Completed: ${item.completed}
                </p>
                <hr>
            `;
        });

        document.getElementById("todos").innerHTML = output;
    })
    .catch(function(error) {
        console.log(error);
    });
