const displayText = document.getElementById('displayText');
const savedText = sessionStorage.getItem('text');
displayText.textContent = savedText ? savedText : 'No text found.';