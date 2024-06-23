const addTaskBtn = document.getElementById("add-task-btn");
const addTaskDiv = document.getElementById("add-task-container");
const modalBox = document.getElementById("modalbox");
const cancelBtn = document.getElementById("cancel-task");

cancelBtn.addEventListener('click',(e) => {
    // preventDefault();
    // modalBox.classList.add("d-none");
    modalBox.style.display = "none";
})

addTaskBtn.addEventListener('click',e => {
    modalBox.style.display = "flex";
    addTaskDiv.classList.add("d-block");
})