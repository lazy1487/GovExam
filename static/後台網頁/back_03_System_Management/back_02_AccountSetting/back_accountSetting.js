// 獲取「全部開啟」按鈕
var allOpenButton = document.getElementById('allOpen');
var allCloseButton = document.getElementById('allClose');
// 添加點擊事件監聽器
allOpenButton.addEventListener('click', function() {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = true;
        checkbox.value = 'true';
    });
});

allCloseButton.addEventListener('click',function(){
    var checkboxes = document.querySelectorAll('.form-check-input');

    // 將每個 checkbox 設置為選中
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = false;
        checkbox.value = 'false';
    }); 
})

document.getElementById('allClose').addEventListener('click', function() {
    // 取得所有的 input 元素
    var inputs = document.querySelectorAll('input.form-control');
    // 逐一清除每個 input 元素的值
    inputs.forEach(function(input) {
        input.value = '';
    });
});

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

var inputEmail = document.getElementById('inputEmail');
var hiddenEmail = document.getElementById('hiddenEmail');
inputEmail.addEventListener('input', function() {hiddenEmail.value = inputEmail.value;});

var statusSelect = document.getElementById('statusSelect');
var hiddenStatusSelect = document.getElementById('hiddenStatusSelect');
statusSelect.addEventListener('change', function() {
    var selectedOption = statusSelect.options[statusSelect.selectedIndex];
    var selectedValue = selectedOption.value;
    hiddenStatusSelect.value = selectedValue;
});

var inputaccountadd = document.getElementById('inputaccountadd');
var hiddenaccountadd = document.getElementById('hiddenaccountadd');
inputaccountadd.addEventListener('click', function() {
    hiddenaccountadd.value = inputaccountadd.checked ? "true" : "false";
});

var inputaccountmodify = document.getElementById('inputaccountmodify');
var hiddenaccountmodify = document.getElementById('hiddenaccountmodify');
inputaccountmodify.addEventListener('click', function() {
    hiddenaccountmodify.value = inputaccountmodify.checked ? "true" : "false";
});

var inputenvironmentsetting = document.getElementById('inputenvironmentsetting');
var hiddenenvironmentsetting = document.getElementById('hiddenenvironmentsetting');
inputenvironmentsetting.addEventListener('click', function() {
    hiddenenvironmentsetting.value = inputenvironmentsetting.checked ? "true" : "false";
});

var inputsmtpsetting = document.getElementById('inputsmtpsetting');
var hiddensmtpsetting = document.getElementById('hiddensmtpsetting');
inputsmtpsetting.addEventListener('click', function() {
    hiddensmtpsetting.value = inputsmtpsetting.checked ? "true" : "false";
});

var inputsystemsearch = document.getElementById('inputsystemsearch');
var hiddensystemsearch = document.getElementById('hiddensystemsearch');
inputsystemsearch.addEventListener('click', function() {
    hiddensystemsearch.value = inputsystemsearch.checked ? "true" : "false";
});

var inputuserecord = document.getElementById('inputuserecord');
var hiddenuserecord = document.getElementById('hiddenuserecord');
inputsystemsearch.addEventListener('click', function() {
    hiddenuserecord.value = inputuserecord.checked ? "true" : "false";
});

var inputcarouselsetting = document.getElementById('inputcarouselsetting');
var hiddencarouselsetting = document.getElementById('hiddencarouselsetting');
inputcarouselsetting.addEventListener('click', function() {
    hiddencarouselsetting.value = inputcarouselsetting.checked ? "true" : "false";
});

var inputfastlinksetting = document.getElementById('inputfastlinksetting');
var hiddenfastlinksetting = document.getElementById('hiddenfastlinksetting');
inputfastlinksetting.addEventListener('click', function() {
    hiddenfastlinksetting.value = inputfastlinksetting.checked ? "true" : "false";
});

var inputnewsetting = document.getElementById('inputnewsetting');
var hiddennewsetting = document.getElementById('hiddennewsetting');
inputnewsetting.addEventListener('click', function() {
    hiddennewsetting.value = inputnewsetting.checked ? "true" : "false";
});

var inputnormalquestionsetting = document.getElementById('inputnormalquestionsetting');
var hiddennormalquestionsetting = document.getElementById('hiddennormalquestionsetting');
inputnormalquestionsetting.addEventListener('click', function() {
    hiddennormalquestionsetting.value = inputnormalquestionsetting.checked ? "true" : "false";
});

var inputnoticesetting = document.getElementById('inputnoticesetting');
var hiddennoticesetting = document.getElementById('hiddennoticesetting');
inputnoticesetting.addEventListener('click', function() {
    hiddennoticesetting.value = inputnoticesetting.checked ? "true" : "false";
});

var inputpaymentsetting = document.getElementById('inputpaymentsetting');
var hiddenpaymentsetting = document.getElementById('hiddenpaymentsetting');
inputpaymentsetting.addEventListener('click', function() {
    hiddenpaymentsetting.value = inputpaymentsetting.checked ? "true" : "false";
});

var inputunitimagesetting = document.getElementById('inputunitimagesetting');
var hiddenunitimagesetting = document.getElementById('hiddenunitimagesetting');
inputunitimagesetting.addEventListener('click', function() {
    hiddenunitimagesetting.value = inputunitimagesetting.checked ? "true" : "false";
});