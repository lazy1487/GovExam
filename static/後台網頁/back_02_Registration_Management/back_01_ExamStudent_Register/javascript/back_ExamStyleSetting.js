// ============================================================================================================================================
tinyMCE.init({
  selector: "textarea", // 目標物件
  auto_focus: "inputExamStyleDes", // 聚焦物件
  language: "zh_TW", // 語系
  theme: "modern", // 佈景主題風格
  plugins: "", // 移除所有套件
  toolbar: false, // 隱藏工具列
  menubar: false, // 隱藏選單列
  statusbar: false, // 隱藏狀態列
  branding: false, // 隱藏品牌資訊
  mobile: { // 行動裝置設定
    theme: "mobile", // 佈景主題風格
    plugins: "", // 移除所有行動裝置的套件
    toolbar: false // 隱藏行動裝置的工具列
  } 
});

const inputExamStyle = document.getElementById('inputExamStyle');
const hiddeninputExamStyle = document.getElementById('hiddeninputExamStyle');

inputExamStyle.addEventListener('input', function() {
  hiddeninputExamStyle.value = inputExamStyle.value;
});