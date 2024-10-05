//====================重新設定按鈕設定====================
tinymce.init({
    selector: "#inputDescription, #inputPrivacy",
    auto_focus: "inputDescription",
    language: "zh_TW",
    theme: "modern",
    plugins: "advlist autolink link image lists charmap print preview",
    mobile: {
        theme: "mobile",
        plugins: ["autosave", "lists", "autolink"],
        toolbar: ["undo", "bold", "italic", "styleselect", "wordcount"]
    },
});


//====================維護啟動按鈕設定====================
document.getElementById("switch").addEventListener("click", function(event) {
    event.preventDefault(); // 防止鏈接的默認行為

    var button = document.getElementById("switch");
    var hiddenInput = document.getElementById("hiddenswitchcarouselsetting");

    if (button.classList.contains("btn-primary")) {
        button.classList.remove("btn-primary");
        button.classList.add("btn-secondary");
        button.textContent = "關閉";
        hiddenInput.value = "Y";
    } else {
        button.classList.remove("btn-secondary");
        button.classList.add("btn-primary");
        button.textContent = "啟用";
        hiddenInput.value = "N";
    }
});

//====================網頁表單內容填入假表單，由假表單送出資料====================
//=====啟動時間=====
document.addEventListener("DOMContentLoaded", function() {
    var UpLoadTime = document.querySelector('input[name="UpLoadTime"]');
    var hiddenUpLoadTime = document.querySelector('input[name="hiddenUpLoadTime"]');
    hiddenUpLoadTime.value = UpLoadTime.value;
    UpLoadTime.addEventListener('input', function() {
        hiddenUpLoadTime.value = UpLoadTime.value;
    });
});
//=====結束時間=====
document.addEventListener("DOMContentLoaded", function() {
    var RemoveTime = document.querySelector('input[name="RemoveTime"]');
    var hiddenRemoveTime = document.querySelector('input[name="hiddenRemoveTime"]');
    hiddenRemoveTime.value = RemoveTime.value;
    RemoveTime.addEventListener('input', function() {
        hiddenRemoveTime.value = RemoveTime.value;
    });
});
//=====維護內容標題=====
document.addEventListener("DOMContentLoaded", function() {
    var inputWebTitle = document.querySelector('input[name="inputWebTitle"]');
    var hiddeninputWebTitle = document.querySelector('input[name="hiddeninputWebTitle"]');
    hiddeninputWebTitle.value = inputWebTitle.value;
    inputWebTitle.addEventListener('input', function() {
        hiddeninputWebTitle.value = inputWebTitle.value;
    });
});
//=====維護信件名稱=====
document.addEventListener("DOMContentLoaded", function() {
    var inputEmailTitle = document.querySelector('input[name="inputEmailTitle"]');
    var hiddeninputEmailTitle = document.querySelector('input[name="hiddeninputEmailTitle"]');
    hiddeninputEmailTitle.value = inputEmailTitle.value;
    inputEmailTitle.addEventListener('input', function() {
        hiddeninputEmailTitle.value = inputEmailTitle.value;
    });
});
//=====維護內容=====
document.addEventListener("DOMContentLoaded", function() {
    var inputDescription = document.querySelector('textarea[name="inputDescription"]');
    var hiddeninputDescription = document.querySelector('textarea[name="hiddeninputDescription"]');
    
    // 初始化隱藏textarea的值
    hiddeninputDescription.value = inputDescription.value;

    // 當textarea的內容改變時，同步更新隱藏textarea的值
    inputDescription.addEventListener('input', function() {
        hiddeninputDescription.value = inputDescription.value;
    });
});
//=====地址=====
document.addEventListener("DOMContentLoaded", function() {
    var inputAddress = document.querySelector('input[name="inputAddress"]');
    var hiddeninputAddress = document.querySelector('input[name="hiddeninputAddress"]');
    hiddeninputAddress.value = inputAddress.value;
    inputAddress.addEventListener('input', function() {
        hiddeninputAddress.value = inputAddress.value;
    });
});
//=====總機=====
document.addEventListener("DOMContentLoaded", function() {
    var inputswitchboard = document.querySelector('input[name="inputswitchboard"]');
    var hiddeninputswitchboard = document.querySelector('input[name="hiddeninputswitchboard"]');
    hiddeninputswitchboard.value = inputswitchboard.value;
    inputswitchboard.addEventListener('input', function() {
        hiddeninputswitchboard.value = inputswitchboard.value;
    });
});
//=====傳真=====
document.addEventListener("DOMContentLoaded", function() {
    var inputFax = document.querySelector('input[name="inputFax"]');
    var hiddeninputFax = document.querySelector('input[name="hiddeninputFax"]');
    hiddeninputFax.value = inputFax.value;
    inputFax.addEventListener('input', function() {
        hiddeninputFax.value = inputFax.value;
    });
});
//=====隱私政策=====
document.addEventListener("DOMContentLoaded", function() {
    var inputPrivacy = document.querySelector('input[name="inputPrivacy"]');
    var hiddeninputPrivacy = document.querySelector('input[name="hiddeninputPrivacy"]');
    hiddeninputPrivacy.value = inputPrivacy.value;
    inputPrivacy.addEventListener('input', function() {
        hiddeninputPrivacy.value = inputPrivacy.value;
    });
});

