document.addEventListener("DOMContentLoaded", function() {
    var inputExamStyle = document.querySelector('input[name="inputExamStyle"]');
    var hiddeninputExamStyle = document.querySelector('input[name="hiddeninputExamStyle"]');
    inputExamStyle.addEventListener('input', function() {
        hiddeninputExamStyle.value = inputExamStyle.value;
    });
});