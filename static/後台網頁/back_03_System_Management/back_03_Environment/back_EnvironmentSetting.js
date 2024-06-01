document.addEventListener("DOMContentLoaded", function() {
    var switchcarouselsetting = document.querySelector('input[name="switchcarouselsetting"]');
    var hiddenswitchcarouselsetting = document.querySelector('input[name="hiddenswitchcarouselsetting"]');
    // 將 checkbox 的值設置到 hiddenInput 的值中
    hiddenswitchcarouselsetting.value = switchcarouselsetting.checked ? "true" : "false";
    // 監聽 checkbox 的改變事件
    switchcarouselsetting.addEventListener('change', function() {
    // 將 checkbox 的值設置到 hiddenInput 的值中
    hiddenswitchcarouselsetting.value = switchcarouselsetting.checked ? "true" : "false";
    });
});


document.addEventListener("DOMContentLoaded", function() {
    var UpLoadTime = document.querySelector('input[name="UpLoadTime"]');
    var hiddenUpLoadTime = document.querySelector('input[name="hiddenUpLoadTime"]');
    hiddenUpLoadTime.value = UpLoadTime.value;
    UpLoadTime.addEventListener('input', function() {
        hiddenUpLoadTime.value = UpLoadTime.value;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var RemoveTime = document.querySelector('input[name="RemoveTime"]');
    var hiddenRemoveTime = document.querySelector('input[name="hiddenRemoveTime"]');
    hiddenRemoveTime.value = RemoveTime.value;
    RemoveTime.addEventListener('input', function() {
        hiddenRemoveTime.value = RemoveTime.value;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var inputWebTitle = document.querySelector('input[name="inputWebTitle"]');
    var hiddeninputWebTitle = document.querySelector('input[name="hiddeninputWebTitle"]');
    hiddeninputWebTitle.value = inputWebTitle.value;
    inputWebTitle.addEventListener('input', function() {
        hiddeninputWebTitle.value = inputWebTitle.value;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var inputEmailTitle = document.querySelector('input[name="inputEmailTitle"]');
    var hiddeninputEmailTitle = document.querySelector('input[name="hiddeninputEmailTitle"]');
    hiddeninputEmailTitle.value = inputEmailTitle.value;
    inputEmailTitle.addEventListener('input', function() {
        hiddeninputEmailTitle.value = inputEmailTitle.value;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var inputDescription = document.querySelector('input[name="inputDescription"]');
    var hiddeninputDescription = document.querySelector('input[name="hiddeninputDescription"]');
    hiddeninputDescription.value = inputDescription.value;
    inputDescription.addEventListener('input', function() {
        hiddeninputDescription.value = inputDescription.value;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var inputAddress = document.querySelector('input[name="inputAddress"]');
    var hiddeninputAddress = document.querySelector('input[name="hiddeninputAddress"]');
    hiddeninputAddress.value = inputAddress.value;
    inputAddress.addEventListener('input', function() {
        hiddeninputAddress.value = inputAddress.value;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var inputswitchboard = document.querySelector('input[name="inputswitchboard"]');
    var hiddeninputswitchboard = document.querySelector('input[name="hiddeninputswitchboard"]');
    hiddeninputswitchboard.value = inputswitchboard.value;
    inputswitchboard.addEventListener('input', function() {
        hiddeninputswitchboard.value = inputswitchboard.value;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var inputFax = document.querySelector('input[name="inputFax"]');
    var hiddeninputFax = document.querySelector('input[name="hiddeninputFax"]');
    hiddeninputFax.value = inputFax.value;
    inputFax.addEventListener('input', function() {
        hiddeninputFax.value = inputFax.value;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var inputPrivacy = document.querySelector('input[name="inputPrivacy"]');
    var hiddeninputPrivacy = document.querySelector('input[name="hiddeninputPrivacy"]');
    hiddeninputPrivacy.value = inputPrivacy.value;
    inputPrivacy.addEventListener('input', function() {
        hiddeninputPrivacy.value = inputPrivacy.value;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var normalQuestionTitle= document.querySelector('input[name="normalQuestionTitle"]');
    var hiddennormalQuestionTitle= document.querySelector('input[name="hiddennormalQuestionTitle"]');
    
    // 初始化时将normalQuestionTitle的值填入hiddennormalQuestionTitle
    hiddennormalQuestionTitle.value = normalQuestionTitle.value;
    
    // 监听normalQuestionTitle的输入事件，保持两者的值同步
    normalQuestionTitle.addEventListener('input', function() {
        hiddennormalQuestionTitle.value = normalQuestionTitle.value;
    });
});