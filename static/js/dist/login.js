/////////////// LOGIN EMAIL VALIDATION ///////////////
function addEmailErrorLogin(errormessage) {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("email_errors_login").appendChild(li);
}
document.getElementById("formLogin").addEventListener("submit", (e) => {
    e.preventDefault();
    const emailLogin = document.getElementById("user_email_login").value;
    document.getElementById("email_errors_login").textContent = '';
    if (emailLogin.trim() == "") {
        addEmailErrorLogin("Email is required.");
    }
    else {
        if (!emailLogin.includes("@")) {
            addEmailErrorLogin("Email must include a @");
        }
    }
});
/////////////// LOGIN PASSWORD VALIDATION ///////////////
function addPasswordErrorLogin(errormessage) {
    const li = document.createElement("li");
    li.textContent = errormessage;
    document.getElementById("password_errors_login").appendChild(li);
}
document.getElementById("formLogin").addEventListener("submit", (e) => {
    e.preventDefault();
    const password = document.getElementById("user_password_login").value;
    document.getElementById("password_errors_login").textContent = '';
    if (password.trim() == "") {
        addPasswordErrorLogin("Password is required.");
    }
});
//# sourceMappingURL=login.js.map