"use strict"
let meetupUrl = 'http://127.0.0.1:5000/api/v2/meetups/upcoming/';
window.onload = fetch(meetupUrl, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
}).then(response => response.json())
    .then(data => {
        if (data.status == 200) {
            let result = ''
            for (let item of data.data) {
                result += `<div class="meetup-card"=id=${item.id}>
                <div class="meetup-info" id=${item.id}>
                    <p id=${item.id}>${item.topic}</p>
                    <p class="location" id=${item.id}>${item.location}</p>
                    <p class="date" id=${item.id}>${item.happeningOn}</p>
                    <p class="info" id=${item.id}>${item.body}</p>
                </div>
                <div class="rsvp-info">
                    <table>
                        <tr>
                            <td>YES</td>
                            <td>${item.yes}</td>
                        </tr>
                        <tr>
                            <td>MAYBE</td>
                            <td>${item.maybe}</td>
                        </tr>
                        <tr>
                            <td>NO</td>
                            <td>${item.no}</td>
                        </tr>
                    </table>
                </div>
                <div class="delete-btn">
                    <button id=${'button' + item.id}>Delete</button>
                </div>
            </div>`
            }
            document.getElementById('result').innerHTML = result;
            for (let item of data.data) {
                document.getElementById(item.id).addEventListener('click', questions);
                document.getElementById('button' + item.id).addEventListener('click', deleteMeetup);
            }
        }
    })
var questions = (event) => {
    //function that gets meetup id and sets it to local storage
    localStorage.setItem("meetupId", event.target.id);
    window.location.href = '../user/questions.html';
}
var deleteMeetup = (event) => {
    let meetupId = event.target.id.slice(6);
    let deleteUrl = `http://127.0.0.1:5000/api/v2/meetups/${meetupId}`;
    let authToken = 'Bearer ' + localStorage.getItem('token');
    fetch(deleteUrl, {
        method: 'DELETE',
        headers: {
            'Authorization': authToken,
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => {
            if (data.status == 200) {
                window.location = window.location;
            }
            else if (data.error[0].message == "Your token has expired") {
                window.alert("Your session has expired please log in");
                window.location.href = '../user/login.html';
            }
            else {
                window.alert(data.error[0].message);
            }
        })
}