document.addEventListener('DOMContentLoaded', function() {
    const translateForm = document.getElementById('translateForm');
    const imageForm = document.getElementById('imageForm');

    translateForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const text = document.getElementById('text').value;
        const targetLanguage = document.getElementById('targetLanguage').value;

        fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text, target_language: targetLanguage })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('translatedText').innerText = data.translated_text;
        });
    });

    imageForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const imageFile = document.getElementById('imageFile').files[0];
        const formData = new FormData();
        formData.append('image', imageFile);

        fetch('/image-to-text', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('extractedText').innerText = data.extracted_text;
        });
    });
});
