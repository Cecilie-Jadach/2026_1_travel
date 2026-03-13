/////////////// LOGIN EMAIL VALIDATION ///////////////
function addEmailErrorLogin(errormessage:string):void {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("email_errors_login").appendChild(li)
}

document.getElementById("formLogin").addEventListener("submit", (e: Event) => {
    e.preventDefault();
    const emailLogin = (document.getElementById("user_email_login") as HTMLInputElement).value;

    document.getElementById("email_errors_login").textContent = '';

    if (emailLogin.trim() == "") {
    addEmailErrorLogin("Email is required.");
    } else {
    if(!emailLogin.includes("@")) {
    addEmailErrorLogin("Email must include a @")
    }}
})

/////////////// LOGIN PASSWORD VALIDATION ///////////////
function addPasswordErrorLogin(errormessage:string):void {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("password_errors_login").appendChild(li)
}

document.getElementById("formLogin").addEventListener("submit", (e: Event) => {
    e.preventDefault();
    const password = (document.getElementById("user_password_login") as HTMLInputElement).value;

    document.getElementById("password_errors_login").textContent = '';

    if (password.trim() == "") {
    addPasswordErrorLogin("Password is required.");
} else if
    (password.length < 2) {
    addPasswordErrorLogin("Password must be at least 8 characters.");
    }
})