//=====考試類別內文，同時也安裝tinyMCE工具包=====
tinymce.init({
    selector: "textarea",                                                 // 目標物件
    auto_focus: "inputExamStyleDes",                                      // 聚焦物件
    language: "zh_TW",                                                    // 語系(CDN沒有中文，需要下載原始source才有)
    theme: "modern",                                                      // 模板風格
    plugins: "advlist autolink link image lists charmap print preview",   // 套件設定
    mobile: {                                                             // 行動裝置設定
        theme: "mobile",                                                  // 模板風格
        plugins: [ "autosave", "lists", "autolink" ],                     // 套件設定
        toolbar: [ "undo", "bold", "italic", "styleselect","wordcount" ]  // 工具列設定
    },
    setup: function(editor) {
        editor.on('change keyup', function() {
            // 當編輯器內容變化時，將其值設置為 hidden 輸入框的值
            document.getElementById('hiddeninputExamStyleDes').value = editor.getContent();
        });
    }
});

//=====考試類別代號=====
const inputExamStyleID = document.getElementById('inputExamStyleID');
const hiddeninputExamStyleID = document.getElementById('hiddeninputExamStyleID');

inputExamStyleID.addEventListener('input', function() {
    hiddeninputExamStyleID.value = inputExamStyleID.value;
});
//=====考試類別名稱=====
const inputExamStyle = document.getElementById('inputExamStyle');
const hiddeninputExamStyle = document.getElementById('hiddeninputExamStyle');

inputExamStyle.addEventListener('input', function() {
    hiddeninputExamStyle.value = inputExamStyle.value;
});

//=====考試類別是否啟用=====
document.getElementById('toggleButton').addEventListener('click', function() {
    var hiddenInput = document.getElementById('hiddeninputExamStyleIsUsed');
    var button = document.getElementById('toggleButton');

    if (hiddenInput.value === 'N') {
        hiddenInput.value = 'Y';
        button.textContent = '禁用';
        button.classList.remove('btn-warning');
        button.classList.add('btn-primary');
    } else {
        hiddenInput.value = 'N';
        button.textContent = '啟用';
        button.classList.remove('btn-primary');
        button.classList.add('btn-secndary');
    }
});

//=====考試類別啟用時間=====
const inputExamStyleStartTime = document.getElementById('inputExamStyleStartTime');
const hiddeninputExamStyleStartTime = document.getElementById('hiddeninputExamStyleStartTime');

inputExamStyleStartTime.addEventListener('input', function() {
    hiddeninputExamStyleStartTime.value = inputExamStyleStartTime.value;
});

//=====考試類別結束時間=====
const inputExamStyleEndTime = document.getElementById('inputExamStyleEndTime');
const hiddeninputExamStyleEndTime = document.getElementById('hiddeninputExamStyleEndTime');

inputExamStyleEndTime.addEventListener('input', function() {
    hiddeninputExamStyleEndTime.value = inputExamStyleEndTime.value;
});

//=====重新設定按鈕點擊後清除value值=====
document.getElementById('resetButton').addEventListener('click', function() {
    // 獲取 inputExamStyleID 輸入框元素
    var inputExamStyleID = document.getElementById('inputExamStyleID');
    var inputExamStyle = document.getElementById('inputExamStyle');
    var inputExamStyleDes = tinymce.get('inputExamStyleDes');
    var inputExamStyleIsUsed = document.getElementById('inputExamStyleIsUsed');
    var inputExamStyleStartTime = document.getElementById('inputExamStyleStartTime');
    var inputExamStyleEndTime = document.getElementById('inputExamStyleEndTime');
    // 清空輸入框的值
    inputExamStyleID.value = '';
    inputExamStyle.value = '';
    if (inputExamStyleDes) {
        inputExamStyleDes.setContent('請輸入考試類別內文');}
    inputExamStyleIsUsed = '';
    inputExamStyleStartTime.value = '';
    inputExamStyleEndTime.value = '';
});

// =====必須要補齊以下script語法=====
// =====<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>=====
$(document).ready(function() {
    $('#submitBtn').on('click', function(e) {
        e.preventDefault();
        
        var fields = [
            { id: '#inputExamStyleID', error: '#errorTextID' },
            { id: '#inputExamStyle', error: '#errorText' },
            { id: '#inputExamStyleStartTime', error: '#errorTextStatrTime' },
            { id: '#inputExamStyleEndTime', error: '#errorTextEndTime' }
        ];

        var isValid = true;

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