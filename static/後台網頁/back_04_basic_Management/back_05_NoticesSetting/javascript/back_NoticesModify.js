tinyMCE.init({
    // 初始化參數設定[註1]
    selector: "textarea", // 目標物件
    auto_focus: "normalQuestionDesContext", // 聚焦物件
    language: "zh_TW", // 語系(CDN沒有中文，需要下載原始source才有)
    theme: "modern", // 模板風格
    plugins : "advlist autolink link image lists charmap print preview", // 套件設定: 進階清單、自動連結、連結、上傳圖片、清單、特殊字元表、列印、預覽
    mobile: { // 行動裝置設定
        theme: "mobile", // 模板風格
        plugins: [ "autosave", "lists", "autolink" ],  // 套件設定: 自動儲存、清單、自動連結
        toolbar: [ "undo", "bold", "italic", "styleselect","wordcount" ]  // 工具列設定: 復原、粗體、斜體、樣式表
    } 
});