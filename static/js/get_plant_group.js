document.addEventListener('DOMContentLoaded', (event) => {
    const leftArrow = document.getElementById('leftArrow');
    const rightArrow = document.getElementById('rightArrow');
    const pageSelector = document.getElementById('groupPageSelector');

    pageSelector.addEventListener('change', function() {
      window.location.href = '?page=' + this.value;
    });
    leftArrow.addEventListener('click', function() {
      window.location.href = '?page=' + leftArrow.getAttribute('data-group-id');
    });
    rightArrow.addEventListener('click', function() {
      window.location.href = '?page=' + rightArrow.getAttribute('data-group-id');
    });
});