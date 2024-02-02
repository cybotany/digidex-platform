document.addEventListener('DOMContentLoaded', function() {
    // Select all accordion headers
    var accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(function(header) {
        header.addEventListener('click', function() {
            // Toggle the corresponding accordion content
            var content = this.nextElementSibling; // Assuming content comes right after header
            if (content.style.display === 'none' || content.style.display === '') {
                content.style.display = 'block';
                this.querySelector('.icon-accordion').classList.add('rotate-icon'); // Rotate the icon if needed
            } else {
                content.style.display = 'none';
                this.querySelector('.icon-accordion').classList.remove('rotate-icon'); // Reset the icon rotation
            }
        });
    });
});

