// ======假表單===============================================================================================

var inputName = document.getElementById("inputName");
var inputID = document.getElementById("inputID");
var inputAge = document.getElementById("inputAge");
var inputAddress = document.getElementById("inputAddress");
var inputPhone = document.getElementById("inputPhone");
var inputEmail = document.getElementById("inputEmail");
var inputAgency = document.getElementById("inputAgency");
var inputAgencyDepa = document.getElementById("inputAgencyDepa");
var inputAgencyPhone = document.getElementById("inputAgencyPhone");
var inputAgencyAddress = document.getElementById("inputAgencyAddress");

var hiddeninputName = document.getElementById("hiddeninputName");
var hiddeninputID = document.getElementById("hiddeninputID");
var hiddeninputAge = document.getElementById("hiddeninputAge");
var hiddeninputAddress = document.getElementById("hiddeninputAddress");
var hiddeninputPhone = document.getElementById("hiddeninputPhone");
var hiddeninputEmail = document.getElementById("hiddeninputEmail");
var hiddeninputAgency = document.getElementById("hiddeninputAgency");
var hiddeninputAgencyDepa = document.getElementById("hiddeninputAgencyDepa");
var hiddeninputAgencyPhone = document.getElementById("hiddeninputAgencyPhone");
var hiddeninputAgencyAddress = document.getElementById("hiddeninputAgencyAddress");

// 當 inputName 的值改變時，同步更新 hiddeninputName 的值
inputName.addEventListener('input', function() {
    if (hiddeninputName) {hiddeninputName.value = inputName.value;}
});

inputID.addEventListener('input', function() {
    if (hiddeninputID) {hiddeninputID.value = inputID.value;}
});

inputAge.addEventListener('input', function() {
    if (hiddeninputAge) {hiddeninputAge.value = inputAge.value;}
});

inputAddress.addEventListener('input', function() {
    if (hiddeninputAddress) {hiddeninputAddress.value = inputAddress.value;}
});

inputPhone.addEventListener('input', function() {
    if (hiddeninputPhone) {hiddeninputPhone.value = inputPhone.value;}
});

inputEmail.addEventListener('input', function() {
    if (hiddeninputEmail) {hiddeninputEmail.value = inputEmail.value;}
});

inputAgency.addEventListener('input', function() {
    if (hiddeninputAgency) {hiddeninputAgency.value = inputAgency.value;}
});

inputAgencyDepa.addEventListener('input', function() {
    if (hiddeninputAgencyDepa) {hiddeninputAgencyDepa.value = inputAgencyDepa.value;}
});

inputAgencyPhone.addEventListener('input', function() {
    if (hiddeninputAgencyPhone) {hiddeninputAgencyPhone.value = inputAgencyPhone.value;}
});

inputAgencyAddress.addEventListener('input', function() {
    if (hiddeninputAgencyAddress) {hiddeninputAgencyAddress.value = inputAgencyAddress.value;}
});

// ======重新按鈕設定=========================================================================================
var resetButton = document.getElementById('resetButton');

resetButton.addEventListener('click', function() {
    var inputName = document.getElementById("inputName");
    var inputID = document.getElementById("inputID");
    var inputAge = document.getElementById("inputAge");
    var inputAddress = document.getElementById("inputAddress");
    var inputPhone = document.getElementById("inputPhone");
    var inputEmail = document.getElementById("inputEmail");
    var inputAgency = document.getElementById("inputAgency");
    var inputAgencyDepa = document.getElementById("inputAgencyDepa");
    var inputAgencyPhone = document.getElementById("inputAgencyPhone");
    var inputAgencyAddress = document.getElementById("inputAgencyAddress");


    if (inputName) {inputName.value = '';}
    if (inputID) {inputID.value = '';}
    if (inputAge) {inputAge.value = '';}
    if (inputAddress) {inputAddress.value = '';}
    if (inputPhone) {inputPhone.value = '';}
    if (inputEmail) {inputEmail.value = '';}
    if (inputAgency) {inputAgency.value = '';}
    if (inputAgencyDepa) {inputAgencyDepa.value = '';}
    if (inputAgencyPhone) {inputAgencyPhone.value = '';}
    if (inputAgencyAddress) {inputAgencyAddress.value = '';}
});

