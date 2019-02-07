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
        this.data['meetup'] = localStorage.getItem('meetupId');
        return JSON.stringify(this.data);
    }
    getFieldValue(name) {
        return document.getElementById(name).value;
    }
}
let questionUrl = 'https://questioner-api-v2.herokuapp.com/api/v2/questions';
let questionButton = 'postQuestion';
let fieldNames = [
    "title",
    "body"
]
let questionHandler = new FormHandler(questionUrl, fieldNames);
document.getElementById(questionButton).addEventListener('click', postQuestion);
function postQuestion(event) {
    event.preventDefault();
    let authToken = 'Bearer ' + localStorage.getItem('token');
    fetch(questionHandler.getUrl, {
        method: 'POST',
        headers: {
            'Authorization': authToken,
            'Content-Type': 'application/json'
        },
        body: questionHandler.Data
    }).then(response => response.json())
        .then(data => {
            if (data.status != 201) {
                if (data.error == "The token provided is not valid") {
                    window.alert("Please log in to submit your question");
                    window.location.href = '../user/login.html';
                } else if (data.msg == "Token has been revoked") {
                    window.alert("Please login to submit your question");
                    window.location.href = "../user/login.html";
                } else if (data.error[0].message == 'Token Bearer not given') {
                    window.alert("Please log in in order to post a question");
                    window.location.href = '../user/login.html';
                } else if (data.error[0].message == "Your token has expired") {
                    window.alert("Your session has expired please log in");
                    window.location.href = '../user/login.html';
                } else if (data.status == 406) {
                    window.alert(data.error[0].message);
                } else {
                    window.alert(data.error);
                }
            }
            else {
                window.location.href = "../user/questions.html";
            }
        })
}