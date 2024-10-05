tinymce.init({
    selector: "#examInfoContent, #registerContent", // 分開每個選擇器
    auto_focus: "#examInfoContent",
    language: "zh_TW",
    theme: "modern",
    plugins: "advlist autolink link image lists charmap print preview",
    mobile: {
        theme: "mobile",
        plugins: ["autosave", "lists", "autolink"],
        toolbar: ["undo", "bold", "italic", "styleselect", "wordcount"]
    },
    setup: function(editor) {
        editor.on('init', function() {
            var hiddenInputId = editor.getElement().id === "examInfoContent" ? "hiddenexamInfoContent" : "hiddenregisterContent";
            var hiddenInput = document.getElementById(hiddenInputId);
            hiddenInput.value = editor.getContent(); // 設定隱藏輸入框的值
        });

        editor.on('change', function() {
            var hiddenInputId = editor.getElement().id === "examInfoContent" ? "hiddenexamInfoContent" : "hiddenregisterContent";
            var hiddenInput = document.getElementById(hiddenInputId);
            hiddenInput.value = editor.getContent(); // 在改變事件中也設定隱藏輸入框的值
        });
    }
});

//==========通用函數設定==========
function syncInputValues(inputId, hiddenInputId) {
    const inputElement = document.getElementById(inputId);
    const hiddenInputElement = document.getElementById(hiddenInputId);

    inputElement.addEventListener('input', function() {
        hiddenInputElement.value = inputElement.value;
    });
}

//==========表單插入假表單==========
//=====考試類別代號和考試類別標題=====
syncInputValues('inputExamStyleID', 'hiddeninputExamStyleID');
syncInputValues('inputExamTitle', 'hiddeninputExamTitle');
//==========顯示於平台==========
function toggleButtonshowdesk() {
    const buttonshowdesk = document.getElementById('showdesk');
    const hiddenshowdesk = document.getElementById('hiddenshowdesk');
    
    if (hiddenshowdesk.value === 'N') {
        hiddenshowdesk.value = 'Y';
        buttonshowdesk.textContent = '關閉';
        buttonshowdesk.classList.remove('btn-secondary');
        buttonshowdesk.classList.add('btn-warning');
    } else {
        hiddenshowdesk.value = 'N';
        buttonshowdesk.textContent = '開啟';
        buttonshowdesk.classList.remove('btn-warning');
        buttonshowdesk.classList.add('btn-secondary');
    }
}
//==========開放報名===========
function toggleButtonopenRegister() {
    const buttonopenRegister = document.getElementById('openRegister');
    const hiddenopenRegister = document.getElementById('hiddenopenRegister');
    
    if (hiddenopenRegister.value === 'N') {
        hiddenopenRegister.value = 'Y';
        buttonopenRegister.textContent = '關閉';
        buttonopenRegister.classList.remove('btn-secondary');
        buttonopenRegister.classList.add('btn-warning');
    } else {
        hiddenopenRegister.value = 'N';
        buttonopenRegister.textContent = '開啟';
        buttonopenRegister.classList.remove('btn-warning');
        buttonopenRegister.classList.add('btn-secondary');
    }
}

