let form = document.querySelector('form')
let submitBtn = document.getElementById('submitBtn')

let table = document.createElement('table')
table.border = "1";
table.style.marginTop = "20px";
document.body.appendChild(table);

table.innerHTML = `
<tr>
    <th>Full Name</th>
    <th>Email</th>
    <th>Phone Number</th>
    <th>Gender</th>
    <th>Password</th>
</tr>
`

submitBtn.addEventListener('click', function(e) {
    e.preventDefault();
    let name = document.getElementById('fullName').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phoneNum').value;
    let password = document.getElementById('password').value;
    let genderInput = document.querySelector('input[name="gender"]:checked');
    let gender = genderInput ? genderInput.value : '';
    let terms = document.getElementById('terms');

    if (!terms.checked) {
        alert('You must agree to the terms and conditions before submitting.');
        return;
    }

    let newRow = container(name, email, phone, gender, password);
    presentational(newRow);
    form.reset();
})

function container(name, email, phone, gender, password) {
    let tr = document.createElement('tr');
    tr.innerHTML = `
    <td>${name}</td>
    <td>${email}</td>
    <td>${phone}</td>
    <td>${gender}</td>
    <td>${password}</td>
    `;
    return tr;
}

function presentational(row) {
    table.appendChild(row)
}
