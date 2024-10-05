function openNewWindow() {
    // 新視窗的網址
    var url = "/backAccountFunctionView";
    
    // 設定新視窗的寬度和高度
    var width = 1500;
    var height = 800;
    
    // 計算螢幕的寬度和高度
    var screenWidth = window.screen.width;
    var screenHeight = window.screen.height;
    
    // 計算新視窗的左上角位置，使其位於螢幕正中間
    var left = (screenWidth - width) / 2;
    var top = (screenHeight - height) / 2;
    
    // 開啟新視窗，設定寬度、高度、位置，以及不顯示導覽按鈕
    var newWindow = window.open(url, "_blank", `width=${width},height=${height},top=${top},left=${left},toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no,copyhistory=no`);
    
}

//=====畫面上的表單value值填入隱藏表單，用隱藏表單提交資料=====
var inputAccount = document.getElementById('inputAccount');
var hiddenUserAccount = document.getElementById('hiddenUserAccount');
inputAccount.addEventListener('input', function() {hiddenUserAccount.value = inputAccount.value;});

var inputUserName = document.getElementById('inputUserName');
var hiddenUserName = document.getElementById('hiddenUserName');
inputUserName.addEventListener('input', function() {hiddenUserName.value = inputUserName.value;});

var inputPassWord = document.getElementById('inputPassWord');
var hiddenPassWord = document.getElementById('hiddenPassWord');
inputPassWord.addEventListener('input', function() {hiddenPassWord.value = inputPassWord.value;});

var inputSecondPassWord = document.getElementById('inputSecondPassWord');
var hiddenSecondPassword = document.getElementById('hiddenSecondPassword');
inputSecondPassWord.addEventListener('input', function() {hiddenSecondPassword.value = inputSecondPassWord.value;});

var inputPhone = document.getElementById('inputPhone');
var hiddenPhone = document.getElementById('hiddenPhone');
inputPhone.addEventListener('input', function() {hiddenPhone.value = inputPhone.value;});

var inputEmail = document.getElementById('inputEmail');
var hiddenEmail = document.getElementById('hiddenEmail');
inputEmail.addEventListener('input', function() {hiddenEmail.value = inputEmail.value;});

$(document).ready(function(){
    // 初始化隱藏輸入框的值
    $('#hiddenStatusSelect').val($('#statusSelect').val());

    // 當下拉選單的值改變時
    $('#statusSelect').change(function(){
        // 更新隱藏輸入框的值
        $('#hiddenStatusSelect').val($(this).val());
    });
});

//========================================jQuery的slideToggle(所有模組設定)========================================
$(document).ready(function(){
    $("#flip").click(function(){
        console.log("Flip clicked"); // 確認點擊事件是否觸發
        $("#panel").slideToggle("slow", function() {
            console.log("Panel toggled"); // 確認 slideToggle 是否完成
        });
    });
});


//=====從 Local Storage 提取值並設置到相應的輸入框中(搭配back_accountFunctionView.js)：
window.onload = function() {
    const hiddenaccountadd = localStorage.getItem('hiddenaccountadd');
    const hiddenaccountmodify = localStorage.getItem('hiddenaccountmodify');
    const hiddenpasswordReset = localStorage.getItem('hiddenpasswordReset');

    document.getElementById('hiddenaccountadd').value = hiddenaccountadd;
    document.getElementById('hiddenaccountmodify').value = hiddenaccountmodify;
    document.getElementById('hiddenpasswordReset').value = hiddenpasswordReset;

    // 清除存儲的值（如果不需要再次使用）
    localStorage.removeItem('hiddenaccountadd');
    localStorage.removeItem('hiddenaccountmodify');
    localStorage.removeItem('hiddenpasswordReset');
};

