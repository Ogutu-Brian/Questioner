"use strict"
import {
    urls
} from './urls.js';
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
export {
    FormHandler,
    signup
};