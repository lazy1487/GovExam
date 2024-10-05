document.getElementById('exportButton').addEventListener('click', function () {
    // 定義數據
    const data = [
        ["姓名", "年齡", "性別"],
        ["張三", 30, "男"],
        ["李四", 28, "女"],
        ["王五", 35, "男"]
    ];

    // 創建一個工作表
    const ws = XLSX.utils.aoa_to_sheet(data);

    // 創建一個工作簿
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

    // 將工作簿導出為Excel文件
    XLSX.writeFile(wb, "example.xlsx");
});