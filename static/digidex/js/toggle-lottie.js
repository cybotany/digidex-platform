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
