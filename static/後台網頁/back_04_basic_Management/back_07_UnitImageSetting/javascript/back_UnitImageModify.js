function showFileName() {
    var input = document.getElementById('imageFile');
    var fileName = input.files[0].name;
    document.getElementById('fileName').textContent = 'Selected file: ' + fileName;
}