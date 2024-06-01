document.addEventListener("DOMContentLoaded", function() {
    // 選取第一個 input 元素
    var firstInputinputTitle = document.querySelector('.form-control.inputTitle');
    var firstInputimageDes = document.querySelector('.form-control.imageDes');
    var firstInputselected = document.querySelector('.form-control.selected');
    var firstInputinputURL = document.querySelector('.form-control.inputURL');
    var firstInputimageFile = document.querySelector('.form-control.imageFile');
    
    // 選取第二個 input 元素
    var secondInputinputTitle = document.querySelector('input[name="inputTitle"]:not(.form-control.inputTitle)');
    var secondInputimageDes = document.querySelector('input[name="imageDes"]:not(.form-control.imageDes)');
    var secondInputselected = document.querySelector('input[name="selected"]:not(.form-control.selected)');
    var secondInputinputURL = document.querySelector('input[name="inputURL"]:not(.form-control.inputURL)');
    var secondInputimageFile = document.querySelector('input[name="imageFile"]:not(.form-control.imageFile)');
    
    // 確保選取的元素存在
    if (firstInputinputTitle && secondInputinputTitle) {
        firstInputinputTitle.addEventListener('input', function() {
            secondInputinputTitle.value = firstInputinputTitle.value;
        });
        secondInputinputTitle.value = firstInputinputTitle.value;
    }

    if (firstInputimageDes && secondInputimageDes) {
        firstInputimageDes.addEventListener('input', function() {
            secondInputimageDes.value = firstInputimageDes.value;
        });
        secondInputimageDes.value = firstInputimageDes.value;
    }

    if (firstInputselected && secondInputselected) {
        firstInputselected.addEventListener('input', function() {
            secondInputselected.value = firstInputselected.value;
        });
        secondInputselected.value = firstInputselected.value;
    }

    if (firstInputinputURL && secondInputinputURL) {
        firstInputinputURL.addEventListener('input', function() {
            secondInputinputURL.value = firstInputinputURL.value;
        });
        secondInputinputURL.value = firstInputinputURL.value;
    }

    if (firstInputimageFile && secondInputimageFile) {
        firstInputimageFile.addEventListener('input', function() {
            secondInputimageFile.value = firstInputimageFile.value;
        });
        secondInputimageFile.value = firstInputimageFile.value;
    }
});