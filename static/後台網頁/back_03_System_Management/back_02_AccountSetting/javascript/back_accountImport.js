document.getElementById('exportButton').addEventListener('click', function () {
    // 定義數據
    const data = [
        ["使用者名稱", "使用者密碼", "使用者電話","使用者電子郵件"]
    ];

    // 創建一個工作表
    const ws = XLSX.utils.aoa_to_sheet(data);

    // 創建一個工作簿
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, "Sheet1");

    // 將工作簿導出為Excel文件
    XLSX.writeFile(wb, "example.xlsx");
});

// 匯出Excel的功能
document.getElementById('exportButton').addEventListener('click', function () {
    const data = [
        ["使用者名稱", "使用者密碼", "使用者電話","使用者電子郵件"]
    ];

    const ws = XLSX.utils.aoa_to_sheet(data);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, "Sheet1");
    XLSX.writeFile(wb, "example.xlsx");
});

// 匯入Excel並顯示在網頁上，並暫存數據到localStorage
document.getElementById('inputFile').addEventListener('change', function (e) {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const data = new Uint8Array(e.target.result);
        const workbook = XLSX.read(data, { type: 'array' });

        // 假設只讀取第一個工作表
        const firstSheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[firstSheetName];

        // 解析成JSON數據
        const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

        // 定義正確的標題
        const correctHeaders = ["使用者名稱", "使用者密碼", "使用者電話", "使用者電子郵件"];

        // 檢查標題是否匹配
        const importedHeaders = jsonData[0];
        const isCorrect = correctHeaders.every((header, index) => header === importedHeaders[index]);

        if (!isCorrect) {
            const errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
            errorModal.show();
            document.getElementById('inputFile').value = "";
            return;
        }

        // 將數據暫存到localStorage
        localStorage.setItem('excelData', JSON.stringify(jsonData));

        // 動態生成表格
        generateTable(jsonData);

        // 顯示表格的td元素
        document.getElementById('tableTd').style.display = "table-cell";
        document.getElementById('searchTitle').style.display = "table-cell";
        document.getElementById('searchInput').style.display = "table-cell";
    };

    reader.readAsArrayBuffer(file);
});

// 頁面加載時檢查是否有暫存數據，若有則載入
window.onload = function () {
    const storedData = localStorage.getItem('excelData');
    if (storedData) {
        const jsonData = JSON.parse(storedData);
        generateTable(jsonData);
    }
};


// 動態生成表格的函數
function generateTable(jsonData) {
    // 動態生成表格頭
    const tableHeader = document.getElementById('tableHeader');
    tableHeader.innerHTML = "";
    jsonData[0].forEach(header => {
        const th = document.createElement('th');
        th.innerText = header;
        tableHeader.appendChild(th);
    });

    // 動態生成表格內容
    const tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = "";
    jsonData.slice(1).forEach(row => {
        const tr = document.createElement('tr');
        row.forEach(cell => {
            const td = document.createElement('td');
            td.innerText = cell;
            tr.appendChild(td);
        });
        tableBody.appendChild(tr);
    });

    // 設定滾動條 (這是可選的，通常滾動條會根據內容自動顯示)
    const tableContainer = document.getElementById('tableContainer');
    tableContainer.style.overflowY = "auto"; // 這樣可以確保滾動軸隨著表格生成自動顯示
}


// 清除表格的函數
function clearTable() {
    const tableHeader = document.getElementById('tableHeader');
    const tableBody = document.getElementById('tableBody');
    tableHeader.innerHTML = ""; // 清空表格頭
    tableBody.innerHTML = "";   // 清空表格內容
    // 清除localStorage中的暫存數據
    localStorage.removeItem('excelData');
    document.getElementById('inputFile').value = "";
    document.getElementById('tableTd').style.display = "none";
    document.getElementById('searchTitle').style.display = "none";
    document.getElementById('searchInput').style.display = "none";
    
}

// 綁定清除按鈕的點擊事件
document.getElementById('clearButton').addEventListener('click', clearTable);