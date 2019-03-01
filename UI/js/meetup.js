"use strict"
import {
    urls
} from './urls.js';
import {
    FormHandler
} from './sharedLibrary.js';
let meetupButton = 'postMeeup';
document.getElementById(meetupButton).addEventListener('click', createMeetup);
let fieldNames = [
    'location',
    'topic',
    'happeningOn',
    'body'
]
let meetupHandler = new FormHandler(urls.postMeetupUrl, fieldNames)

function createMeetup(event) {
    //Function that handles creation of meetup event
    event.preventDefault()
    let authToken = 'Bearer ' + localStorage.getItem('token');
    fetch(meetupHandler.getUrl, {
            method: 'POST',
            headers: {
                'Authorization': authToken,
                'Content-Type': 'application/json'
            },
            body: meetupHandler.Data
        }).then(response => response.json())
        .then(data => {
            if (data.status != 201) {
                if (data.error == "The token provided is not valid") {
                    window.alert("Please log in to create a meetup");
                    window.location.href = '../user/login.html';
                } else if (data.msg == "Token has been revoked") {
                    window.alert("Please login to create a meetup");
                    window.location.href = "../user/login.html";
                } else if (data.error[0].message == 'Token Bearer not given') {
                    window.alert("Please log in to create a meetup");
                    window.location.href = '../user/login.html';
                } else if (data.error[0].message == "Your token has expired") {
                    window.alert("Your session has expired please log in");
                    window.location.href = '../user/login.html';
                } else {
                    window.alert(data.error[0].message);
                }
            } else {
                window.location.href = "../admin/admin.html";
            }
        })
}