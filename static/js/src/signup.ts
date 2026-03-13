/////////////// SIGNUP FIRST NAME VALIDATION ///////////////
function addErrorFirstName(errormessage:string):void {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("user_first_name_errors_signup").appendChild(li)
}

document.getElementById("formSignup").addEventListener("submit", (e: Event) => {
    e.preventDefault();
    const firstNameSignup = (document.getElementById("user_first_name") as HTMLInputElement).value;

    document.getElementById("user_first_name_errors_signup").textContent = '';

    if (firstNameSignup.trim() == "") {
    addErrorFirstName("First name is required."); 
    }
    else if
    (firstNameSignup.length < 2) {
    addErrorFirstName("First name must be at least 2 characters");
    }
    else if 
    (firstNameSignup.length > 20) {
        addErrorFirstName("First name cannot exceed 20 characters");
    }
})

/////////////// SIGNUP LAST NAME VALIDATION ///////////////
function addErrorLastName(errormessage:string):void {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("user_last_name_errors_signup").appendChild(li)
}

document.getElementById("formSignup").addEventListener("submit", (e: Event) => {
    e.preventDefault();
    const lastNameSignup = (document.getElementById("user_last_name") as HTMLInputElement).value;

    document.getElementById("user_last_name_errors_signup").textContent = '';

    if (lastNameSignup.trim() == "") {
    addErrorLastName("Last name is required."); 
    }
    else if
    (lastNameSignup.length < 2) {
    addErrorLastName("Last name must be at least 2 characters");
    }
    else if 
    (lastNameSignup.length > 20) {
        addErrorLastName("Last name cannot exceed 20 characters");
    }
})

/////////////// SIGNUP EMAIL VALIDATION ///////////////
function addEmailErrorSignUp(errormessage:string):void {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("email_errors_signup").appendChild(li)
}

document.getElementById("formSignup").addEventListener("submit", (e: Event) => {
    e.preventDefault();
    const emailSignup = (document.getElementById("user_email") as HTMLInputElement).value;

    document.getElementById("email_errors_signup").textContent = '';

    if (emailSignup.trim() == "") {
    addEmailErrorSignUp("Email is required.");
    } else {
    if(!emailSignup.includes("@")) {
    addEmailErrorSignUp("Email must include a @")
    }}
})

/////////////// SIGNUP PASSWORD VALIDATION ///////////////
function addPasswordErrorSignUp(errormessage:string):void {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("password_errors_signup").appendChild(li)
}

document.getElementById("formSignup").addEventListener("submit", (e: Event) => {
    e.preventDefault();
    const passwordSignup = (document.getElementById("user_password") as HTMLInputElement).value;

    document.getElementById("password_errors_signup").textContent = '';

    if (passwordSignup.trim() == "") {
    addPasswordErrorSignUp("Password is required.");
}
})
