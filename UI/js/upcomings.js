"use strict"
let meetupUrl = 'https://questioner-api-v2.herokuapp.com/api/v2/meetups/upcoming/';
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
                result +=
                    `<div class="card" id=${item.id}>
                    <div class="card-info" id=${item.id}>
                        <p id=${item.id}>${item.topic}</p>
                        <p class="location" id=${item.id}>${item.location}</p>
                        <p class="date" id=${item.id}>${item.happeningOn}</p>
                        <p class="info" id=${item.id}>${item.body}</p>
                    </div>
                </div>`;
            }
            document.getElementById('result').innerHTML = result;
            for (let item of data.data) {
                document.getElementById(item.id).addEventListener('click', questions);
            }
        }
    })
var questions = (event) => {
    //function that gets meetup id and sets it to local storage
    localStorage.setItem("meetupId", event.target.id);
    window.location.href = 'questions.html';
}
