// ======假表單===============================================================================================
var elements = [
    { id: "AgencyDepartmentID", hiddenId: "hiddenAgencyDepartmentID" },
    { id: "AgencyDepartmentName", hiddenId: "hiddenAgencyDepartmentName" },
    { id: "AgencyDepartmentAreaCode", hiddenId: "hiddenAgencyDepartmentAreaCode" },
    { id: "AgencyDepartmentAddress", hiddenId: "hiddenAgencyDepartmentAddress" },
    { id: "AgencyDepartmentTyped", hiddenId: "hiddenAgencyDepartmentTyped" },
    { id: "Agencyaffiliated", hiddenId: "hiddenAgencyaffiliated" },
    { id: "AgencyDepartmentPhone", hiddenId: "hiddenAgencyDepartmentPhone" },
    { id: "AgencyDepartmentFax", hiddenId: "hiddenAgencyDepartmentFax" }
];

// 遍歷陣列，為每個元素添加事件監聽器
elements.forEach(function(element) {
    var inputElement = document.getElementById(element.id);
    var hiddenElement = document.getElementById(element.hiddenId);

    if (inputElement && hiddenElement) {
        inputElement.addEventListener('input', function() {
            hiddenElement.value = inputElement.value;
        });
    }
});
// ======重新按鈕設定=========================================================================================
var resetButton = document.getElementById('resetButton');

resetButton.addEventListener('click', function() {
    var AgencyDepartmentIDElement = document.getElementById("AgencyDepartmentID");
    var AgencyDepartmentNameElement = document.getElementById("AgencyDepartmentName");
    var AgencyDepartmentAreaCodeElement = document.getElementById("AgencyDepartmentAreaCodeElement");
    var AgencyDepartmentAddressElement = document.getElementById("AgencyDepartmentAddress");
    var AgencyDepartmentTypedElement = document.getElementById("AgencyDepartmentTyped");
    var AgencyaffiliatedElement = document.getElementById("Agencyaffiliated");
    var AgencyDepartmentPhoneElement = document.getElementById("AgencyDepartmentPhone");
    var AgencyDepartmentFaxElement = document.getElementById("AgencyDepartmentFax");

    if (AgencyDepartmentIDElement) {AgencyDepartmentIDElement.value = '';}
    if (AgencyDepartmentNameElement) {AgencyDepartmentNameElement.value = '';}
    if (AgencyDepartmentAreaCodeElement) {AgencyDepartmentAreaCodeElement.value = '';}
    if (AgencyDepartmentAddressElement) {AgencyDepartmentAddressElement.value = '';}
    if (AgencyDepartmentTypedElement) {AgencyDepartmentTypedElement.value = '';}
    if (AgencyaffiliatedElement) {AgencyaffiliatedElement.value = '';}
    if (AgencyDepartmentPhoneElement) {AgencyDepartmentPhoneElement.value = '';}
    if (AgencyDepartmentFaxElement) {AgencyDepartmentFaxElement.value = '';}
});


$(document).ready(function() {
    $('#submitBtn').on('click', function(e) {
        e.preventDefault();
        var isValid = true;

        var fields = [
            { id: '#AgencyDepartmentID', error: '#AgencyDepartmentID_ErrorText' },
            { id: '#AgencyDepartmentName', error: '#AgencyDepartmentName_ErrorText' },
            { id: '#AgencyDepartmentTyped', error: '#AgencyDepartmentTyped_ErrorText' },
            { id: '#Agencyaffiliated', error: '#Agencyaffiliated_ErrorText' },
            { id: '#AgencyDepartmentPhone', error: '#AgencyDepartmentPhone_ErrorText' },
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

        var areaCode = $('#AgencyDepartmentAreaCode').val().trim();
        var address = $('#AgencyDepartmentAddress').val().trim();

        if (areaCode === '' || address === '') {
            $('#AgencyDepartmentAreaCode').addClass('is-invalid');
            $('#AgencyDepartmentAddress').addClass('is-invalid');
            $('#AgencyDepartmentAddress_ErrorText').removeClass('d-none');
            isValid = false;
        } else {
            $('#AgencyDepartmentAreaCode').removeClass('is-invalid');
            $('#AgencyDepartmentAddress').removeClass('is-invalid');
            $('#AgencyDepartmentAddress_ErrorText').addClass('d-none');
        }

        if (isValid) {
            $('#SaveModal').modal('show');
        }
    });

    $('#AgencyDepartmentAreaCode, #AgencyDepartmentAddress').on('input', function() {
        var areaCode = $('#AgencyDepartmentAreaCode').val().trim();
        var address = $('#AgencyDepartmentAddress').val().trim();

        if (areaCode !== '' && address !== '') {
            $('#AgencyDepartmentAreaCode').removeClass('is-invalid');
            $('#AgencyDepartmentAddress').removeClass('is-invalid');
            $('#AgencyDepartmentAddress_ErrorText').addClass('d-none');
        }
    });

    var fields = [
        '#AgencyDepartmentID',
        '#AgencyDepartmentName',
        '#AgencyDepartmentTyped',
        '#Agencyaffiliated',
        '#AgencyDepartmentPhone'
    ];

    fields.forEach(function(field) {
        $(field).on('input', function() {
            if ($(field).val().trim() !== '') {
                $(field).removeClass('is-invalid');
                $(field + '_ErrorText').addClass('d-none');
            }
        });
    });

    $('#resetButton').on('click', function() {
        $('input.form-control').val('').removeClass('is-invalid');
        $('small.error-text').addClass('d-none');
    });
});

