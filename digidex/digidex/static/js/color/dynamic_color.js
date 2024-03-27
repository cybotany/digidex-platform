document.addEventListener('DOMContentLoaded', function() {
    var colorBlock = document.getElementById('dynamicColorBlock');
    // Example: Fetching color values from somewhere, e.g., data attributes
    var bgColor = colorBlock.dataset.bgColor;
    var textColor = colorBlock.dataset.textColor;

    colorBlock.style.backgroundColor = bgColor;
    colorBlock.style.color = textColor;
});
