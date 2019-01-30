"use strict"
document.getElementById("postSingup").addEventListener('click', signUp)
function signUp(event) {
    event.preventDefault()
    let firstName = document.getElementById('firstName').value;
    let lastName = document.getElementById('lastName').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirmPassword').value;
    let phoneNumber = document.getElementById('phone').value;
    let userName = document.getElementById('username').value;
    fetch('http://127.0.0.1:5000/api/v2/auth/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        cache: "force-cache",
        body: JSON.stringify({
            firstname: firstName,
            lastname: lastName,
            email: email,
            password: password,
            confirmpassword: confirmPassword,
            username: userName,
            phoneNumber: phoneNumber
        })
    }).then(response => response.json())
        .then(data => {
            if (data.status != 201) {
                window.alert(data.error[0].message);
            }
            else {
                window.location.href = "../user/signup.html";
            }
        })
}