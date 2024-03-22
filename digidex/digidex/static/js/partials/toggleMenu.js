document.addEventListener('DOMContentLoaded', function () {
    // Select the menu button
    var menuButton = document.querySelector('.menu-button.w-nav-button');
    
    // Check if the menu button is present
    if (menuButton) {
        // Select the navigation menu
        var navMenu = document.querySelector('.nav-menu.w-nav-menu');

        // Add click event listener to the menu button
        menuButton.addEventListener('click', function () {
            // Toggle a class (e.g., 'show-menu') on the navigation menu to show/hide it
            navMenu.classList.toggle('show-menu');
        });
    }
});
