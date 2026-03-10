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
        addErrorTitle("Title must be filled out");
    }
    else if (destinationTitle.length < 2) {
        addErrorTitle("Title must be at least 2 characters");
    }
    else if (destinationTitle.length > 50) {
        addErrorTitle("Title cannot exceed 50 characters");
    }
});
/////////////// DESTINATION START DATE VALIDATION ///////////////
function addErrorStartDate(errormessage) {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("destination_start_date_errors").appendChild(li);
}
document.getElementById("formDestination").addEventListener("submit", (e) => {
    e.preventDefault();
    const destionationStartDate = document.getElementById("destination_start_date").value;
    document.getElementById("destination_start_date_errors").textContent = '';
    if (destionationStartDate.trim() == "") {
        addErrorStartDate("Start date must be filled out");
    }
});
/////////////// DESTINATION END DATE VALIDATION ///////////////
function addErrorEndDate(errormessage) {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("destination_end_date_errors").appendChild(li);
}
document.getElementById("formDestination").addEventListener("submit", (e) => {
    e.preventDefault();
    const destionationEndDate = document.getElementById("destination_end_date").value;
    document.getElementById("destination_end_date_errors").textContent = '';
    if (destionationEndDate.trim() == "") {
        addErrorEndDate("End date must be filled out");
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
    const destinationLocation = document.getElementById("destination_title").value;
    document.getElementById("destination_location_errors").textContent = '';
    if (destinationLocation.trim() == "") {
        addErrorLocation("Location must be filled out");
    }
    else if (destinationLocation.length < 2) {
        addErrorLocation("Location must be at least 2 characters");
    }
    else if (destinationLocation.length > 50) {
        addErrorLocation("Location cannot exceed 90 characters");
    }
});
/////////////// DESTINATION COUNTRY VALIDATION ///////////////
// function addErrorCountry(errormessage:string):void {
//     const li = document.createElement("li");
//     li.textContent = errormessage;
//     document.getElementById("destination_country_errors").appendChild(li)
// }
// document.getElementById("formDestination").addEventListener("submit", (e: Event) => {
//     e.preventDefault();
//     const destinationCountry = (document.getElementById("user_password") as HTMLInputElement).value;
//     document.getElementById("destination_country_errors").textContent = '';
//     if (destinationCountry.trim() == "") {
//     addPasswordErrorSignUp("Country must be filled out");
// }
// })
//# sourceMappingURL=destination.js.map