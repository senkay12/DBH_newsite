// Mobil menü
(function () {
  var t = document.getElementById('menuToggle'),
      n = document.getElementById('navlinks');
  if (t && n) {
    t.addEventListener('click', function () {
      var open = n.classList.toggle('open');
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    n.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') n.classList.remove('open');
    });
  }
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
