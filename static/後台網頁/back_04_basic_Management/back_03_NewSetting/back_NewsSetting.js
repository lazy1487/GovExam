document.addEventListener('DOMContentLoaded', (event) => {
    const clearButton = document.getElementById('allClose');

    // 添加点击事件监听器
    clearButton.addEventListener('click', () => {
        document.getElementById('inputSubTitle').value = '';
        document.getElementById('UploadTime').value = '';
        document.getElementById('RemoveTime').value = '';
    });
});