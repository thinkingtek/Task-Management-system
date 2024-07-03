const delTaskBtn = document.getElementById("deltask-btn");
const addTaskBtn = document.getElementById("add-task-btn");
const addTaskDiv = document.getElementById("add-task-container");
const deleteTaskDiv = document.getElementById("delete-task-container");
const modalBox = document.getElementById("modalbox");
const cancelBtn = document.getElementById("cancel-task");

// cancelBtn.addEventListener('click',(e) => {
//     modalBox.style.display = "none";
// })

// Close modal
function closeModal() {
    modalBox.style.display = "none";
    addTaskDiv.style.display = "none";
    // deleteTaskDiv.style.display = "none";
    deleteTaskDiv ? deleteTaskDiv.style.display = "none": "" ;
}

// add task (Opens modal and add task container)
function addTask() {
    modalBox.style.display = "flex";
    addTaskDiv.style.display = "block";
    // addTaskDiv.classList.add("d-block");
}

// Delete Task
function delTask() {
    modalBox.style.display = "flex";
    addTaskDiv.style.display = "none";
    deleteTaskDiv.style.display = "block";
}
