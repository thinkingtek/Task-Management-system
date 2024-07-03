const tasksContainer = document.querySelector("#task-grid-container");
const loader = document.querySelector(".loader-container");
const apiError = document.getElementById("fetchError");


// hide & show loader
function showLoader() {
    loader.classList.add("d-block");
}
function hideLoader() {
    loader.classList.add("d-none");
}

// Getting Tasklist from an API
function taskList() {
    const taskContainer = document.querySelector(".tasks-container");
    const taskListUrl = 'http://127.0.0.1:8000/api-task-list/';

    fetch(taskListUrl)
        .then(res => {
            if (!res.ok) {
                throw new Error('Network response was not OK');
            }
            return res.json()
        })
        .then(data => {
            console.log(data);
            setTimeout(() => {
                taskContainer.classList.remove("d-none");
                hideLoader();
                const tasks = data;
    
                for (const taskItem in tasks) {
                    const taskDiv = `
                    <div id="task-list-wrapper-${tasks[taskItem].pk}">
                    <div class="grid align-ctr three-containers-grid priority-time-category">
                        <div class="priority">${tasks[taskItem].priority}</div>
                        <div class="flex-ctr justify-ctr time">
                            <img src="static/img/icons/icons8-time-50.png" alt="" srcset="">
                            ${new Date(tasks[taskItem].timestamp).toLocaleTimeString()}
                        </div>
                        <div class="category">${tasks[taskItem].category}</div>
                    </div>
                    <div class="task-details">
                        <div class="flex flex-btw task-title">
                            <a href="task-details/${tasks[taskItem].id}/">${tasks[taskItem].title}</a>
                            <img src="static/img/icons/icons8-menu-vertical-50.png" alt="" srcset="">
                        </div>
                        <p class="task-desc">
                            ${tasks[taskItem].description}
                        </p>
                        <div class="flex-ctr task-date">
                            <img src="static/img/icons/icons8-calender-64.png" alt="" srcset="">
                            ${new Date(tasks[taskItem].due_date).toLocaleDateString()}
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
                                <a href="task-update/${tasks[taskItem].id}/" class="edit-task">
                                    <img src="static/img/icons/icons8-edit-32.png" alt="" srcset="">
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                    `
                tasksContainer.innerHTML += taskDiv;
                };
            }, 1500);
        })
        .catch(error => {
            hideLoader();
            apiError.innerText = error.message;
        })
}


taskList();