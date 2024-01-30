document.addEventListener("DOMContentLoaded", function() {
  var lottieElements = document.querySelectorAll('.lottie-animation-1-banner, .lottie-animation-2-banner, .lottie-animation-2-blur-banner');

  lottieElements.forEach(function(element) {
    var animationPath = element.getAttribute('data-src');
    var loop = element.getAttribute('data-loop') === '1';
    var autoplay = element.getAttribute('data-autoplay') === '1';

    var animation = lottie.loadAnimation({
      container: element,
      renderer: 'svg',
      loop: loop,
      autoplay: autoplay,
      path: animationPath
    });
  });
});