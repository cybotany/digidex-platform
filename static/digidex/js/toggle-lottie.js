document.addEventListener("DOMContentLoaded", function() {
  // Function to initialize Lottie animation for a single element
  function initLottieAnimation(element) {
    // Move 'data-src' value to 'src' and remove 'data-src'
    var animationPath = element.getAttribute('data-src');
    element.setAttribute('src', animationPath);
    element.removeAttribute('data-src');

    var loop = element.getAttribute('data-loop') === '1';
    var autoplay = element.getAttribute('data-autoplay') === '1';

    lottie.loadAnimation({
      container: element,
      renderer: 'svg',
      loop: loop,
      autoplay: autoplay,
      path: animationPath
    });
  }

  // Intersection Observer Callback
  function onIntersection(entries, observer) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        initLottieAnimation(entry.target);
        observer.unobserve(entry.target); // Stop observing the current target
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
