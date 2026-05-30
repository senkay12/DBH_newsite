// Mobil menü aç/kapat
(function () {
  var t = document.getElementById('menuToggle'),
      n = document.getElementById('navlinks');
  if (t && n) {
    t.addEventListener('click', function () {
      var open = n.classList.toggle('open');
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
})();

// Açılır alt menüler (mobilde tıkla-aç; masaüstünde hover CSS ile)
(function () {
  var toggles = document.querySelectorAll('.sub-toggle');
  toggles.forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      // Sadece mobilde tıklama ile aç/kapat
      if (window.matchMedia('(max-width:680px)').matches) {
        e.preventDefault();
        var li = btn.closest('.has-sub');
        var open = li.classList.toggle('open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      }
    });
  });
})();

// Demo formu (backend bağlanacak)
(function () {
  var f = document.getElementById('contactForm'),
      ok = document.getElementById('formOk');
  if (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!f.checkValidity()) { f.reportValidity(); return; }
      if (ok) ok.style.display = 'block';
      var btn = f.querySelector('button[type=submit]');
      if (btn) btn.textContent = 'Gönderildi ✓';
      f.reset();
    });
  }
})();
