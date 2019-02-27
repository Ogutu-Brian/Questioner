"use strict"
import {urls} from './urls.js';
import {FormHandler} from './sharedLibrary.js';
//Class that handles forms on click of buttons
const loginButton = 'loginButton';
let loginFields = [
    'email',
    'password'
];
let loginHandler = new FormHandler(urls.loginUrl, loginFields);
document.getElementById(loginButton).addEventListener('click', login);
function login(event) {
    //function that handles login event
    event.preventDefault();
    fetch(loginHandler.getUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: loginHandler.Data
    }).then(response => response.json())
        .then(data => {
            if (data.status == 200) {
                localStorage.setItem("token", data.data[0].token);
                window.location.href = '../user/meetups.html';
            } else {
                window.alert(data.error);
            }
        })
}