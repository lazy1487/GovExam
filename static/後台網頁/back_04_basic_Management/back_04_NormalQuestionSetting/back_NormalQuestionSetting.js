document.addEventListener("DOMContentLoaded", function() {
    var normalQuestionTitle= document.querySelector('input[name="normalQuestionTitle"]');
    var hiddennormalQuestionTitle= document.querySelector('input[name="hiddennormalQuestionTitle"]');
    hiddennormalQuestionTitle.value = normalQuestionTitle.value;
    normalQuestionTitle.addEventListener('input', function() {
        hiddennormalQuestionTitle.value = normalQuestionTitle.value;
    });
});