document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('cv-form');
    const resultsCard = document.getElementById('results-card');
    const resultsContent = document.getElementById('results-content');
    const loadingIndicator = document.getElementById('loading');

    // Handle form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Show loading indicator
        loadingIndicator.classList.remove('d-none');
        resultsContent.innerHTML = '';
        resultsCard.classList.remove('d-none');

        // Create form data
        const formData = new FormData(form);

        // Send the request to the server
        fetch('/analyze', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || 'İşlem sırasında bir hata oluştu.');
                });
            }
            return response.json();
        })
        .then(data => {
            // Hide loading indicator
            loadingIndicator.classList.add('d-none');

            // Display the results
            const suggestions = data.suggestions;
            resultsContent.innerHTML = `<div class="suggestions">${formatSuggestions(suggestions)}</div>`;
        })
        .catch(error => {
            // Hide loading indicator
            loadingIndicator.classList.add('d-none');

            // Display error message
            resultsContent.innerHTML = `<div class="alert alert-danger">${error.message}</div>`;
        });
    });

    // Format suggestions to HTML
    function formatSuggestions(text) {
        // Replace newlines with <br> tags
        return text.replace(/\n/g, '<br>');
    }

    // Add drag and drop functionality for file input
    const fileInput = document.getElementById('cv_file');
    const dropArea = fileInput.parentElement;

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    function highlight() {
        dropArea.classList.add('highlight');
    }

    function unhighlight() {
        dropArea.classList.remove('highlight');
    }

    dropArea.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        fileInput.files = files;
    }
});