//==========梯次設定和級別設定==========
syncInputValues('ladder', 'hiddenladder');
syncInputValues('level', 'hiddenlevel');
//==========北部地區人數、中部地區人數、南部地區人數、東部地區人數、離島地區人數設定==========
syncInputValues('registerCount_N', 'hiddenregisterCount_N');
syncInputValues('registerCount_C', 'hiddenregisterCount_C');
syncInputValues('registerCount_S', 'hiddenregisterCount_S');
syncInputValues('registerCount_E', 'hiddenregisterCount_E');
syncInputValues('registerCount_I', 'hiddenregisterCount_I');
//==========一般考生費用和薦送考生費用設定==========
syncInputValues('generalPayment', 'hiddengeneralPayment');
syncInputValues('agencyPayment', 'hiddenagencyPayment');
//==========年齡限制設定==========
syncInputValues('ageLimit', 'hiddenageLimit');
//==========考試資訊內文和報名填寫內文設定==========
syncInputValues('examInfoContent', 'hiddenexamInfoContent');
syncInputValues('registerContent', 'hiddenregisterContent');
//==========考試日期設定==========
syncInputValues('examDate', 'hiddenexamDate');
//==========文章上架和下架日期設定==========
syncInputValues('articleUpdateTime', 'hiddenarticleUpdateTime');
syncInputValues('articleRemoveTime', 'hiddenarticleRemoveTime');
//==========一般報名開始日期和一般報名結束日期設定==========
syncInputValues('examRegistrationStartDate', 'hiddenexamRegistrationStartDate');
syncInputValues('examRegistrationEndDate', 'hiddenexamRegistrationEndDate');
//==========機關報名開始日期和機關報名結束日期設定==========
syncInputValues('agencyRegistrationStartDate', 'hiddenagencyRegistrationStartDate');
syncInputValues('agencyRegistrationEndDate', 'hiddenagencyRegistrationEndDate');
//==========一般報名繳費開始日期和一般報名繳費結束日設定==========
syncInputValues('examPaymentStartDate', 'hiddenexamPaymentStartDate');
syncInputValues('examPaymentEndDate', 'hiddenexamPaymentEndDate');
//==========薦送報名繳費開始日期和薦送報名繳費結束日期設定==========
syncInputValues('agencyPaymentStartDate', 'hiddenagencyPaymentStartDate');
syncInputValues('agencyPaymentEndDate', 'hiddenagencyPaymentEndDate');
//==========考試通知單下載起始日期和考試通知單下載結束日期設定==========
syncInputValues('examNoticeDownloadStartDate', 'hiddenexamNoticeDownloadStartDate');
syncInputValues('examNoticeDownloadEndDate', 'hiddenexamNoticeDownloadEndDate');
//==========成績查詢起始日期和成績查詢結束日期設定==========
syncInputValues('scoreSearchStartDate', 'hiddenscoreSearchStartDate');
syncInputValues('scoreSearchEndDate', 'hiddenscoreSearchEndDate');
//==========證書下載起始日期和證書下載結束日期設定==========
syncInputValues('certificateDownloadStartDate', 'hiddencertificateDownloadStartDate');
syncInputValues('certificateDownloadEndDate', 'hiddencertificateDownloadEndDate');

