"use strict"
//Class that handles forms on click of buttons
import {
    FormHandler
} from './sharedLibrary.js';
import {
    urls
} from './urls.js';
let questionId = localStorage.getItem('questionId');
let questionUrl = `${urls.postQuestionUrl}/${questionId}`;
let commentUrl = `${urls.commentUrl}/${questionId}`;
window.onload = fetch(questionUrl, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
    .then(data => {
        let result = `<button onclick="location.href='question.html'" class="btn">Ask Question</button>
            <div class="question-view">
                <p class="title">${data.data[0].title}</p>
                <p>${data.data[0].body}</p>
            </div>`
        document.getElementById('result').innerHTML = result;
        fetch(commentUrl, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(commentResponse => commentResponse.json())
            .then(commentsData => {
                if (commentsData.status == 200) {
                    for (let item of commentsData.data) {
                        result += `<div class="question-view comment">
                    <p class="fas fa-user"> ${item.user}</p>
                    <p>${item.comment}</p>
                </div>`
                    }

                }
                result += `<textarea name="" id='comment' cols="30" rows="10"></textarea><br>
                <button class="comment-btn" id='postComment'>Post Your Comment</button>`
                document.getElementById('result').innerHTML = result;
                let newCommentUrl = 'https://questioner-api-v2.herokuapp.com/api/v2/comments/';
                let postButton = 'postComment';
                let fieldNames = [
                    'comment'
                ];
                document.getElementById(postButton).addEventListener('click', postComment);
                let postCommentHandler = new FormHandler(newCommentUrl, fieldNames);

                function postComment(event) {
                    event.preventDefault();
                    let authToken = 'Bearer ' + localStorage.getItem('token');
                    fetch(postCommentHandler.getUrl, {
                            method: 'POST',
                            headers: {
                                'Authorization': authToken,
                                'Content-Type': 'application/json'
                            },
                            body: postCommentHandler.Data
                        }).then(newCommentResponse => newCommentResponse.json())
                        .then(newCommentData => {
                            if (newCommentData.error == "The token provided is not valid") {
                                window.alert("Please log in to submit your comment");
                                window.location.href = '../user/login.html';
                            } else if (newCommentData.msg == "Token has been revoked") {
                                window.alert("Please login to submit your comment");
                                window.location.href = "../user/login.html";
                            } else if (newCommentData.status == 201) {
                                window.location = window.location;
                            } else if (newCommentData.status == 406) {
                                window.alert(newCommentData.error[0].message);
                            } else if (newCommentData.status == 401) {
                                if (newCommentData.error[0].message == 'Your token has expired') {
                                    window.alert("Your session has expired, please log in");
                                    window.location.href = '../user/login.html';
                                } else if (newCommentData.error[0].message == 'Token Bearer not given') {
                                    window.alert("Please sign in in order to post a comment");
                                    window.location.href = '../user/login.html';
                                }
                            }
                        })
                }
            })
    })