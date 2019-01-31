"use strict"
//Class that handles forms on click of buttons
class FormHandler {
    constructor(url, fieldNames) {
        this.data = {};
        this.url = url;
        this.fieldNames = fieldNames;
    }
    //gets url
    get getUrl() {
        return this.url;
    }
    //creates the object to be posted
    createFormData() {
        for (let name of this.fieldNames) {
            this.data[name] = this.getFieldValue(name);
        }
    }
    //gets the data being posted
    get Data() {
        this.createFormData()
        return JSON.stringify(this.data);
    }
    getFieldValue(name) {
        return document.getElementById(name).value;
    }
}
const signupButton = 'postSignUp';
const signupUrl = 'http://127.0.0.1:5000/api/v2/auth/signup';
let fieldNames = [
    'firstname',
    'lastname',
    'password',
    'confirmpassword',
    'email',
    'username',
    'phoneNumber'
];
const signUp = new FormHandler(signupUrl, fieldNames);
document.getElementById("postSignUp").addEventListener('click', signup);
function signup(event) {
    event.preventDefault()
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
                window.location.href("../user/login.html");
            }
        })
}