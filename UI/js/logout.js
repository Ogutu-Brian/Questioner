"use strict"
let authToken = 'Bearer ' + localStorage.getItem('token');
let logOutUrl = 'http://127.0.0.1:5000/api/v2/auth/logout';
document.getElementById('logout-btn').addEventListener('click', logout);
var logout = (event) => {
    event.preventDefault();
    fetch(logOutUrl, {
        method: 'DELETE',
        headers: {
            'Authorization': authToken,
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => {
            if (data.status == 200) {
                window.location.href = '../user/logoin.html';
            }
        })
}