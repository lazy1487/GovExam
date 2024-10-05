var moveUpButton = document.getElementById('moveUpButton')
var moveDownButton = document.getElementById('moveDownButton')
var moveToTopButton = document.getElementById('moveToTopButton')
var moveToBottomButton = document.getElementById('moveToBottomButton')

// 上移按钮功能
moveUpButton.addEventListener('click', function() {
    var selectedIndex = selectMenu.selectedIndex;
    if (selectedIndex > 0) {
        var selectedOption = selectMenu.options[selectedIndex];
        var previousOption = selectMenu.options[selectedIndex - 1];
        selectMenu.insertBefore(selectedOption, previousOption);
    }
});

// 下移按钮功能
moveDownButton.addEventListener('click', function() {
    var selectedIndex = selectMenu.selectedIndex;
    if (selectedIndex < selectMenu.options.length - 1) {
        var selectedOption = selectMenu.options[selectedIndex];
        var nextOption = selectMenu.options[selectedIndex + 1];
        selectMenu.insertBefore(nextOption, selectedOption);
    }
});

// 置顶按钮功能
moveToTopButton.addEventListener('click', function() {
    var selectedIndex = selectMenu.selectedIndex;
    if (selectedIndex > 0) {
        var selectedOption = selectMenu.options[selectedIndex];
        var firstOption = selectMenu.options[0];
        selectMenu.insertBefore(selectedOption, firstOption);
    }
});

// 置底按钮功能
moveToBottomButton.addEventListener('click', function() {
    var selectedIndex = selectMenu.selectedIndex;
    var lastIndex = selectMenu.options.length - 1;
    if (selectedIndex < lastIndex) {
        var selectedOption = selectMenu.options[selectedIndex];
        var lastOption = selectMenu.options[lastIndex];
        selectMenu.appendChild(selectedOption);
        selectMenu.selectedIndex = lastIndex; // 将置底的选项设为选中状态
    }
});

confirmSaveButton.addEventListener('click', function() {
    var data = [];
    for (var i = 0; i < selectMenu.options.length; i++) {
        data.push({
            title: selectMenu.options[i].text,
            sort: i + 1
        });
    }

    fetch('/update_sort', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        var saveResultModal = new bootstrap.Modal(document.getElementById('SaveResultModal'));
        var saveResultMessage = document.getElementById('saveResultMessage');

        if (data.status === 'success') {
            saveResultMessage.textContent = '資料已成功更新';
        } else {
            saveResultMessage.textContent = '資料更新失敗';
        }

        saveResultModal.show();
    })
    .catch(error => {
        console.error('Error:', error);
        var saveResultModal = new bootstrap.Modal(document.getElementById('SaveResultModal'));
        var saveResultMessage = document.getElementById('saveResultMessage');
        saveResultMessage.textContent = '資料更新失敗';
        saveResultModal.show();
    });
});