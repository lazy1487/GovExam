document.getElementById('confirmationForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission

    var closeButton = document.querySelector('a[data-bs-toggle="modal"][data-bs-target="#CloseModal"]');
    closeButton.textContent = '啟用';
    closeButton.classList.remove('btn-primary');
    closeButton.classList.add('btn-secondary');

    var closeResultModal = new bootstrap.Modal(document.getElementById('CloseResultModal'));
    closeResultModal.hide();
});
