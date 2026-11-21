// Прячем боковое меню, когда доскроллили до фото — чтобы не лежало поверх картинки
(function () {
  var menu = document.querySelector('.menu');
  var photo = document.querySelector('.photo');
  if (!('IntersectionObserver' in window) || !menu || !photo) return;
  new IntersectionObserver(function (entries) {
    menu.classList.toggle('menu--hidden', entries[0].isIntersecting);
  }, { threshold: 0.15 }).observe(photo);
})();
