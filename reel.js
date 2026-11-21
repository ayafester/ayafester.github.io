// Шоурилы: картинки по очереди плавно сменяют друг друга, пока блок виден на экране.
// data-interval — скорость смены (мс). Если у картинки есть data-caption, он попадает в figcaption.
// При «уменьшить движение» — стоит первая картинка.
(function () {
  var reels = document.querySelectorAll('.reel');
  if (!reels.length) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  reels.forEach(function (reel, n) {
    var imgs = reel.querySelectorAll('img');
    var caption = reel.querySelector('figcaption');
    var every = parseInt(reel.getAttribute('data-interval'), 10) || 1600;
    imgs[0].classList.add('is-on');
    if (reduce || imgs.length < 2) return;
    var i = 0, timer = null;
    function step() {
      imgs[i].classList.remove('is-on');
      i = (i + 1) % imgs.length;
      imgs[i].classList.add('is-on');
      if (caption && imgs[i].dataset.caption) caption.textContent = imgs[i].dataset.caption;
    }
    function start() { if (!timer) timer = setInterval(step, every); }
    function stop() { clearInterval(timer); timer = null; }
    if (!('IntersectionObserver' in window)) { setTimeout(start, n * 250); return; }
    new IntersectionObserver(function (e) {
      e[0].isIntersecting ? setTimeout(start, (n % 3) * 250) : stop();
    }, { threshold: 0.3 }).observe(reel);
  });
})();
