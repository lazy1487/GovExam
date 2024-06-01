
tinyMCE.init({
    // 初始化參數設定[註1]
    selector: "textarea", // 目標物件
    auto_focus: "inputDes", // 聚焦物件
    language: "zh_TW", // 語系(CDN沒有中文，需要下載原始source才有)
    theme: "modern", // 模板風格
    plugins : "advlist autolink link image lists charmap print preview", // 套件設定: 進階清單、自動連結、連結、上傳圖片、清單、特殊字元表、列印、預覽
    mobile: { // 行動裝置設定
        theme: "mobile", // 模板風格
        plugins: [ "autosave", "lists", "autolink" ],  // 套件設定: 自動儲存、清單、自動連結
        toolbar: [ "undo", "bold", "italic", "styleselect","wordcount" ]  // 工具列設定: 復原、粗體、斜體、樣式表
    } 
});

document.addEventListener("DOMContentLoaded", function() {
    var modal = new bootstrap.Modal(document.getElementById('exampleModal'));

    // 當按下表單的提交按鈕時，檢查表單的所有必填欄位是否都已填寫
    document.getElementById('submitButton').addEventListener('click', function(event) {
        var inputSubTitleValue = document.getElementById('inputSubTitle').value;
        var inputDesValue = document.getElementById('inputDes').value;
        var inputContextValue = document.getElementById('inputContext').value;
        var inputTitleValue = document.getElementById('inputTitle').value;
        var uploadTimeValue = document.getElementsByName('UploadTime')[0].value;
        var removeTimeValue = document.getElementsByName('RemoveTime')[0].value;

        if (!inputSubTitleValue || !inputDesValue || !inputContextValue || !inputTitleValue || !uploadTimeValue || !removeTimeValue) {
            event.preventDefault(); // 防止表單提交
            modal.show(); // 如果任何一個必填欄位為空，顯示模態對話框
        }
    });
});

document.addEventListener('DOMContentLoaded', (event) => {
    const resetButton = document.getElementById('resetButton');

    // 保存初始值
    const initialValues = {
        inputSubTitle: document.getElementById('inputSubTitle').value,
        inputDes: document.getElementById('inputDes').value,
        inputContext: document.getElementById('inputContext').value,
        inputTitle: document.getElementById('inputTitle').value,
        upLoadTime: document.getElementById('upLoadTime').value,
        RemoveTime: document.getElementById('RemoveTime').value
    };

    // 添加点击事件监听器
    resetButton.addEventListener('click', () => {
        document.getElementById('inputSubTitle').value = initialValues.inputSubTitle;
        document.getElementById('inputDes').value = initialValues.inputDes;
        document.getElementById('inputContext').value = initialValues.inputContext;
        document.getElementById('inputTitle').value = initialValues.inputTitle;
        document.getElementById('upLoadTime').value = initialValues.upLoadTime;
        document.getElementById('RemoveTime').value = initialValues.RemoveTime;
    });
});