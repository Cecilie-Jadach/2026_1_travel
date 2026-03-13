/////////////// DESTINATION TITLE VALIDATION ///////////////
function addErrorTitle(errormessage) {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("destination_title_errors").appendChild(li);
}
document.getElementById("formDestination").addEventListener("submit", (e) => {
    e.preventDefault();
    const destinationTitle = document.getElementById("destination_title").value;
    document.getElementById("destination_title_errors").textContent = '';
    if (destinationTitle.trim() == "") {
        addErrorTitle("Title is required.");
    }
    else if (destinationTitle.length < 2) {
        addErrorTitle("Title must be at least 2 characters.");
    }
    else if (destinationTitle.length > 50) {
        addErrorTitle("Title cannot exceed 50 characters.");
    }
});
/////////////// DESTINATION DATE VALIDATION ///////////////
function addErrorDate(targetId, errormessage) {
    const li = document.createElement("li");
    li.textContent = errormessage;
    // Find den specifikke liste baseret på targetId
    const targetList = document.getElementById(targetId);
    if (targetList) {
        targetList.appendChild(li);
    }
}
document.getElementById("formDestination").addEventListener("submit", (e) => {
    e.preventDefault();
    const startDateVal = document.getElementById("destination_start_date").value;
    const endDateVal = document.getElementById("destination_end_date").value;
    document.getElementById("destination_start_date_errors").textContent = '';
    document.getElementById("destination_end_date_errors").textContent = '';
    // 1. Tjek start dato - sendes kun til start_date_errors
    if (startDateVal.trim() == "") {
        addErrorDate("destination_start_date_errors", "Start date is required.");
    }
    // 2. Tjek slut dato - sendes kun til end_date_errors
    if (endDateVal.trim() == "") {
        addErrorDate("destination_end_date_errors", "End date is required.");
    }
    // 3. Sammenligning - sendes kun til end_date_errors
    if (startDateVal && endDateVal) {
        const start = new Date(startDateVal);
        const end = new Date(endDateVal);
        if (end < start) {
            addErrorDate("destination_end_date_errors", "End date cannot be before start date.");
        }
    }
});
/////////////// DESTINATION LOCATION VALIDATION ///////////////
function addErrorLocation(errormessage) {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("destination_location_errors").appendChild(li);
}
document.getElementById("formDestination").addEventListener("submit", (e) => {
    e.preventDefault();
    const destinationLocation = document.getElementById("destination_location").value;
    document.getElementById("destination_location_errors").textContent = '';
    if (destinationLocation.trim() == "") {
        addErrorLocation("Location is required.");
    }
    else if (destinationLocation.length < 2) {
        addErrorLocation("Location must be at least 2 characters.");
    }
    else if (destinationLocation.length > 50) {
        addErrorLocation("Location cannot exceed 90 characters.");
    }
});
/////////////// CONFIRMATION DIALOG FOR DELETION MODAL FUNCTIONALITY ///////////////
function toggleModal(pk) {
    const modal = document.querySelector(`#modal-${pk}`);
    if (modal) {
        // add or remove the class hidden
        modal.classList.toggle('hidden');
    }
}
//# sourceMappingURL=destination.js.map