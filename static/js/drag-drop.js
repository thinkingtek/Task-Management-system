const apiURL = 'http://127.0.0.1:8000/api-task-list/';
let tID;

// When start drag tID (will change to the ID of the task being dragged)
function dragStart(e) {
    const taskID = e.target.getAttribute("data-index")
    tID = taskID;
}

// Getting the current task details in Object format, so it can be replace the updatedTask func
async function taskDetails(updateStatus) {
    const taskID = tID;
    const detailURL = `api-task-details/${taskID}/`;
    parseInt(taskID);

    let updateData = {}

    const response = await fetch(detailURL)
    if (!response.ok) {
        throw new Error('Network response was not OK');
    }
    const data =  await response.json()
    .then(data => {
        updateData = data
        updateData.status = updateStatus;
    })
    return updateData;
}

// Func to update the specific task
function updateTask(updateData) {
    const taskID = tID;
    parseInt(taskID);
    const updateURL = `api-task-update/${taskID}/`;

    fetch(updateURL, {
        method: 'PUT',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(updateData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not OK")
        }
        return response.json();
    })
    .catch(error => {
        console.log(error.message);
    });
}

// drop event to update the DOM
async function drop(event) {
    event.preventDefault();
    let status = event.target.querySelector("p");

    if (status.classList.contains("inprogress-p")) {
        const response = await taskDetails("in progress")
        .then((data) => {
            updateTask(data);
            status.innerHTML = `<p class="inprogress-p">"${data.title}" updated</p>`;
        });
    }
    if (status.classList.contains("completed-p")) {
        const response = await taskDetails("completed")
        .then((data) => {
            updateTask(data);
            status.innerHTML = `<p class="completed-p">"${data.title}" updated</p>`;
        });
    }
    if (status.classList.contains("overdue-p")) {
        const response = await taskDetails("overdue")
        .then((data) => {
            updateTask(data);
            status.innerHTML = `<p class="overdue-p">"${data.title}" updated</p>`;
        });
    }
    
}

function dragEnter(e) {
    e.target.classList.add("drag-enter");
}
function dragOver(event) {
    event.preventDefault();
}
function dragLeave(event) {
    event.target.classList.remove("drag-enter");
}

// Adding event listeners for draggables div 
function addEventListeners() {
    const draggables = document.querySelectorAll(".draggables");
    // const taskStatusDiv = document.querySelectorAll(".status-grid");

    draggables.forEach(draggable => {
        draggable.addEventListener('dragstart',(e) => dragStart(e));
    });

    // To add event listners for each Status DIV
    // taskStatusDiv.forEach(div => {
    //     div.addEventListener('dragover', dragOver);
    //     div.addEventListener('drop', drop);
    //     div.addEventListener('dragenter', dragEnter);
    //     div.addEventListener('dragleave', dragLeave);

    // });
    
}

addEventListeners();