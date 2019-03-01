"use strict"
import {
    urls
} from './urls.js';
import {
    FormHandler
} from './sharedLibrary.js';
const signupButton = 'postSignUp';
let singupFieldNames = [
    'firstname',
    'lastname',
    'password',
    'confirmpassword',
    'email',
    'username',
    'phoneNumber'
];
const signUp = new FormHandler(urls.signupUrl, singupFieldNames);
document.getElementById(signupButton).addEventListener('click', signup);

function signup(event) {
    //Function that handles sign up event
    event.preventDefault();
    fetch(signUp.getUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: signUp.Data
        }).then(response => response.json())
        .then(data => {
            if (data.status != 201) {
                window.alert(data.error[0].message);
            } else {
                window.location.href = "../user/login.html";
            }
        })
}