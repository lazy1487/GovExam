function openNewWindow(itemValue) {
    // 新視窗的網址
    var url = "/backFastLinkImageShow?Title=" + encodeURIComponent(itemValue);
    
    // 設定新視窗的寬度和高度
    var width = 1500;
    var height = 800;
    
    // 計算螢幕的寬度和高度
    var screenWidth = window.screen.width;
    var screenHeight = window.screen.height;
    
    // 計算新視窗的左上角位置，使其位於螢幕正中間
    var left = (screenWidth - width) / 2;
    var top = (screenHeight - height) / 2;
    
    // 開啟新視窗，設定寬度、高度、位置，以及不顯示導覽按鈕
    var newWindow = window.open(url, "_blank", `width=${width},height=${height},top=${top},left=${left},toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no,copyhistory=no`);
    
    // 等待新視窗加載完成後在新視窗中加入下載按鈕
    newWindow.onload = function() {
        var downloadButton = document.createElement('a');
        downloadButton.setAttribute('download', '');
        newWindow.document.body.appendChild(downloadButton);
    };
}