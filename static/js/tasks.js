const loader = document.querySelector(".loader-container");
const apiError = document.getElementById("fetchError");
const taskContainer = document.querySelector(".tasks-container");
const noTasks = document.querySelector(".no-task");
const now  = new Date();

// hide & show loader
function showLoader() {
    loader.classList.add("flex");
    loader.classList.remove("d-none");
}
function hideLoader() {
    loader.classList.remove("flex");
    loader.classList.add("d-none");
}

// hide & show Task container
function showTaskContainer() {
    taskContainer.classList.remove("d-none");
}
function hideTaskContainer() {
    taskContainer.classList.add("d-none");
}

// hide and show no Task
function showEmptyTag() {
    noTasks.classList.remove("d-none");
}
function hideEmptyTag() {
    noTasks.classList.add("d-none");
}
 // Function to truncate the description
//  truncate strings
//  function truncateDescription(description, maxLength) {
//     if (description.length > maxLength) {
//         return description.substring(0, maxLength) + '...';
//     }
//     return description;
// }
// truncate words
function truncateDescription(description, maxWords) {
    const words = description.split(' ');
    if (words.length > maxWords) {
        return words.slice(0, maxWords).join(' ') + '...';
    }
    return description;
}

// Displaying fetched or filtered Tasks in the DOM
const htmlFunc = (tasks) => {
    const tasksContainer = document.getElementById("task-grid-container");
    tasksContainer.innerHTML = "";

    tasks.forEach(task => {
        hideEmptyTag();
        // Truncate to 30 characters
        const truncatedDescription = truncateDescription(task.description, 30); 
        const tasksDiv = document.createElement('div');
        tasksDiv.setAttribute('data-index',task.id);

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
                    <a href="task-details/${task.id}/" draggable="true" data-index="${task.id}" class="draggables grabbing">${task.title}</a>
                    <img src="static/img/icons/icons8-drag-and-drop-no-outline-24-1×.png" alt="" srcset="">
                </div>
                <p class="task-desc">
                    ${truncatedDescription}
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
    
    tasksContainer.appendChild(tasksDiv);
    });

    if (tasks.length < 1) {
        showEmptyTag();
    }

    addEventListeners();
}

// Fecting from API
async function fetchTasks() {
    const response = await fetch(apiURL);
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
    hideTaskContainer();
    console.log(input.value.toLowerCase().trim());
    const lowerCaseIput = input.value.toLowerCase().trim();
    const data = await fetchTasks()
    .then((tasks) => {
        const filteredtasks = tasks.filter(task => task.title.toLowerCase().includes(lowerCaseIput));
        console.log(filteredtasks);
        setTimeout(() => {
            showTaskContainer();
            hideLoader();
            htmlFunc(filteredtasks)
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
    hideTaskContainer();
    const input = event.target.value;
    const data = await fetchTasks()
    .then((tasks) => {
        const filteredtasks = tasks.filter(task => task.status == input || task.priority == input);
        console.log(filteredtasks);
        setTimeout(() => {
            showTaskContainer();
            hideLoader();
            htmlFunc(filteredtasks)
        }, 500);
    })
    .catch(error => {
        hideLoader();
        apiError.innerText = error.message;
    });
    
}

// get sorted tasks
async function sortTasks(event) {   
    showLoader();
    hideTaskContainer();
    const input = event.target.value;
    const data = await fetchTasks()
    .then((tasks) => {
        let flteredtasks = tasks;
        if (input == "decending") {
            flteredtasks = tasks.sort((a, b) => new Date(b.due_date) - new Date(a.due_date));
        }else {flteredtasks = tasks.sort((a, b) => new Date(a.due_date) - new Date(b.due_date));}

        setTimeout(() => {
            showTaskContainer();
            hideLoader();
            htmlFunc(flteredtasks)
        }, 500);
    })
}

window.onload = taskLists;