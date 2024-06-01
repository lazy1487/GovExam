document.getElementById('clear').addEventListener('click', function() {
    // 取得所有的 input 元素
    var inputs = document.querySelectorAll('.form-control');
    // 逐一清除每個 input 元素的值
    inputs.forEach(function(input) {
        input.value = '';
    });
});

var saveButton = document.getElementById('exportData');
// 監聽按鈕的點擊事件
saveButton.addEventListener('click', function() {
    // 創建一個虛擬的URL
    var result_json = JSON.parse(result_json);
    var data = JSON.stringify(result_json);
    // 創建 CSV 文件的內容
    var csvContent = "data:text/csv;charset=utf-8,";
    data.forEach(function(row) {
        csvContent += row.join(",") + "\r\n";
    });

    // 創建虛擬的 Blob
    var blob = new Blob([csvContent], {type: 'text/csv'});

    // 創建一個 <a> 元素，設置其 href 屬性為虛擬的 URL，並且觸發點擊事件
    var link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = 'filename.csv'; // 下載的文件名
    document.body.appendChild(link);
    link.click();

     // 刪除創建的 <a> 元素
     document.body.removeChild(link);
});