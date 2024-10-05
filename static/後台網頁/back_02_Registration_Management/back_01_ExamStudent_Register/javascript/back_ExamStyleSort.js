var moveUpButton = document.getElementById('moveUpButton')
var moveDownButton = document.getElementById('moveDownButton')
var moveToTopButton = document.getElementById('moveToTopButton')
var moveToBottomButton = document.getElementById('moveToBottomButton')

// 上移按鈕功能
moveUpButton.addEventListener('click', function() {
    var selectedIndex = selectMenu.selectedIndex;
    if (selectedIndex > 0) {
        var selectedOption = selectMenu.options[selectedIndex];
        var previousOption = selectMenu.options[selectedIndex - 1];
        selectMenu.insertBefore(selectedOption, previousOption);
    }
});

// 下移按鈕功能
moveDownButton.addEventListener('click', function() {
    var selectedIndex = selectMenu.selectedIndex;
    if (selectedIndex < selectMenu.options.length - 1) {
        var selectedOption = selectMenu.options[selectedIndex];
        var nextOption = selectMenu.options[selectedIndex + 1];
        selectMenu.insertBefore(nextOption, selectedOption);
    }
});

// 置頂按鈕功能
moveToTopButton.addEventListener('click', function() {
    var selectedIndex = selectMenu.selectedIndex;
    if (selectedIndex > 0) {
        var selectedOption = selectMenu.options[selectedIndex];
        var firstOption = selectMenu.options[0];
        selectMenu.insertBefore(selectedOption, firstOption);
    }
});

// 置底按鈕功能
moveToBottomButton.addEventListener('click', function() {
    var selectedIndex = selectMenu.selectedIndex;
    var lastIndex = selectMenu.options.length - 1;
    if (selectedIndex < lastIndex) {
        var selectedOption = selectMenu.options[selectedIndex];
        var lastOption = selectMenu.options[lastIndex];
        selectMenu.appendChild(selectedOption);
        selectMenu.selectedIndex = lastIndex;
    }
});

function moveUp() {
    var selectedOption = $('#selectMenu option:selected');
    if (selectedOption.prev().length > 0) {
        selectedOption.insertBefore(selectedOption.prev());
        updateOptionValues();
    }
}

function moveDown() {
    var selectedOption = $('#selectMenu option:selected');
    if (selectedOption.next().length > 0) {
        selectedOption.insertAfter(selectedOption.next());
        updateOptionValues();
    }
}

function moveToTop() {
    var selectedOption = $('#selectMenu option:selected');
    selectedOption.prependTo('#selectMenu');
    updateOptionValues();
}

function moveToBottom() {
    var selectedOption = $('#selectMenu option:selected');
    selectedOption.appendTo('#selectMenu');
    updateOptionValues();
}

function updateOptionValues() {
    $('#selectMenu option').each(function(index) {
        $(this).val(index + 1); // 更新每個選項的值，這裡假設值是從1開始編號
    });
}
