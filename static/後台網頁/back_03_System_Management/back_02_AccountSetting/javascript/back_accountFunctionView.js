$(document).ready(function(){
    $("#flip").click(function(){
        console.log("Flip clicked"); // 確認點擊事件是否觸發
        $("#panel").slideToggle("slow", function() {
            console.log("Panel toggled"); // 確認 slideToggle 是否完成
        });
    });
});

$(document).ready(function(){
    $("#flip2").click(function(){
        console.log("Flip clicked"); // 確認點擊事件是否觸發
        $("#panel2").slideToggle("slow", function() {
            console.log("Panel toggled"); // 確認 slideToggle 是否完成
        });
    });
});

$(document).ready(function(){
    $("#flip3").click(function(){
        console.log("Flip clicked"); // 確認點擊事件是否觸發
        $("#panel3").slideToggle("slow", function() {
            console.log("Panel toggled"); // 確認 slideToggle 是否完成
        });
    });
});

//==============================================================================

document.getElementById('toggleButtonAdd').addEventListener('click', function() {
    toggleButton(this, 'hiddenSubAccountAdd');
});

document.getElementById('toggleButtonSearch').addEventListener('click', function() {
    toggleButton(this, 'hiddenSubAccountSearch');
});

document.getElementById('toggleButtonReset').addEventListener('click', function() {
    toggleButton(this, 'hiddenSubPasswordReset');
});

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

//=====關閉畫面==============================
function closeWindow() {
    window.close();
}

//=====重新設定==============================
function resetForm() {
    // 設置按鈕為 btn-secondary 並將文字設為 "啟用"
    document.getElementById('toggleButtonAdd').className = 'btn btn-secondary';
    document.getElementById('toggleButtonAdd').innerText = '啟用';

    document.getElementById('toggleButtonSearch').className = 'btn btn-secondary';
    document.getElementById('toggleButtonSearch').innerText = '啟用';

    document.getElementById('toggleButtonReset').className = 'btn btn-secondary';
    document.getElementById('toggleButtonReset').innerText = '啟用';

    // 設置隱藏輸入框的值為 'N'
    document.getElementById('hiddenSubAccountAdd').value = 'N';
    document.getElementById('hiddenSubAccountSearch').value = 'N';
    document.getElementById('hiddenSubPasswordReset').value = 'N';
}

//將值存儲到 Local Storage，並跳轉到accountSetting.html網頁：
function passValuesAndClose() {
    const hiddenSubAccountAdd = document.getElementById('hiddenSubAccountAdd').value;
    const hiddenSubAccountSearch = document.getElementById('hiddenSubAccountSearch').value;
    const hiddenSubPasswordReset = document.getElementById('hiddenSubPasswordReset').value;

    if (window.opener) {
        window.opener.document.getElementById('hiddenaccountadd').value = hiddenSubAccountAdd;
        window.opener.document.getElementById('hiddenaccountmodify').value = hiddenSubAccountSearch;
        window.opener.document.getElementById('hiddenpasswordReset').value = hiddenSubPasswordReset;
    }
    // window.location.href = '/backAccountSetting';
    window.close();
}