//==========元件：「確定送出」按鈕觸發必要事件==========//
$(document).ready(function() {
    $('#submitBtn').on('click', function(e) {
        
        // ==========第一部分：設定所屬類別如果是空白，於元件下方顯示錯誤文字==========//
        e.preventDefault();
        var isValid = true;
        var fields = [
            // ==========所屬類別、標題 =========//
            { id: '#inputExamStyleID', error: '#errorTextID' },
            { id: '#inputExamTitle', error: '#errorText' },
            // ==========顯示於前台、開放報名=========//
            { id: '#ladder', error: '#ladderErrorText' },
            { id: '#level',error:'#levelErrorText'},
            // ==========北部地區人數設定、中部地區人數設定、南部地區人數設定、東部地區人數設定、離島地區人數設定=========//
            { id: '#registerCount_N',error:'#registerCount_N_ErrorText'},
            { id: '#registerCount_C',error:'#registerCount_C_ErrorText'},
            { id: '#registerCount_S',error:'#registerCount_S_ErrorText'},
            { id: '#registerCount_E',error:'#registerCount_E_ErrorText'},
            { id: '#registerCount_I',error:'#registerCount_I_ErrorText'},
            // ==========一般考生費用、薦送考生費用=========//
            { id: '#generalPayment',error:'#generalPayment_ErrorText'},
            { id: '#agencyPayment',error:'#agencyPayment_ErrorText'},
            // ==========年齡限制=========//
            { id: '#ageLimit',error:'#ageLimit_ErrorText'},
            // ==========考試資訊內文、報名填寫內文=========//
            // { id: '#examInfoContent',error:'#examInfoContent_ErrorText'},
            // { id: '#registerContent',error:'#registerContent_ErrorText'},
            // ==========考試日期=========//
            { id: '#examDate',error:'#examDate_ErrorText'},
            // ==========文章上架日期、文章下架日期=========//
            { id: '#articleUpdateTime',error:'#articleUpdateTime_ErrorText'},
            { id: '#articleRemoveTime',error:'#articleRemoveTime_ErrorText'},
            // ==========一般報名開始日期、一般報名結束日期=========//
            { id: '#examRegistrationStartDate',error:'#examRegistrationStartDate_ErrorText'},
            { id: '#examRegistrationEndDate',error:'#examRegistrationEndtDate_ErrorText'},
            // ==========機關報名開始日期、機關報名結束日期=========//
            { id: '#agencyRegistrationStartDate',error:'#agencyRegistrationStartDate_ErrorText'},
            { id: '#agencyRegistrationEndDate',error:'#agencyRegistrationEndDate_ErrorText'},
            // ==========一般報名繳費開始日期、一般報名繳費結束日期==========//
            { id: '#examPaymentStartDate',error:'#examPaymentStartDate_ErrorText'},
            { id: '#examPaymentEndDate',error:'#examPaymentEndDate_ErrorText'},
            // ==========薦送報名繳費開始日期、薦送報名繳費結束日期==========//
            { id: '#agencyPaymentStartDate',error:'#agencyPaymentStartDate_ErrorText'},
            { id: '#agencyPaymentEndDate',error:'#agencyPaymentEndDate_ErrorText'},
            // ==========考試通知單下載開始日期、考試通知單下載結束日期==========//
            { id: '#examNoticeDownloadStartDate',error:'#examNoticeDownloadStartDate_ErrorText'},
            { id: '#examNoticeDownloadEndDate',error:'#examNoticeDownloadEndDate_ErrorText'},
            // ==========成績查詢開始日期、成績查詢結束日期==========//
            { id: '#scoreSearchStartDate',error:'#scoreSearchStartDate_ErrorText'},
            { id: '#scoreSearchEndDate',error:'#scoreSearchEndDate_ErrorText'},
            // ==========證書下載開始日期、證書下載結束日期==========//
            { id: '#certificateDownloadStartDate',error:'#certificateDownloadStartDate_ErrorText'},
            { id: '#certificateDownloadEndDate',error:'#certificateDownloadEndDate_ErrorText'},
        ];

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
        
        // ==========第二部分：判定各區塊起始日期是否有大於結束日期，若有則在起始日期區塊顯示錯誤文字==========//
        // ==========文章上架日期&文章下架日期==========//
        var errorMessage = '';
        var articleUpdateTime = $('#articleUpdateTime').val().trim();
        var articleRemoveTime = $('#articleRemoveTime').val().trim();
        if (articleUpdateTime && articleRemoveTime) {
            if (articleUpdateTime > articleRemoveTime) {
                errorMessage = '文章上架日期不能晚於文章下架日期';
                $('#articleUpdateTime').addClass('is-invalid');
                $('#articleUpdateTime_ErrorText').text(errorMessage).removeClass('d-none');
                isValid = false;
            }
        }
        // ==========一般報名開始日期&一般報名結束日期==========//
        var examRegistrationStartDate = $('#examRegistrationStartDate').val().trim();
        var examRegistrationEndDate = $('#examRegistrationEndDate').val().trim();
        if (examRegistrationStartDate && examRegistrationEndDate) {
            if (examRegistrationStartDate > examRegistrationEndDate) {
                errorMessage = '一般報名開始日期不能晚於一般報名結束日期';
                $('#examRegistrationStartDate').addClass('is-invalid');
                $('#examRegistrationStartDate_ErrorText').text(errorMessage).removeClass('d-none');
                isValid = false;
            }
        }
        // ==========機關報名開始日期&機關報名結束日期==========//
        var agencyRegistrationStartDate = $('#agencyRegistrationStartDate').val().trim();
        var agencyRegistrationEndDate = $('#agencyRegistrationEndDate').val().trim();
        if (agencyRegistrationStartDate && agencyRegistrationEndDate) {
            if (agencyRegistrationStartDate > agencyRegistrationEndDate) {
                errorMessage = '機關報名開始日期不能晚於機關報名結束日期';
                $('#agencyRegistrationStartDate').addClass('is-invalid');
                $('#agencyRegistrationStartDate_ErrorText').text(errorMessage).removeClass('d-none');
                isValid = false;
            }
        }
        // ==========一般報名繳費開始日期&一般報名繳費結束日期==========//   
        var examPaymentStartDate = $('#examPaymentStartDate').val().trim();
        var examPaymentEndDate = $('#examPaymentEndDate').val().trim();
        if (examPaymentStartDate && examPaymentEndDate) {
            if (examPaymentStartDate > examPaymentEndDate) {
                errorMessage = '一般報名繳費開始日期不能晚於一般報名繳費結束日期';
                $('#examPaymentStartDate').addClass('is-invalid');
                $('#examPaymentStartDate_ErrorText').text(errorMessage).removeClass('d-none');
                isValid = false;
            }
        }

        // ==========薦送報名繳費開始日期&薦送報名繳費結束日期	==========//   
        var agencyPaymentStartDate = $('#agencyPaymentStartDate').val().trim();
        var agencyPaymentEndDate = $('#agencyPaymentEndDate').val().trim();
        if (agencyPaymentStartDate && agencyPaymentEndDate) {
            if (agencyPaymentStartDate > agencyPaymentEndDate) {
                errorMessage = '薦送報名繳費開始日期不能晚於薦送報名繳費結束日期';
                $('#agencyPaymentStartDate').addClass('is-invalid');
                $('#agencyPaymentStartDate_ErrorText').text(errorMessage).removeClass('d-none');
                isValid = false;
            }
        }

        // ==========考試通知單下載起始日期&考試通知單下載結束日期==========//   
        var examNoticeDownloadStartDate = $('#examNoticeDownloadStartDate').val().trim();
        var examNoticeDownloadEndDate = $('#examNoticeDownloadEndDate').val().trim();
        if (examNoticeDownloadStartDate && examNoticeDownloadEndDate) {
            if (examNoticeDownloadStartDate > examNoticeDownloadEndDate) {
                errorMessage = '考試通知單下載起始日期不能晚於考試通知單下載結束日期';
                $('#examNoticeDownloadStartDate').addClass('is-invalid');
                $('#examNoticeDownloadStartDate_ErrorText').text(errorMessage).removeClass('d-none');
                isValid = false;
            }
        }

        // ==========成績查詢開始日期&成績查詢結束日期==========//   
        var scoreSearchStartDate = $('#scoreSearchStartDate').val().trim();
        var scoreSearchEndDate = $('#scoreSearchEndDate').val().trim();
        if (scoreSearchStartDate && scoreSearchEndDate) {
            if (scoreSearchStartDate > scoreSearchEndDate) {
                errorMessage = '考試通知單下載起始日期不能晚於考試通知單下載結束日期';
                $('#scoreSearchStartDate').addClass('is-invalid');
                $('#scoreSearchEndDate').text(errorMessage).removeClass('d-none');
                isValid = false;
            }
        }

        // ==========證書下載開始日期&證書下載結束日期==========//  
        var certificateDownloadStartDate = $('#certificateDownloadStartDate').val().trim();
        var certificateDownloadEndDate = $('#certificateDownloadEndDate').val().trim();
        if (certificateDownloadStartDate && certificateDownloadEndDate) {
            if (certificateDownloadStartDate > certificateDownloadEndDate) {
                errorMessage = '考試通知單下載起始日期不能晚於考試通知單下載結束日期';
                $('#certificateDownloadStartDate').addClass('is-invalid');
                $('#certificateDownloadStartDate').text(errorMessage).removeClass('d-none');
                isValid = false;
            }
        }

        if (isValid) {
            $('#SaveModal').modal('show');
        }
    });
});

