document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault();

    let fileInput = document.getElementById('fileInput');
    let formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <p>Recommended Grinder Setting: <strong>${data.grinder_setting}</strong></p>
            <img src="/static/images/${fileInput.files[0].name}" alt="Uploaded Image" style="max-width: 300px;"/>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
