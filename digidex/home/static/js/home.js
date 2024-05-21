document.addEventListener('DOMContentLoaded', function () {
    // Select the menu button
    var menuButton = document.querySelector('.menu-button.base-nav-button');
    
    // Check if the menu button is present
    if (menuButton) {
        // Select the navigation menu
        var navMenu = document.querySelector('.nav-menu.base-nav-menu');

        // Add click event listener to the menu button
        menuButton.addEventListener('click', function () {
            // Toggle a class (e.g., 'show-menu') on the navigation menu to show/hide it
            navMenu.classList.toggle('show-menu');
        });
    }
});

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

document.addEventListener("DOMContentLoaded", function() {
  // Function to animate lines
  function animateLines(startDelay = 0) {
    setTimeout(() => {
      document.querySelectorAll('.line-w').forEach(line => line.style.height = '100%');
      document.querySelectorAll('.line-h').forEach(line => line.style.width = '100%');
    }, startDelay);
  }

  // Initialize Lottie animation with custom settings
  function initLottieAnimation(element, startDelay = 0) {
    var animationPath = element.getAttribute('data-src');
    var loop = element.getAttribute('data-loop') === '1';
    var autoplay = element.getAttribute('data-autoplay') === '1';

    // Load the animation with a delay if specified
    setTimeout(() => {
      lottie.loadAnimation({
        container: element,
        renderer: 'svg',
        loop: loop,
        autoplay: autoplay,
        path: animationPath
      });
    }, startDelay);
  }

  // Intersection Observer Callback
  function onIntersection(entries, observer) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (entry.target.classList.contains('lottie-animation-1')) {
          // Start line animations slightly earlier than the Lottie animation
          animateLines(300);
          initLottieAnimation(entry.target);
        } else {
          // Start other Lottie animations with a delay
          initLottieAnimation(entry.target, 500);
        }
        observer.unobserve(entry.target);
      }
    });
  }

  // Set up the Intersection Observer
  var observer = new IntersectionObserver(onIntersection, {
    rootMargin: '0px',
    threshold: 0.1
  });

  // Observe all Lottie elements
  var lottieElements = document.querySelectorAll('.lottie-animation-1, .lottie-animation-2, .lottie-animation-2-blur');
  lottieElements.forEach(element => observer.observe(element));
});
