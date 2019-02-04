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
let endpointUrl = 'https://questioner-api-v2.herokuapp.com/api/v2/meetups';
let meetupButton = 'postMeeup';
document.getElementById(meetupButton).addEventListener('click', createMeetup);
let fieldNames = [
    'location',
    'topic',
    'happeningOn',
    'body'
]
let meetupHandler = new FormHandler(endpointUrl, fieldNames)
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
                if (data.error[0].message == "Token Bearer not given") {
                    window.alert("Please log in in order to create a meetup");
                } else if (data.error[0].message == "Your token has expired") {
                    window.location.href = "../user/login.html";
                } else {
                    window.alert(data.error[0].message);
                }
            } else {
                window.location.href = "../user/meetups.html";
            }
        })
}