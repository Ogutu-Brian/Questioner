let meetupId = localStorage.getItem("meetupId");
questionsUrl = 'http://127.0.0.1:5000/api/v2/questions/' + meetupId + '/';
window.onload = fetch(questionsUrl, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
}).then(response => response.json())
    .then(data => {
        if (data.status != 200) {
        } else {
            let result = '';
            for (let item of data.data) {
                result += `<tr>
                <td colspan="3">
                <a href="questionview.html">
                    ${item.title}
                </a>
                </td>
            </tr>
            <tr>
                <td class="cell">
                    <button class="fa fa-thumbs-down button button-margin"> 4</button>
                </td>
                <td>
                    <button class="fa fa-thumbs-up button button-margin"> 1</button>
                </td>
                <td>
                    <button class="fas fa-comments" onclick="location.href='questionview.html'"> 1</button></td>
            </tr>`
            }
            document.getElementById('result').innerHTML = result;
        }
    })