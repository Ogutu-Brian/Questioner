let meetupUrl = 'http://127.0.0.1:5000/api/v2/meetups/upcoming/';
window.onload = fetch(meetupUrl, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
}).then(response => response.json())
    .then(data => {
        let result = ''
        for (let item of data.data) {
            result +=
                `<div class="card" id=id=${item.id}>
                    <div class="card-info">
                        <p>${item.topic}</p>
                        <p class="location">${item.location}</p>
                        <p class="date">${item.happeningOn}</p>
                        <p class="info">${item.body}</p>
                    </div>
                </div>`;
        }
        document.getElementById('result').innerHTML = result;
    })