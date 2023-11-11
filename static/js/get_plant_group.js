document.addEventListener('DOMContentLoaded', (event) => {
    const pageSelector = document.getElementById('groupPageSelector');

    pageSelector.addEventListener('change', function() {
      window.location.href = '?page=' + this.value;
    });
});