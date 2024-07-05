const loader = document.querySelector(".loader-container");
const apiError = document.getElementById("fetchError");
const taskContainer = document.querySelector(".tasks-container");
const apiURL = 'http://127.0.0.1:8000/api-task-list/';

// hide & show loader
function showLoader() {
    loader.classList.add("flex");
    loader.classList.remove("d-none");
}
function hideLoader() {
    loader.classList.remove("flex");
    loader.classList.add("d-none");
}

// Displaying fetched or filtered Tasks in the DOM
const htmlFunc = (tasks) => {
    const tasksContainer = document.getElementById("task-grid-container");
    tasksContainer.innerHTML = "";

    tasks.forEach(task => {
        const tasksDiv = document.createElement('div');
        tasksDiv.setAttribute('id',task.id);

        tasksDiv.innerHTML = `
            <div class="grid align-ctr three-containers-grid priority-time-category">
                <div class="priority">${task.priority}</div>
                <div class="flex-ctr justify-ctr time">
                    <img src="static/img/icons/icons8-time-50.png" alt="" srcset="">
                    ${new Date(task.timestamp).toLocaleTimeString()}
                </div>
                <div class="category">${task.category}</div>
            </div>
            <div class="task-details">
                <div class="flex flex-btw task-title">
                    <a href="task-details/${task.id}/">${task.title}</a>
                    <img src="static/img/icons/icons8-menu-vertical-50.png" alt="" srcset="">
                </div>
                <p class="task-desc">
                    ${task.description}
                </p>
                <div class="flex-ctr task-date">
                    <img src="static/img/icons/icons8-calender-64.png" alt="" srcset="">
                    ${new Date(task.due_date).toLocaleDateString()}
                </div>
                <div class="flex flex-btw users-icons">
                    <div class="relative flex profile-pix">
                        <img src="static/img/profile-pic.jpg" alt="" srcset="" class="cover circle">
                        <img src="static/img/profile-pic.jpg" alt="" srcset="" class="cover circle">
                        <img src="static/img/profile-pic.jpg" alt="" srcset="" class="cover circle">
                    </div>
                    <div class="flex-ctr icons-div">
                        <img src="static/img/icons/icons8-eye-50.png" alt="" srcset="">
                        <img src="static/img/icons/icons8-trash-can-100.png" alt="" srcset="">
                        <a href="task-update/${task.id}/" class="edit-task">
                            <img src="static/img/icons/icons8-edit-32.png" alt="" srcset="">
                        </a>
                    </div>
                </div>
            </div>
        `;
    tasksContainer.appendChild(tasksDiv)
    });
}

// Fecting from API
async function fetchTasks() {
    const response = await fetch(apiURL)
    if (!response.ok) {
        throw new Error('Network response was not OK');
    }
    const data =  await response.json();
    return data;
}

// Fetching Tasks
async function taskLists() {
    const data = await fetchTasks()
    .then((tasks) => {
        setTimeout(() => {
            taskContainer.classList.remove("d-none");
            hideLoader();
            htmlFunc(tasks);
            console.log("------Fetching all Task lists---------");
        }, 500);
    })
    .catch(error => {
        hideLoader();
        apiError.innerText = error.message;
    });
}


// Search Filtering
async function searchTaskForm(event) {  
    event.preventDefault(); 
    const input = document.getElementById("search-input");
    showLoader();
    taskContainer.classList.add("d-none");
    console.log(input.value.toLowerCase().trim());
    const lowerCaseIput = input.value.toLowerCase().trim();
    const data = await fetchTasks()
    .then((tasks) => {
        const flteredtasks = tasks.filter(task => task.title.toLowerCase().includes(lowerCaseIput));
        console.log(flteredtasks);
        setTimeout(() => {
            taskContainer.classList.remove("d-none");
            hideLoader();
            htmlFunc(flteredtasks)
        }, 500);
    })
    .catch(error => {
        hideLoader();
        apiError.innerText = error.message;
    });
    
}
// Filter tasks based on proirity and status
async function filterTasks(event) {   
    showLoader();
    taskContainer.classList.add("d-none");
    const input = event.target.value;
    const data = await fetchTasks()
    .then((tasks) => {
        const flteredtasks = tasks.filter(task => task.status == input || task.priority == input);
        console.log(flteredtasks);
        setTimeout(() => {
            taskContainer.classList.remove("d-none");
            hideLoader();
            htmlFunc(flteredtasks)
        }, 500);
    })
    .catch(error => {
        hideLoader();
        apiError.innerText = error.message;
    });
    
}
// get sorted tasks
function sortTasks(event) {   
    console.log(event.target.value);
    // fetchTasks();
}

window.onload = taskLists;