document.getElementById('allOpen').addEventListener('click', function() {
    document.getElementById('hiddenaccountadd').value = 'Y';                                              //=====帳號權限設定-新增=====
    document.getElementById('hiddenaccountmodify').value = 'Y';                                           //=====帳號權限設定-修改=====
    document.getElementById('hiddenpasswordReset').value = 'Y';                                           //=====帳號權限設定-重設密碼===== 
    const buttons = [
        //====================報名管理模組====================
        { buttonId: 'Button_exam_Registration', hiddenInputId: 'hiddenExamRegistration' },                //=====一般考生報名=====
        { buttonId: 'Button_agnecy_Registration', hiddenInputId: 'hiddenAgencyRegistration' },            //=====機關薦送報名=====
        //====================系統管理模組====================
        { buttonId: 'Button_system_EnvironmentSetting', hiddenInputId: 'hiddenenvironmentsetting' },      //=====系統環境設定=====
        { buttonId: 'Button_system_SMTPSetting', hiddenInputId: 'hiddensmtpsetting' },                    //=====SMTP設定=====
        { buttonId: 'Button_system_SystemSearch', hiddenInputId: 'hiddensystemsearch' },                  //=====系統登入查詢=====
        //====================基本管理模組====================
        { buttonId: 'Button_basic_CarouselSetting', hiddenInputId: 'hiddencarouselsetting' },             //=====輪播圖維護=====
        { buttonId: 'Button_basic_FastLinkSetting', hiddenInputId: 'hiddenfastlinksetting' },             //=====快速連結設定=====
        { buttonId: 'Button_basic_NewsSetting', hiddenInputId: 'hiddennewsetting' },                      //=====最新消息維護===== 
        { buttonId: 'Button_basic_NormalQuestionSetting', hiddenInputId: 'hiddennormalquestionsetting' }, //=====常見問題資訊維護=====
        { buttonId: 'Button_basic_NoticesSetting', hiddenInputId: 'hiddennoticesetting' },                //=====注意事項維護=====
        { buttonId: 'Button_basic_PaymentSetting', hiddenInputId: 'hiddenpaymentsetting' },               //=====付款提示維護=====
        { buttonId: 'Button_basic_UnitImageSetting', hiddenInputId: 'hiddenunitimagesetting' },           //=====單元形象維護=====
    ];

    buttons.forEach(button => {
        const buttonElement = document.getElementById(button.buttonId);
        const hiddenInputElement = document.getElementById(button.hiddenInputId);
        buttonElement.className = 'btn btn-primary';
        buttonElement.innerText = '關閉';
        hiddenInputElement.value = 'Y';
    });
});


document.getElementById('allClose').addEventListener('click', function() {
    document.getElementById('hiddenaccountadd').value = 'N';           //=====帳號權限設定-新增=====                                   //=====帳號權限設定-新增=====
    document.getElementById('hiddenaccountmodify').value = 'N';        //=====帳號權限設定-修改=====                                  //=====帳號權限設定-修改=====
    document.getElementById('hiddenpasswordReset').value = 'N';        //=====帳號權限設定-重設密碼=====

    const buttons = [
        //====================報名管理模組====================
        { buttonId: 'Button_exam_Registration', hiddenInputId: 'hiddenExamRegistration' },                //=====一般考生報名=====
        { buttonId: 'Button_agnecy_Registration', hiddenInputId: 'hiddenAgencyRegistration' },            //=====機關薦送報名=====
        //====================系統管理模組====================
        { buttonId: 'Button_system_EnvironmentSetting', hiddenInputId: 'hiddenenvironmentsetting' },      //=====系統環境設定=====
        { buttonId: 'Button_system_SMTPSetting', hiddenInputId: 'hiddensmtpsetting' },                    //=====SMTP設定=====
        { buttonId: 'Button_system_SystemSearch', hiddenInputId: 'hiddensystemsearch' },                  //=====系統登入查詢=====
        //====================基本管理模組====================
        { buttonId: 'Button_basic_CarouselSetting', hiddenInputId: 'hiddencarouselsetting' },             //=====輪播圖維護=====
        { buttonId: 'Button_basic_FastLinkSetting', hiddenInputId: 'hiddenfastlinksetting' },             //=====快速連結設定=====
        { buttonId: 'Button_basic_NewsSetting', hiddenInputId: 'hiddennewsetting' },                      //=====最新消息維護===== 
        { buttonId: 'Button_basic_NormalQuestionSetting', hiddenInputId: 'hiddennormalquestionsetting' }, //=====常見問題資訊維護=====
        { buttonId: 'Button_basic_NoticesSetting', hiddenInputId: 'hiddennoticesetting' },                //=====注意事項維護=====
        { buttonId: 'Button_basic_PaymentSetting', hiddenInputId: 'hiddenpaymentsetting' },               //=====付款提示維護=====
        { buttonId: 'Button_basic_UnitImageSetting', hiddenInputId: 'hiddenunitimagesetting' },           //=====單元形象維護=====
    ];

    buttons.forEach(button => {
        const buttonElement = document.getElementById(button.buttonId);
        const hiddenInputElement = document.getElementById(button.hiddenInputId);
        buttonElement.className = 'btn btn-secondary';
        buttonElement.innerText = '啟用';
        hiddenInputElement.value = 'N';
    });
});

