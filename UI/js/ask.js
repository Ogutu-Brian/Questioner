"use strict"
//Class that handles forms on click of buttons
import {
    FormHandler
} from './sharedLibrary.js';
import {
    urls
} from './urls.js';
let questionButton = 'postQuestion';
let fieldNames = [
    "title",
    "body"
]
let questionHandler = new FormHandler(urls.postQuestionUrl, fieldNames);
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
            } else {
                window.location.href = "../user/questions.html";
            }
        })
}