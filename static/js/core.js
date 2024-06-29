const delTaskBtn = document.getElementById("deltask-btn");
const addTaskBtn = document.getElementById("add-task-btn");
const addTaskDiv = document.getElementById("add-task-container");
const deleteTaskDiv = document.getElementById("delete-task-container");
const modalBox = document.getElementById("modalbox");
const cancelBtn = document.getElementById("cancel-task");

// cancelBtn.addEventListener('click',(e) => {
//     modalBox.style.display = "none";
// })

// cancel modal
function closeModal() {
    modalBox.style.display = "none";
    addTaskDiv.style.display = "none";
    deleteTaskDiv.style.display = "none";
}
addTaskBtn.addEventListener('click',e => {
    modalBox.style.display = "flex";
    addTaskDiv.style.display = "block";
    // addTaskDiv.classList.add("d-block");
})
delTaskBtn.addEventListener('click',e => {
    modalBox.style.display = "flex";
    addTaskDiv.style.display = "none";
    deleteTaskDiv.style.display = "block";
})