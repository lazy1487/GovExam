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

//==========元件：「確定送出」按鈕觸發必要事件==========//
$(document).ready(function() {
    $('#submitBtn').on('click', function(e) {
        // ==========第一部分：設定所屬類別如果是空白，於元件下方顯示錯誤文字==========//
        e.preventDefault();
        var isValid = true;
        var fields = [
            { id: '#inputTitle', error: '#Title_ErrorText' },
            { id: '#inputURL', error: '#URL_ErrorText' },
            { id: '#relativePathFile', error: '#imageFile_ErrorText' },
            { id: '#phonerelativePathFile', error: '#phoneimageFile_ErrorText' },
            { id: '#upLoadTime', error: '#imageStartDate_ErrorText' },
            { id: '#RemoveTime', error: '#imageEndDate_ErrorText' },
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
        
        // ==========第二部分：判定各區塊起始日期是否有大於結束日期，若有則在起始日期區塊顯示錯誤文字==========//
        // ==========上架日期&文章下架日期==========//
        var errorMessage = '';
        var upLoadTime = $('#upLoadTime').val().trim();
        var RemoveTime = $('#RemoveTime').val().trim();
        if (upLoadTime && RemoveTime) {
            if (upLoadTime > RemoveTime) {
                errorMessage = '輪播圖上架日期不能晚於下架日期';
                $('#upLoadTime').addClass('is-invalid');
                $('#imageStartDate_ErrorText').text(errorMessage).removeClass('d-none');
                isValid = false;
            }
        }

        if (isValid) {
            $('#SaveModal').modal('show');
        }
    });
});

//==========元件：「重新設定」按鈕觸發必要事件==========//
var initInputTitle  = document.getElementById('inputTitle').value;
var initImageDes  = document.getElementById('imageDes').value;
var initSelected  = document.getElementById('selected').value;
var initInputURL  = document.getElementById('inputURL').value;
var initUpLoadTime  = document.getElementById('upLoadTime').value;
var initRemoveTime  = document.getElementById('RemoveTime').value;


document.getElementById('resetButton').addEventListener('click', function() {
    // 獲取輸入框元素
    var inputTitle = document.getElementById('inputTitle');
    var imageDes = document.getElementById('imageDes');
    var selected = document.getElementById('selected');
    var inputURL = document.getElementById('inputURL');
    var upLoadTime = document.getElementById('upLoadTime');
    var RemoveTime = document.getElementById('RemoveTime');
    var relativePathFile = document.getElementById('relativePathFile');
    // 清空輸入框的值
    inputTitle.value = initInputTitle ;
    imageDes.value = initImageDes ;
    selected.value = initSelected ;
    inputURL.value = initInputURL ;
    upLoadTime.value = initUpLoadTime ;
    RemoveTime.value = initRemoveTime ;
    

    var fileStatusButton = document.getElementById('fileStatusButton');
    fileStatusButton.className = 'btn btn-secondary fw-bold';
    fileStatusButton.value = '未選照片';
    relativePathFile.value ='';

    var phonefileStatusButton = document.getElementById('phonefileStatusButton');
    phonefileStatusButton.className = 'btn btn-secondary fw-bold';
    phonefileStatusButton.value = '未選照片';
    phonerelativePathFile.value = '';
    
});

//==========通用函數設定==========
function syncInputValues(inputId, hiddenInputId) {
    const inputElement = document.getElementById(inputId);
    const hiddenInputElement = document.getElementById(hiddenInputId);

    inputElement.addEventListener('input', function() {
        hiddenInputElement.value = inputElement.value;
    });
}

syncInputValues('inputTitle', 'hiddeninputTitle');
syncInputValues('imageDes', 'hiddenimageDes');
syncInputValues('selected', 'hiddenselected');
syncInputValues('inputURL', 'hiddeninputURL');
syncInputValues('imageFile', 'hiddenimageFile');
syncInputValues('phoneimageFile', 'hiddenphoneimageFile');
syncInputValues('upLoadTime', 'hiddenupLoadTime');
syncInputValues('RemoveTime', 'hiddenRemoveTime');