//==========元件：「重新設定」按鈕觸發必要事件==========//
$(document).ready(function() {
    // 定義初始值
    var initialValues = {
        inputExamStyleID: $('#inputExamStyleID').val(),
        inputExamTitle: $('#inputExamTitle').val(),
        ladder: $('#ladder').val(),
        level: $('#level').val(),
        registerCount_N: $('#registerCount_N').val(),
        registerCount_C: $('#registerCount_C').val(),
        registerCount_S: $('#registerCount_S').val(),
        registerCount_E: $('#registerCount_E').val(),
        registerCount_I: $('#registerCount_I').val(),
        generalPayment: $('#generalPayment').val(),
        agencyPayment: $('#agencyPayment').val(),
        ageLimit: $('#ageLimit').val(),
        examInfoContent: $('#examInfoContent').val(),
        registerContent: $('#registerContent').val(),
        examDate: $('#examDate').val(),
        articleUpdateTime: $('#articleUpdateTime').val(),
        articleRemoveTime: $('#articleRemoveTime').val(),
        examRegistrationStartDate: $('#examRegistrationStartDate').val(),
        examRegistrationEndDate: $('#examRegistrationEndDate').val(),
        agencyRegistrationStartDate: $('#agencyRegistrationStartDate').val(),
        agencyRegistrationEndDate: $('#agencyRegistrationEndDate').val(),
        examPaymentStartDate: $('#examPaymentStartDate').val(),
        examPaymentEndDate: $('#examPaymentEndDate').val(),
        agencyPaymentStartDate: $('#agencyPaymentStartDate').val(),
        agencyPaymentEndDate: $('#agencyPaymentEndDate').val(),
        examNoticeDownloadStartDate: $('#examNoticeDownloadStartDate').val(),
        examNoticeDownloadEndDate: $('#examNoticeDownloadEndDate').val(),
        scoreSearchStartDate: $('#scoreSearchStartDate').val(),
        scoreSearchEndDate: $('#scoreSearchEndDate').val(),
        certificateDownloadStartDate: $('#certificateDownloadStartDate').val(),
        certificateDownloadEndDate: $('#certificateDownloadEndDate').val()
    };

    // 點擊重設按鈕事件
    $('#resetButton').on('click', function(e) {
        e.preventDefault();
        // 將每個元素的值重設為初始值
        $.each(initialValues, function(key, value) {
            $('#' + key).val(value);
        });
    });
});