//========================================模組按鈕設定========================================
//====================報名管理模組====================
//=====一般考生報名=====
document.getElementById('Button_exam_Registration').addEventListener('click', function() {
    toggleButton(this, 'hiddenExamRegistration');});
//=====機關薦送報名=====
document.getElementById('Button_agnecy_Registration').addEventListener('click', function() {
        toggleButton(this, 'hiddenAgencyRegistration');});
//====================系統管理模組====================(帳號權限設定另外撰寫至back_accountFunctionView.js)
//=====系統環境設定=====
document.getElementById('Button_system_EnvironmentSetting').addEventListener('click', function() {
    toggleButton(this, 'hiddenenvironmentsetting');});
//=====SMTP設定=====
document.getElementById('Button_system_SMTPSetting').addEventListener('click', function() {
    toggleButton(this, 'hiddensmtpsetting');});
//=====系統登入查詢=====
document.getElementById('Button_system_SystemSearch').addEventListener('click', function() {
    toggleButton(this, 'hiddensystemsearch');});
//====================基本管理模組====================
//=====輪播圖維護=====
document.getElementById('Button_basic_CarouselSetting').addEventListener('click', function() {
    toggleButton(this, 'hiddencarouselsetting');});
//=====快速連結設定=====
document.getElementById('Button_basic_FastLinkSetting').addEventListener('click', function() {
    toggleButton(this, 'hiddenfastlinksetting');});
//=====最新消息維護=====
document.getElementById('Button_basic_NewsSetting').addEventListener('click', function() {
    toggleButton(this, 'hiddennewsetting');});
//=====常見問題資訊維護=====
document.getElementById('Button_basic_NormalQuestionSetting').addEventListener('click', function() {
    toggleButton(this, 'hiddennormalquestionsetting');});
//=====注意事項維護=====
document.getElementById('Button_basic_NoticesSetting').addEventListener('click', function() {
    toggleButton(this, 'hiddennoticesetting');});
//=====付款提示維護=====
document.getElementById('Button_basic_PaymentSetting').addEventListener('click', function() {
    toggleButton(this, 'hiddenpaymentsetting');});   
//=====單元形象維護=====
document.getElementById('Button_basic_UnitImageSetting').addEventListener('click', function() {
    toggleButton(this, 'hiddenunitimagesetting');});   
        
//======================共用函式======================
function toggleButton(button, hiddenInputId) {
    var hiddenInput = document.getElementById(hiddenInputId);

    if (button.classList.contains('btn-secondary')) {
        button.classList.remove('btn-secondary');
        button.classList.add('btn-primary');
        button.textContent = '關閉';
        hiddenInput.value = 'Y';
    } else {
        button.classList.remove('btn-primary');
        button.classList.add('btn-secondary');
        button.textContent = '啟用';
        hiddenInput.value = 'N';
    }
}
//======================畫面載入時模組隱藏表單預設為N======================
window.onload = function() {
//====================報名管理模組====================
//=====一般考生報名
    document.getElementById('hiddenExamRegistration').value = 'N';
//=====機關薦送報名
    document.getElementById('hiddenAgencyRegistration').value = 'N';
//====================系統管理模組====================
//=====帳號權限設定-新增=====
    document.getElementById('hiddenaccountadd').value = 'N';
//=====帳號權限設定-修改=====
    document.getElementById('hiddenaccountmodify').value = 'N';
//=====帳號權限設定-重設密碼=====
    document.getElementById('hiddenpasswordReset').value = 'N';
//=====系統環境設定=====
    document.getElementById('hiddenenvironmentsetting').value = 'N';
//=====SMTP設定=====
    document.getElementById('hiddensmtpsetting').value = 'N';
//=====系統登入查詢=====
    document.getElementById('hiddensystemsearch').value = 'N';
//====================基本管理模組====================
//=====輪播圖維護=====
    document.getElementById('hiddencarouselsetting').value = 'N';
//=====快速連結設定=====
    document.getElementById('hiddenfastlinksetting').value = 'N';
//=====最新消息維護=====
    document.getElementById('hiddennewsetting').value = 'N';
//=====常見問題資訊維護=====
    document.getElementById('hiddennormalquestionsetting').value = 'N';
//=====注意事項維護=====
    document.getElementById('hiddennoticesetting').value = 'N';
//=====付款提示維護=====
    document.getElementById('hiddenpaymentsetting').value = 'N';
//=====單元形象維護=====
    document.getElementById('hiddenunitimagesetting').value = 'N';
};

