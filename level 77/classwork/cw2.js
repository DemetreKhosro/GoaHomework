let textarea = document.getElementById('message')
let counter = document.getElementById('counter')
const limit = 200

textarea.addEventListener('keydown', function(e) {
    let length = textarea.value.length
    counter.textContent = `${length} / ${limit}`
    if (length > limit) {
        counter.style.color = 'red'
    } else {
        counter.style.color = 'green'
    }
})