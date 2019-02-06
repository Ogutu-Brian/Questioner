"use strict"
let meetupId = localStorage.getItem("meetupId");
let questionsUrl = `http://127.0.0.1:5000/api/v2/questions/${meetupId}/`;
let authToken = 'Bearer ' + localStorage.getItem('token');
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
window.onload = fetch(questionsUrl, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
}).then(response => response.json())
    .then(data => {
        if (data.status == 200) {
            let result = '';
            for (let item of data.data) {
                result += `<tr>
                <td colspan="3">
                <a id=${item.id}>
                    ${item.title}
                </a>
                </td>
            </tr>
            <tr>
                <td class="cell">
                    <button class="fa fa-thumbs-down button button-margin" id=${'downvote' + item.id}> ${item.downvotes}</button>
                </td>
                <td>
                    <button class="fa fa-thumbs-up button button-margin" id=${'upvote' + item.id}> ${item.upvotes}</button>
                </td>
                <td>
                    <button class="fas fa-comments" id=${'question' + item.id}> ${item.comments}</button></td>
            </tr>`
            }
            document.getElementById('result').innerHTML = result;
            for (let item of data.data) {
                document.getElementById(item.id).addEventListener('click', comments);
                document.getElementById('question' + item.id).addEventListener('click', commentButton);
                document.getElementById('upvote' + item.id).addEventListener('click', upvoteQuestion);
                document.getElementById('downvote' + item.id).addEventListener('click', downvoteQuestion);
            }
        }
    })
var comments = (event) => {
    localStorage.setItem('questionId', event.target.id);
    window.location.href = '../user/questionview.html';
}
var commentButton = (event) => {
    localStorage.setItem('questionId', event.target.id.slice(8));
    window.location.href = '../user/questionview.html';
}
var upvoteQuestion = (event) => {
    let questionId = event.target.id.slice(6);
    let votingUrl = `http://127.0.0.1:5000/api/v2/questions/${questionId}/upvote`;
    fetch(votingUrl, {
        method: 'PATCH',
        mode: "cors",
        headers: {
            'Authorization': authToken,
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.status == 201) {
                window.location = window.location;
            }
            else {
                if (data.error[0].message == "Your token has expired") {
                    window.alert("Your session has expired, please log in");
                    window.location.href = "../user/login.html";
                } else if (data.error[0].message == "Token Bearer not given") {
                    window.alert("Please log in in order to vote");
                    window.location.href = "../user/login.html";
                } else {
                    window.alert(data.error);
                }
            }
        })
}
var downvoteQuestion = (event) => {
    let questionId = event.target.id.slice(8);
    let votingUrl = `http://127.0.0.1:5000/api/v2/questions/${questionId}/downvote`;
    fetch(votingUrl, {
        method: 'PATCH',
        mode: "cors",
        headers: {
            'Authorization': authToken,
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => {
            if (data.status == 201) {
                window.location = window.location;
            }
            else {
                if (data.error[0].message == "Your token has expired") {
                    window.alert("Your session has expired, please log in");
                    window.location.href = "../user/login.html";
                } else if (data.error[0].message == "Token Bearer not given") {
                    window.alert("Please log in in order to vote");
                    window.location.href = "../user/login.html";
                } else {
                    window.alert(data.error);
                }
            }
        })
}
