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
const loginButton = 'loginButton';
const loginUrl = 'http://127.0.0.1:5000/api/v2/auth/login';
let loginFields = [
    'email',
    'password'
];
let loginHandler = new FormHandler(loginUrl, loginFields);
document.getElementById(loginButton).addEventListener('click', login);
function login(event) {
    event.preventDefault();
    fetch(loginHandler.getUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: loginHandler.Data
    }).then(response => response.json())
        .then(data => {
            if (data.status != 200) {
                window.alert(data.error[0])
            }
        })
}