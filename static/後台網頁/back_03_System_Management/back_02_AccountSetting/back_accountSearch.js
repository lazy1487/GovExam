document.getElementById('allClose').addEventListener('click', function() {
    // 取得所有的 input 元素
    var inputs = document.querySelectorAll('.input.form-control');
    // 逐一清除每個 input 元素的值
    inputs.forEach(function(input) {
        input.value = '';
    });
});
