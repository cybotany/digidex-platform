document.addEventListener("DOMContentLoaded", function() {
  // Function to initialize Lottie animations
  function initLottieAnimations(selector) {
    var lottieElements = document.querySelectorAll(selector);

    lottieElements.forEach(function(element) {
      var animationPath = element.getAttribute('data-src');
      var loop = element.getAttribute('data-loop') === '1';
      var autoplay = element.getAttribute('data-autoplay') === '1';

      lottie.loadAnimation({
        container: element,
        renderer: 'svg',
        loop: loop,
        autoplay: autoplay,
        path: animationPath
      });
    });
  }

  // Initialize animations for the first set of elements
  initLottieAnimations('.lottie-animation-1, .lottie-animation-2, .lottie-animation-2-blur');

  // Initialize animations for the new banner elements
  initLottieAnimations('.lottie-animation-1-banner, .lottie-animation-2-banner, .lottie-animation-2-blur-banner');
});
