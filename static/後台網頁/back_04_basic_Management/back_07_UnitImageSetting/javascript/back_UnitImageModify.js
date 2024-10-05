tinyMCE.init({
    // 初始化參數設定[註1]
    selector: "#webmaintain_Context", // 目標物件
    auto_focus: "webmaintain_Context", // 聚焦物件
    language: "zh_TW", // 語系(CDN沒有中文，需要下載原始source才有)
    theme: "modern", // 模板風格
    plugins : "advlist autolink link image lists charmap print preview", // 套件設定: 進階清單、自動連結、連結、上傳圖片、清單、特殊字元表、列印、預覽
    mobile: { // 行動裝置設定
        theme: "mobile", // 模板風格
        plugins: [ "autosave", "lists", "autolink" ],  // 套件設定: 自動儲存、清單、自動連結
        toolbar: [ "undo", "bold", "italic", "styleselect","wordcount" ]  // 工具列設定: 復原、粗體、斜體、樣式表
    } 
});

var imageDesTextarea = document.getElementById('imageDes');
var hiddenimageDesInput = document.getElementById('hiddenimageDes');

// 当 textarea 的值发生变化时，更新隐藏输入框的值
imageDesTextarea.addEventListener('input', function() {
    hiddenimageDesInput.value = imageDesTextarea.value;
});

// 初始化时将 textarea 的值赋给隐藏输入框
hiddenimageDesInput.value = imageDesTextarea.value;

function displayFileName() {
    var selectedFile = document.getElementById('fileInput').files[0];
    var fileName = selectedFile ? selectedFile.name : '';
    document.getElementById('inputFile').value = fileName;

    // 清空 hiddeninputfile
    document.getElementById('hiddeninputfile').value = '';

    // 在 hiddeninputfile 中填入檔案名稱
    document.getElementById('hiddeninputfile').value = fileName;
}


function updateHiddenInputFile() {
    var filePath = document.getElementById('inputFile').value;
    document.getElementById('hiddeninputfile').value = filePath;
}

//=====畫面載入時先抓取value值=====
var initInputFile  = document.getElementById('inputFile').value;
var initImageDes  = document.getElementById('imageDes').value;

//=====重新設定按鈕點擊後清除value值=====
document.getElementById('resetButton').addEventListener('click', function() {
    // 獲取 inputFile 輸入框元素
    var inputFile = document.getElementById('inputFile');
    var imageDes = document.getElementById('imageDes');

    // 還原輸入框的值
    inputFile.value = initInputFile;
    imageDes.value = initImageDes;

});

$(document).ready(function() {
    $('#submitBtn').on('click', function(e) {
        e.preventDefault();
        
        var fields = [
            { id: '#inputFile', error: '#errorText' },
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