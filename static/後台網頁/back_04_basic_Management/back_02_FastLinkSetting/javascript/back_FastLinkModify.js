tinyMCE.init({
    // 初始化參數設定[註1]
    selector: "#linkMaintainContext", // 目標物件
    auto_focus: "linkMaintainContext", // 聚焦物件
    language: "zh_TW", // 語系(CDN沒有中文，需要下載原始source才有)
    theme: "modern", // 模板風格
    plugins : "advlist autolink link image lists charmap print preview", // 套件設定: 進階清單、自動連結、連結、上傳圖片、清單、特殊字元表、列印、預覽
    mobile: { // 行動裝置設定
        theme: "mobile", // 模板風格
        plugins: [ "autosave", "lists", "autolink" ],  // 套件設定: 自動儲存、清單、自動連結
        toolbar: [ "undo", "bold", "italic", "styleselect","wordcount" ]  // 工具列設定: 復原、粗體、斜體、樣式表
    } 
});

function displayFileName(fileInputId, relativePathFileId, statusButtonId, imageId, modalId) {
    var fileInput = document.getElementById(fileInputId);
    var relativePathFile = document.getElementById(relativePathFileId);
    var statusButton = document.getElementById(statusButtonId);

    if (fileInput.files.length > 0) {
        relativePathFile.value = fileInput.files[0].name;
        statusButton.value = "檢視照片";
        statusButton.classList.remove("btn-secondary");
        statusButton.classList.add("btn-info");

        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById(imageId).src = e.target.result;
        };
        reader.readAsDataURL(fileInput.files[0]);
    } else {
        relativePathFile.value = "";
        statusButton.value = "未選照片";
        statusButton.classList.remove("btn-info");
        statusButton.classList.add("btn-secondary");

        // Clear image source
        document.getElementById(imageId).src = "";
    }
}

function openModal(statusButtonId, modalId) {
    var statusButton = document.getElementById(statusButtonId);
    if (statusButton.value === "檢視照片") {
        $('#' + modalId).modal('show');
    }
}

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

//==========元件：「確定送出」按鈕觸發必要事件==========//
$(document).ready(function() {
    $('#submitBtn').on('click', function(e) {
        // ==========第一部分：設定所屬類別如果是空白，於元件下方顯示錯誤文字==========//
        e.preventDefault();
        var isValid = true;
        var fields = [
            { id: '#inputTitle', error: '#Title_ErrorText' },
            { id: '#inputURL', error: '#URL_ErrorText' },
            { id: '#LinkPathFile', error: '#LinkimageFile_ErrorText' }
        ];

        fields.forEach(function(field) {
            var input = $(field.id).val().trim();
            if (input === '') {
                $(field.id).addClass('is-invalid');
                $(field.error).removeClass('d-none');
                isValid = false;
            } else {
                $(field.id).removeClass('is-invalid');
                $(field.error).addClass('d-none');
            }
        });
        if (isValid) {
            $('#SaveModal').modal('show');
        }
    });
});
