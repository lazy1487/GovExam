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

//  畫面載入時先抓取value值
var initInputExamStyleID  = document.getElementById('inputExamStyleID').value;
var initInputExamStyle  = document.getElementById('inputExamStyle').value;


document.getElementById('resetButton').addEventListener('click', function() {
    // 獲取 inputExamStyleID 輸入框元素
    var inputExamStyleID = document.getElementById('inputExamStyleID');
    var inputExamStyle = document.getElementById('inputExamStyle');
    var inputExamStyleDes = tinymce.get('inputExamStyleDes');
    var inputExamStyleIsUsed = document.getElementById('inputExamStyleIsUsed');
    var inputExamStyleStartTime = document.getElementById('inputExamStyleStartTime');
    var inputExamStyleEndTime = document.getElementById('inputExamStyleEndTime');
    
    // 清空輸入框的值
    inputExamStyleID.value = initInputExamStyleID ;
    inputExamStyle.value = initInputExamStyle;
    if (inputExamStyleDes) {
        inputExamStyleDes.setContent('');}
    inputExamStyleStartTime.value = '' ;
    inputExamStyleEndTime.value = '';
});


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