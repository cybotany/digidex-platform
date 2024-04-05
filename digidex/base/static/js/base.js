document.addEventListener('DOMContentLoaded', function() {
    var observer = new IntersectionObserver(function(entries) {
        // Loop through the entries
        entries.forEach(entry => {
            // If the element is in the viewport
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1; // Change opacity to 1
                observer.unobserve(entry.target); // Optionally stop observing
            }
        });
    }, {
        threshold: 0.1 // Adjust according to when you want the transition to start
    });

    // Target the element within '.section-hero' to observe
    var heroContent = document.querySelector('.section-hero .content');
    observer.observe(heroContent);
});
