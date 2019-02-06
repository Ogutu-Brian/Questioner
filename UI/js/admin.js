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
                            <td>10</td>
                        </tr>
                        <tr>
                            <td>MAYBE</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>NO</td>
                            <td>45</td>
                        </tr>
                    </table>
                </div>
                <div class="delete-btn">
                    <button>Delete</button>
                </div>
            </div>`
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
    window.location.href = '../user/questions.html';
}
