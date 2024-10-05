function showSpinner() {
    // 隱藏登入按鈕
    document.querySelector('button[type="submit"]').style.display = 'none';
    
    // 顯示轉圈圈
    document.getElementById('loadingSpinner').style.display = 'block';
    
    // 提交表單
    document.getElementById('loginForm').submit();
}

document.addEventListener('DOMContentLoaded', function () {
    const title = document.getElementById('main-title');
    const carousel = document.getElementById('carouselExampleIndicators');

    carousel.addEventListener('slide.bs.carousel', function (event) {
        switch (event.to) {
            case 0:
                title.textContent = '考試報名資訊';
                break;
            case 1:
                title.textContent = '最新消息';
                break;
            case 2:
                title.textContent = '常見問題';
                break;
            case 3:
                title.textContent = '問題回饋';
                break;
            default:
                title.textContent = '政府考試管理平台';
        }
    });
});