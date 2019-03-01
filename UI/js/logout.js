"use strict"
//logs out a user
import {
    urls
} from './urls.js';
let authToken = 'Bearer ' + localStorage.getItem('token');
var logout = () => {
    //Function to log out and clear local storage
    fetch(urls.logoutUrl, {
            method: 'DELETE',
            headers: {
                'Authorization': authToken,
                'Content-Type': 'application/json'
            }
        }).then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.status == 200) {
                window.alert("Successfully Logged out");
                window.location.href = '../index.html';
            } else if (data.msg == "Token has been revoked") {
                window.alert("You are not logged in");
                window.location.href = "../index.html";
            } else if (data.error[0].message == "Token Bearer not given") {
                window.alert("You are not logged in");
                window.location.href = '../user/login.html';
            } else if (data.error[0].message == "Your token has expired") {
                window.alert("Your session has expired,please log in");
                window.location.href = '../user/login.html';
            } else if (data.error == "The token provided is not valid") {
                window.alert("You are not logged in");
                window.location.href = '../index.html';
            }
            localStorage.clear();
        })
}