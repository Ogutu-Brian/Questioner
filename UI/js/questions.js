"use strict"
let meetupId = localStorage.getItem("meetupId");
let questionsUrl = 'http://127.0.0.1:5000/api/v2/questions/' + meetupId + '/';
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
                    <button class="fa fa-thumbs-down button button-margin"> 0</button>
                </td>
                <td>
                    <button class="fa fa-thumbs-up button button-margin"> 0</button>
                </td>
                <td>
                    <button class="fas fa-comments" id=${'question' + item.id}> ${item.comments}</button></td>
            </tr>`
            }
            document.getElementById('result').innerHTML = result;
            for (let item of data.data) {
                document.getElementById(item.id).addEventListener('click', comments);
                document.getElementById('question' + item.id).addEventListener('click', commentButton);
            }
        }
    })
var comments = (event) => {
    localStorage.setItem('questionId', event.target.id);
    window.location.href = '../user/questionview.html';
}
var commentButton = (event) => {
    console.log(event.target.id.slice(8))
    localStorage.setItem('questionId', event.target.id.slice(8));
    window.location.href = '../user/questionview.html';
}