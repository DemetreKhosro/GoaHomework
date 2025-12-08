const taskInput = document.getElementById('task-input');
const addBtn = document.getElementById('add-task-btn');
const taskList = document.getElementById('task-list');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function addTask(task) {
    const listItem = document.createElement('li');
    listItem.id = task.id;
    listItem.innerHTML = `
        <span>${task.text}</span>
        <button class="delete-btn" data-id="${task.id}">Delete</button>
    `;
    taskList.appendChild(listItem);
}

function renderTasks() {
    taskList.innerHTML = '';
    tasks.forEach(addTask);
}

function deleteTask(taskId) {
    tasks = tasks.filter(task => String(task.id) !== taskId);
    saveTasks();
    
    const itemToRemove = document.getElementById(taskId);
    if (itemToRemove) {
        itemToRemove.remove();
    }
}

addBtn.addEventListener('click', () => {
    const text = taskInput.value.trim();

    if (text) {
        const newTask = {
            id: Date.now(),
            text: text
        };

        tasks.push(newTask);
        addTask(newTask);
        saveTasks();
        taskInput.value = '';
    }
});

taskList.addEventListener('click', (e) => {
    if (e.target.classList.contains('delete-btn')) {
        const taskId = e.target.dataset.id;
        deleteTask(taskId);
    }
});

renderTasks();