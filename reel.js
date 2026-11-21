// Шоурил на карточках кейсов: картинки по очереди плавно сменяют друг друга,
// пока карточка видна на экране. При «уменьшить движение» — стоит первая картинка.
(function () {
  var reels = document.querySelectorAll('.reel');
  if (!reels.length) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  reels.forEach(function (reel, n) {
    var imgs = reel.querySelectorAll('img');
    imgs[0].classList.add('is-on');
    if (reduce || imgs.length < 2) return;
    var i = 0, timer = null;
    function step() {
      imgs[i].classList.remove('is-on');
      i = (i + 1) % imgs.length;
      imgs[i].classList.add('is-on');
    }
    function start() { if (!timer) timer = setInterval(step, 2200); }
    function stop() { clearInterval(timer); timer = null; }
    if (!('IntersectionObserver' in window)) { setTimeout(start, n * 300); return; }
    new IntersectionObserver(function (e) {
      e[0].isIntersecting ? setTimeout(start, (n % 3) * 400) : stop();
    }, { threshold: 0.3 }).observe(reel);
  });
})();
