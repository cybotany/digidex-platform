// get_plant_group.js
document.addEventListener('DOMContentLoaded', (event) => {
    const leftArrow = document.getElementById('leftArrow');
    const rightArrow = document.getElementById('rightArrow');

    leftArrow.addEventListener('click', function() {
        window.location.href = '?page=' + leftArrow.getAttribute('data-group-id');
    });
    rightArrow.addEventListener('click', function() {
        window.location.href = '?page=' + rightArrow.getAttribute('data-group-id');
    });
});
