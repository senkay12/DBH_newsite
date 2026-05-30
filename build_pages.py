# -*- coding: utf-8 -*-
"""DBHSOFT çok-sayfa üretici — ortak header/footer + sayfa gövdeleri."""
import os, io

OUT = os.path.dirname(os.path.abspath(__file__))

FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;600;700&display=swap">'

def head(title, desc, canonical, extra=""):
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#000000">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/dbhsoft-logo-512.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONT}
<link rel="stylesheet" href="assets/css/style.css">{extra}
</head>
<body>
<div class="brand-line"></div>
"""

CARET = '<svg class="caret" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>'

def header(active="", sub=""):
    def cls(key): return ' class="active"' if active == key else ""
    def scls(key): return ' class="active"' if sub == key else ""
    return f"""
<header class="site-header">
  <nav class="nav wrap" aria-label="Ana menü">
    <a href="index.html" class="brand" aria-label="DBHSOFT ana sayfa">
      <img src="assets/dbhsoft-logo-512.png" alt="DBHSOFT logosu" width="34" height="34">
      <span>DBH<span class="tld">SOFT</span></span>
    </a>
    <ul class="nav-links" id="navlinks">
      <li><a href="index.html"{cls('anasayfa')}>Anasayfa</a></li>
      <li class="has-sub">
        <button class="sub-toggle" aria-haspopup="true" aria-expanded="false">Kurumsal {CARET}</button>
        <ul class="submenu">
          <li><a href="hakkimizda.html"{scls('hakkimizda')}>Hakkımızda</a></li>
          <li><a href="insan-kaynaklari.html"{scls('insan')}>İnsan Kaynakları</a></li>
        </ul>
      </li>
      <li class="has-sub">
        <button class="sub-toggle" aria-haspopup="true" aria-expanded="false">SGO MatriX {CARET}</button>
        <ul class="submenu">
          <li><a href="ozellikler.html"{scls('ozellikler')}>SGO MatriX Özellikleri</a></li>
          <li><a href="moduller.html"{scls('moduller')}>SGO MatriX Modüller</a></li>
          <li><a href="kobi.html"{scls('kobi')}>KOBİ'lere Özel</a></li>
        </ul>
      </li>
      <li><a href="musteriler.html"{cls('musteriler')}>Müşterilerimiz</a></li>
      <li><a href="iletisim.html"{cls('iletisim')}>İletişim</a></li>
    </ul>
    <div class="nav-cta">
      <a href="iletisim.html" class="btn btn-primary">Demo Talep Et</a>
      <button class="menu-toggle" id="menuToggle" aria-label="Menüyü aç/kapat" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </nav>
</header>
"""

FOOTER = """
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a href="index.html" class="brand"><img src="assets/dbhsoft-logo-512.png" alt="DBHSOFT logosu" width="34" height="34"> <span>DBH<span style="color:#7f8ca3">SOFT</span></span></a>
        <p>25 yılı aşkın tecrübeyle saha satış, dağıtım ve merchandising operasyonları için mobil kurumsal yazılım üreten teknoloji firması.</p>
        <div class="social">
          <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3V6h-3c-1.7 0-3 1.3-3 3v2H8v3h3v6h3v-6h2.5l.5-3H14V9.5c0-.3.2-.5.5-.5Z"/></svg></a>
          <a href="#" aria-label="X (Twitter)"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 3h3l-6.6 7.5L22 21h-5.6l-4.4-5.7L6.9 21H3.9l7-8L2.5 3H8l4 5.2L17.5 3Zm-1 16h1.6L7.6 4.7H5.9L16.5 19Z"/></svg></a>
          <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
          <a href="#" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.94 7.5a1.94 1.94 0 1 1 0-3.88 1.94 1.94 0 0 1 0 3.88ZM5.3 9h3.3v11H5.3V9Zm5.3 0h3.16v1.5h.05c.44-.83 1.5-1.7 3.1-1.7 3.3 0 3.9 2.17 3.9 5V20h-3.3v-4.9c0-1.17 0-2.67-1.63-2.67-1.63 0-1.88 1.27-1.88 2.58V20h-3.3V9Z"/></svg></a>
        </div>
      </div>
      <div>
        <h5>SGO MatriX</h5>
        <ul>
          <li><a href="ozellikler.html">SGO MatriX Özellikleri</a></li>
          <li><a href="moduller.html">SGO MatriX Modüller</a></li>
          <li><a href="kobi.html">KOBİ'lere Özel</a></li>
        </ul>
      </div>
      <div>
        <h5>Kurumsal</h5>
        <ul>
          <li><a href="hakkimizda.html">Hakkımızda</a></li>
          <li><a href="insan-kaynaklari.html">İnsan Kaynakları</a></li>
          <li><a href="musteriler.html">Müşterilerimiz</a></li>
          <li><a href="kvkk.html">KVKK &amp; Gizlilik</a></li>
        </ul>
      </div>
      <div>
        <h5>İletişim</h5>
        <ul>
          <li><a href="tel:+902524175558">+90 252 417 55 58</a></li>
          <li><a href="mailto:info@dbhsoft.com">info@dbhsoft.com</a></li>
          <li><a href="https://maps.google.com/?q=Marmaris+Muğla" target="_blank" rel="noopener">Marmaris / Muğla</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 DBHSOFT. Tüm hakları saklıdır.</div>
      <div>Marmaris · Muğla · Türkiye</div>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
"""

CK = '<span class="ck"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span>'

def page(fn, title, desc, active, sub, body, extra=""):
    html = head(title, desc, "https://www.dbhsoft.com/"+fn, extra) + header(active, sub) + "\n<main>\n" + body + "\n</main>\n" + FOOTER
    with io.open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fn, len(html), "bytes")

# ---------------- ÖZELLİKLER ----------------
feat = lambda ic, svg, h, p: '<article class="feature"><span class="ic '+ic+'">'+svg+'</span><h3>'+h+'</h3><p>'+p+'</p></article>'
S = {
 'bar':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19V5M4 19h16M8 16v-5M12 16V8M16 16v-7M20 16v-3"/></svg>',
 'barcode':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7v10M8 7v10M11 7v10M15 7v10M18 7v10M21 7v10"/></svg>',
 'truck':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h11v8H3zM14 10h4l3 3v2h-7z"/><circle cx="7" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/></svg>',
 'temp':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/><circle cx="12" cy="12" r="9"/></svg>',
 'box':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.7l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.7l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="m3.3 7 8.7 5 8.7-5M12 22V12"/></svg>',
 'phone':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="3"/><path d="M11 18h2"/></svg>',
 'net':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="7" r="3"/><circle cx="5" cy="18" r="2.5"/><circle cx="19" cy="18" r="2.5"/><path d="M12 10v3M12 13l-5 3M12 13l5 3"/></svg>',
 'dev':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg>',
 'route':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18 3 21V6l6-3 6 3 6-3v15l-6 3-6-3Z"/><path d="M9 3v15M15 6v15"/></svg>',
 'gps':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8Z"/><circle cx="12" cy="10" r="2.6"/></svg>',
 'clock':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-6.2-8.5"/><path d="M21 4v5h-5"/><path d="M12 7v5l3 2"/></svg>',
 'tag':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 9h.01M15 15h.01M16 8 8 16"/><path d="M3.6 9.4 9.4 3.6a2 2 0 0 1 2.8 0l8.2 8.2a2 2 0 0 1 0 2.8l-5.8 5.8a2 2 0 0 1-2.8 0L3.6 12.2a2 2 0 0 1 0-2.8Z"/></svg>',
 'card':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M7 15h4"/></svg>',
}
features13 = "".join([
 feat('blue',S['bar'],'Raporlama ve Analizler','Detaylı operasyonel raporlar ve analizlerle sahayı uçtan uca görünür kılar.'),
 feat('amber',S['barcode'],'Ekipman Barkod Verifikasyonu','Saha ekipmanlarının barkod ile doğrulanması ve takibi.'),
 feat('green',S['truck'],'Sipariş / Tahsilat','Sahada sipariş alımı ve tahsilat işlemlerinin tek akışta yönetimi.'),
 feat('blue',S['temp'],'Soğuk / Sıcak Satış','Ön satış ve kamyondan satış (van sales) senaryolarının tamamı.'),
 feat('amber',S['box'],'Stok Takibi','Araç ve depo stoklarının anlık takibi ve yönetimi.'),
 feat('green',S['phone'],'Mobil Ekran İzleme','Saha cihazlarının ve mobil ekranların merkezden izlenmesi.'),
 feat('blue',S['net'],'Merkez, Distribütör ve Bayi İlişkisi','Merkez–distribütör–bayi zincirinin tek platformda yönetimi.'),
 feat('amber',S['dev'],'Win.Mobile ve Android App','Windows Mobile ve Android cihazlarda çalışan saha uygulaması.'),
 feat('green',S['route'],'Rut Optimizasyonu','Coğrafi rota planlama ile ziyaret ve dağıtım verimliliği.'),
 feat('blue',S['gps'],'GPS Takip','Saha ekibinin konum ve hareketlerinin canlı GPS takibi.'),
 feat('amber',S['clock'],'Gerçek Zamanlı Çalışma','Veriler anlık akar; kararlar gecikmeden alınır.'),
 feat('green',S['tag'],'Gelişmiş İskonto ve Promosyon Modülü','Kural tabanlı, kademeli iskonto ve kampanya senaryoları.'),
 feat('blue',S['card'],'Uzaktan Temassız Tahsilat','Mobil ödeme ile uzaktan, temassız tahsilat imkânı.'),
])

ozellikler_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Anasayfa</a> · SGO MatriX · Özellikleri</div>
    <h1>Satış noktalarınızı <span class="grad">tek noktadan</span> yönetin.</h1>
    <p>SGO-MatriX, satış noktalarının ve satış organizasyonunun tek noktadan yönetilmesini sağlayan mobil satış dağıtım programıdır; gerçek zamanlı stratejik kararları destekler.</p>
  </div>
</section>

<section class="block" style="padding-top:48px">
  <div class="wrap">
    <div class="features">{features13}</div>
  </div>
</section>

<section class="block soft">
  <div class="wrap">
    <div class="kobi">
      <h2>Özellikleri sahanızda görün.</h2>
      <p>Sektörünüze uyarlanmış canlı bir demo ile SGO MatriX'in operasyonunuzu nasıl hızlandırdığını gösterelim.</p>
      <div class="cta-actions">
        <a href="iletisim.html" class="btn btn-primary">Demo Talep Et</a>
        <a href="moduller.html" class="btn btn-light">Modülleri Gör</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------- MODÜLLER ----------------
mod = lambda ic, svg, h, p: '<div class="module"><span class="ic '+ic+'">'+svg+'</span><div><h3>'+h+'</h3><p>'+p+'</p></div></div>'
M = {
 'check':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3 8-8"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
 'target':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="0.5" fill="currentColor"/></svg>',
 'report':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>',
 'cart':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1.6"/><circle cx="18" cy="21" r="1.6"/><path d="M3 4h2l2.4 12.4a2 2 0 0 0 2 1.6h8.2a2 2 0 0 0 2-1.6L21 8H6"/></svg>',
 'shield':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><path d="M12 3 4 6v6c0 5 3.4 7.7 8 9 4.6-1.3 8-4 8-9V6z"/></svg>',
 'swap':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h13l-3-3M20 17H7l3 3"/></svg>',
 'plug':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M5 12a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2M5 12a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2"/></svg>',
 'web':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="14" rx="2"/><path d="M2 9h20M7 14h5"/></svg>',
 'sap':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M5 12a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2M5 12a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2"/><circle cx="7.5" cy="8" r="1" fill="currentColor"/><circle cx="7.5" cy="16" r="1" fill="currentColor"/></svg>',
 'sms':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
}
modules10 = "".join([
 mod('blue',M['check'],'MatriX İş Onay','Çok kademeli iş akışı ve onay mekanizması ile saha taleplerini yönetin.'),
 mod('amber',M['target'],'MatriX Satış Temsilcisi Hedef Takibi','Temsilci bazında hedef tanımlayın, gerçekleşmeyi anlık izleyin.'),
 mod('green',M['report'],'MatriX Web Raporlama','Operasyonel verilerinizi web üzerinden detaylı rapor ve panellerle inceleyin.'),
 mod('blue',M['cart'],'B2B e-Ticaret','Bayilerinizin self-servis sipariş verebildiği mobil e-ticaret kanalı.'),
 mod('amber',M['shield'],'MatriX TADB Kontrol Entegrasyonu','TADB kontrol süreçlerini SGO MatriX ile entegre yönetin.'),
 mod('green',M['swap'],'MatriX Sipariş Aktarım Sistemi','Sahadan gelen siparişleri merkezi sistemlere otomatik aktarın.'),
 mod('blue',M['plug'],'MatriX Netsis Entegrasyonu','Netsis ERP ile çift yönlü, sertifikalı veri entegrasyonu.'),
 mod('amber',M['web'],'MatriX Web Sipariş','Web üzerinden sipariş girişi ve takibi için merkezi ekran.'),
 mod('green',M['sap'],'MatriX SAP Entegrasyonu','SAP ile gerçek zamanlı, güvenli ve sertifikalı entegrasyon.'),
 mod('blue',M['sms'],'MatriX SMS Web Servis','Otomatik SMS bildirim ve duyuruları için web servis altyapısı.'),
])

moduller_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Anasayfa</a> · SGO MatriX · Modüller</div>
    <h1>İhtiyacınıza göre <span class="grad">büyüyen</span> modüler yapı.</h1>
    <p>Müşterilerimizin iş süreçlerinden doğan ihtiyaçlar, sistemin gelişimini yönlendirir. İşte SGO MatriX modülleri.</p>
  </div>
</section>

<section class="block" style="padding-top:48px">
  <div class="wrap">
    <div class="modules">{modules10}</div>
  </div>
</section>

<section class="block soft">
  <div class="wrap product rev">
    <div class="copy">
      <span class="tag">Dağıtım Rutu Optimizasyonu — Harita Modülü</span>
      <h2>Daha kısa rota, daha az yakıt, daha çok ziyaret.</h2>
      <p>Harita tabanlı rut optimizasyonu modülü; dağıtım sıralamasını, sevkiyatı ve ziyaret rotalarını tek ekranda planlar. Doğru sıralama ile yaklaşık %25'e varan yakıt tasarrufu sağlanabilir.</p>
      <ul class="checklist">
        <li>{CK} Eş zamanlı çalışma ve dağıtım sıralaması</li>
        <li>{CK} Renk kodlu rotalar ve mesafe bilgisi</li>
        <li>{CK} Otomatik veya manuel sevkiyat planlama</li>
        <li>{CK} Mobil uygulama entegrasyonu</li>
      </ul>
    </div>
    <div class="product-art">
      <div class="inner">
        <span class="tag" style="color:#c9b6ff">~%25 yakıt tasarrufu</span>
        <h3 style="margin-top:12px">Akıllı rota planlama</h3>
        <p>Renk kodlu rotalar, mesafe optimizasyonu ve otomatik sıralama ile filo verimliliği artar.</p>
        <div class="chip-row"><span class="chip">Harita</span><span class="chip">Renk kodlu rota</span><span class="chip">Sevkiyat</span><span class="chip">Mesafe</span><span class="chip">Mobil</span></div>
      </div>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap product">
    <div class="copy">
      <span class="tag">B2B Mobil (e-Ticaret)</span>
      <h2>Bayinizle 7/24 dijital sipariş kanalı.</h2>
      <p>Müşteriye özel promosyonlar, farklı promosyon mekanikleri, satış temsilcisi mobil takibi, SMS bildirimleri, duyurular, eğitim ve bilgi paylaşımı — bayilerinizle aranızdaki tüm iletişimi tek platformda toplayan B2B mobil e-ticaret çözümü.</p>
      <ul class="checklist">
        <li>{CK} Müşteriye özel fiyat ve promosyonlar</li>
        <li>{CK} SMS bildirimleri ve duyurular</li>
        <li>{CK} Satış temsilcisi mobil takibi</li>
        <li>{CK} Eğitim ve bilgi paylaşımı</li>
      </ul>
    </div>
    <div class="product-art">
      <div class="inner">
        <span class="tag" style="color:#c9b6ff">Self-servis bayi portalı</span>
        <h3 style="margin-top:12px">Bayi siparişi cebinde</h3>
        <p>Bayiler kendi siparişini verir, kampanyaları görür, bildirimleri alır — saha yükü azalır.</p>
        <div class="chip-row"><span class="chip">Promosyon</span><span class="chip">SMS</span><span class="chip">Duyuru</span><span class="chip">Eğitim</span><span class="chip">Sipariş</span></div>
      </div>
    </div>
  </div>
</section>
"""

# ---------------- KOBİ ----------------
kobi_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Anasayfa</a> · SGO MatriX · KOBİ'lere Özel</div>
    <h1>KOBİ'ler için <span class="grad">ölçeğinize</span> uygun paketler.</h1>
    <p>Tanıtım filmimizi izleyin, işletmenize özel paketleri keşfedin ve hemen bir demo talep edin. Büyük ölçekli kurumsal gücü, KOBİ'nize uygun paketlerle sunuyoruz.</p>
    <div class="cta-actions"><a href="iletisim.html" class="btn btn-primary">Demo Talep Et</a></div>
  </div>
</section>

<section class="block" style="padding-top:48px">
  <div class="wrap">
    <div class="vals">
      <div class="val"><span class="ic blue">{S['truck']}</span><h3>Hızlı kurulum</h3><p>Sahaya hızlı çıkış için hazır modül seti ve kısa uyarlama süreci.</p></div>
      <div class="val"><span class="ic amber">{S['tag']}</span><h3>Uygun maliyet</h3><p>İhtiyacınız kadar modül, ölçeğinize uygun fiyatlandırma.</p></div>
      <div class="val"><span class="ic green">{S['clock']}</span><h3>Gerçek zamanlı</h3><p>Saha verisi anlık merkeze akar; KOBİ'nizde kurumsal görünürlük.</p></div>
    </div>
  </div>
</section>

<section class="block soft">
  <div class="wrap">
    <div class="sec-head left">
      <span class="tag">Pakette neler var?</span>
      <h2>Temel saha operasyonu, kutudan çıkar çıkmaz.</h2>
    </div>
    <ul class="checklist" style="max-width:680px">
      <li>{CK} Mobil saha satışı (ön satış &amp; sıcak satış)</li>
      <li>{CK} Sipariş, irsaliye ve tahsilat</li>
      <li>{CK} GPS ve rut takibi</li>
      <li>{CK} Gelişmiş iskonto ve promosyon</li>
      <li>{CK} Raporlama ve analizler</li>
      <li>{CK} ERP entegrasyonu (Netsis / Logo / SAP)</li>
    </ul>
    <div class="cta-actions"><a href="iletisim.html" class="btn btn-primary">Size Uygun Paketi Konuşalım</a></div>
  </div>
</section>
"""

# ---------------- MÜŞTERİLER ----------------
tiles = "".join(f'<div class="client-tile">{t}</div>' for t in
  ["FMCG","İçecek","Gıda","İlaç","Kozmetik","Dağıtım","Perakende","Tütün","Tarım","Lojistik","Endüstri","Distribütör"])
musteriler_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Anasayfa</a> · Müşterilerimiz</div>
    <h1>3 kıtada, 18 ülkede <span class="grad">sektör liderlerinin</span> tercihi.</h1>
    <p>Dünya çapındaki şirketler, kendilerini rekabetten ayırabilecek özel yazılımlar için bize başvuruyor. Hızlı tüketim, içecek, gıda, ilaç ve dağıtım sektörlerinin önde gelen markaları DBHSOFT altyapısını kullanıyor.</p>
  </div>
</section>

<section class="stats" aria-label="Şirket rakamları">
  <div class="wrap stats-grid">
    <div class="stat"><div class="num">25<em>+</em></div><div class="cap">Yıllık Tecrübe</div></div>
    <div class="stat"><div class="num">150<em>+</em></div><div class="cap">Hizmet Verilen Müşteri</div></div>
    <div class="stat"><div class="num">3</div><div class="cap">Kıta</div></div>
    <div class="stat"><div class="num">18</div><div class="cap">Ülke</div></div>
    <div class="stat"><div class="num">2.500<em>+</em></div><div class="cap">Distribütör</div></div>
    <div class="stat"><div class="num">25<em>+</em></div><div class="cap">Kullanıcı</div></div>
  </div>
</section>

<section class="block clients">
  <div class="wrap">
    <div class="sec-head"><span class="tag">Çalıştığımız Sektörler</span><h2>Geniş bir sektör yelpazesi.</h2></div>
    <div class="logos">{tiles}</div>
    <p class="note">Gerçek müşteri logoları, izinli görseller temin edildiğinde bu alana yerleştirilecektir.</p>
  </div>
</section>

<section class="block soft">
  <div class="wrap">
    <div class="sec-head"><span class="tag">Blog &amp; Haberler</span><h2>Ürün, hizmet ve teknolojiden haberler.</h2><p>Büyümenizi desteklemek için ürünlerimiz, hizmetlerimiz ve teknolojiye dair içerikler.</p></div>
    <div class="blog-grid">
      <article class="post"><div class="cover a"></div><div class="body"><span class="cat">Saha Satış</span><h3>Saha satışında dijitalleşmenin 5 somut faydası</h3><p>Mobil saha satış otomasyonunun verimlilik, hata oranı ve tahsilat üzerindeki etkileri.</p><span class="more">Devamını oku</span></div></article>
      <article class="post"><div class="cover b"></div><div class="body"><span class="cat">Rut Optimizasyonu</span><h3>Doğru rut planlamasıyla yakıt maliyetini düşürmek</h3><p>Renk kodlu rotalar ve akıllı sıralama ile dağıtım filonuzda tasarruf sağlayın.</p><span class="more">Devamını oku</span></div></article>
      <article class="post"><div class="cover c"></div><div class="body"><span class="cat">Entegrasyon</span><h3>ERP entegrasyonu: SAP ve Netsis ile sorunsuz akış</h3><p>Sahadan merkeze veri akışında entegrasyonun rolü ve dikkat edilmesi gerekenler.</p><span class="more">Devamını oku</span></div></article>
    </div>
    <p class="note">Blog yazıları yayınlandıkça bu alanda listelenecektir.</p>
  </div>
</section>
"""

# ---------------- İLETİŞİM ----------------
iletisim_body = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Anasayfa</a> · İletişim</div>
    <h1>Bizimle çalışmaya <span class="grad">hazır mısınız?</span></h1>
    <p>Saha probleminizi anlatın; sektörünüze uyarlanmış bir demo ile dönelim. 24 saat içinde yanıt veriyoruz.</p>
  </div>
</section>

<section class="block contact" style="padding-top:48px">
  <div class="wrap contact-grid">
    <div>
      <span class="tag">İletişim Bilgileri</span>
      <h2>Operasyonunuzu birlikte hızlandıralım.</h2>
      <div class="cinfo">
        <a href="https://maps.google.com/?q=Armutalan+Mah.+Taşlıcalılar+Cad.+No+12+Marmaris+Muğla" target="_blank" rel="noopener">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8Z"/><circle cx="12" cy="10" r="2.6"/></svg></span>
          <span><span class="l">Adres</span><span class="v">Armutalan Mah. Taşlıcalılar Cad. No: 12 Kat: 1 No: 3<br>Marmaris / MUĞLA</span></span>
        </a>
        <a href="tel:+902524175558">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.1-8.7A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.7a2 2 0 0 1-.4 2.1L8 9.6a16 16 0 0 0 6 6l1.1-1.1a2 2 0 0 1 2.1-.5c.9.3 1.8.5 2.7.6a2 2 0 0 1 1.7 2Z"/></svg></span>
          <span><span class="l">Telefon</span><span class="v">+90 252 417 55 58</span></span>
        </a>
        <a href="mailto:info@dbhsoft.com">
          <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span>
          <span><span class="l">E-posta</span><span class="v">info@dbhsoft.com</span></span>
        </a>
      </div>
    </div>

    <form class="cform" id="contactForm" novalidate>
      <h3>Demo Talep Formu</h3>
      <p class="sub">Bilgilerinizi bırakın, ekibimiz sizinle iletişime geçsin.</p>
      <div class="frow">
        <div class="field"><label for="ad">Ad Soyad</label><input id="ad" name="ad" type="text" autocomplete="name" required></div>
        <div class="field"><label for="firma">Şirket</label><input id="firma" name="firma" type="text" autocomplete="organization" required></div>
      </div>
      <div class="frow">
        <div class="field"><label for="eposta">Kurumsal E-posta</label><input id="eposta" name="eposta" type="email" autocomplete="email" required></div>
        <div class="field"><label for="tel">Telefon</label><input id="tel" name="tel" type="tel" autocomplete="tel"></div>
      </div>
      <div class="field">
        <label for="sektor">Sektör</label>
        <select id="sektor" name="sektor">
          <option value="">Seçiniz</option>
          <option>FMCG / Hızlı Tüketim</option>
          <option>İçecek</option>
          <option>Gıda</option>
          <option>İlaç &amp; Sağlık</option>
          <option>Dağıtım / Distribütör</option>
          <option>Diğer</option>
        </select>
      </div>
      <div class="field"><label for="mesaj">Mesajınız</label><textarea id="mesaj" name="mesaj" placeholder="Saha operasyonunuzla ilgili kısaca bilgi verin."></textarea></div>
      <label class="consent">
        <input type="checkbox" id="kvkk" required>
        <span><a href="kvkk.html" style="color:var(--violet);font-weight:600">KVKK Aydınlatma Metni</a>'ni okudum; iletişim bilgilerimin işlenmesine onay veriyorum.</span>
      </label>
      <button type="submit" class="btn btn-primary">Talebi Gönder</button>
      <div class="form-ok" id="formOk">Teşekkürler! Talebiniz alındı, 24 saat içinde dönüş yapacağız.</div>
    </form>
  </div>
</section>
"""

# ---------------- HAKKIMIZDA ----------------
hakkimizda_body = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Anasayfa</a> · Kurumsal · Hakkımızda</div>
    <h1>Sahanın 25 yıllık <span class="grad">teknoloji ortağı.</span></h1>
    <p>1997'den bu yana, sektörün kurallarını değiştirenler ve yenilikçiler için bir teknoloji ortağıyız. Dünya çapındaki şirketler, kendilerini rekabetten ayırabilecek özel yazılımlar için bize başvuruyor.</p>
  </div>
</section>

<section class="block" style="padding-top:48px">
  <div class="wrap">
    <div class="prose">
      <h2>Biz kimiz?</h2>
      <p><strong>1997 yılında kurulmuş olan firmamız, 2005 yılında yazılım geliştirme faaliyetlerine başlamıştır.</strong> Gelişen mobil dünyanın yazılım ihtiyaçlarını öngörmüş ve geliştirdiği farklı teknolojiler ile <strong>2006 yılında ETİ Pazarlama A.Ş. MSDS Projesi ile sektörde bir ilki gerçekleştirmiştir.</strong></p>
      <p><strong>2011 yılında FMCG sektörünün devi Coca-Cola İçecek VOYAGE projesi</strong> ile ticari hayatına çok önemli bir kilometre taşı daha ekleyen DBHSOFT; bugün ana ürünü <strong>SGO MatriX</strong> ile satış noktaları ile satış teşkilatını tek merkezden yönetmeyi sağlayan bir mobil satış dağıtım çözümü sunmaktadır.</p>
      <p>Bugün <strong>3 kıtada, 18 ülkede, 150'den fazla müşteriye</strong> ve <strong>2.500'ü aşkın distribütöre</strong> hizmet veriyoruz. Hızlı tüketim, içecek, gıda, ilaç ve dağıtım gibi farklı sektörlerin önde gelen markaları, saha operasyonlarını DBHSOFT altyapısı üzerinde yürütüyor.</p>
      <h2>Misyonumuz</h2>
      <p>Misyonumuz; talep edilen ürünleri ve birinci sınıf hizmeti sağlayarak, sınırlar ve mesafeler ne olursa olsun müşterilerimizin iş zorluklarını çözme koşullarını yaratmaktır.</p>
      <h2>Vizyonumuz</h2>
      <p>Uluslararası bir yazılım şirketi olarak; üst düzey geliştirme merkezleri geliştirmek, müşterilerimizin yenilikçi ürünlerini tanıtmak ve yetenekli beyinler için işler yaratmak.</p>
      <h2>Ekiplerimiz</h2>
      <p>Proje Yönetimi, Analiz &amp; Test, Yazılım Geliştirme, Sunucu &amp; Veritabanı Yönetimi ve Çözüm Merkezi ekiplerimizle; müşteri memnuniyeti odağında, kurumsal uygulama tecrübesi, gerçek zamanlı çalışma ve kullanım kolaylığı ilkeleriyle çalışırız.</p>
    </div>
  </div>
</section>

<section class="stats" aria-label="Şirket rakamları">
  <div class="wrap stats-grid">
    <div class="stat"><div class="num">25<em>+</em></div><div class="cap">Yıllık Tecrübe</div></div>
    <div class="stat"><div class="num">150<em>+</em></div><div class="cap">Hizmet Verilen Müşteri</div></div>
    <div class="stat"><div class="num">3</div><div class="cap">Kıta</div></div>
    <div class="stat"><div class="num">18</div><div class="cap">Ülke</div></div>
    <div class="stat"><div class="num">2.500<em>+</em></div><div class="cap">Distribütör</div></div>
    <div class="stat"><div class="num">25<em>+</em></div><div class="cap">Kullanıcı</div></div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="kobi">
      <h2>Bizimle çalışmaya hazır mısınız?</h2>
      <p>Saha operasyonunuzu birlikte değerlendirelim; size özel bir demo hazırlayalım.</p>
      <div class="cta-actions">
        <a href="iletisim.html" class="btn btn-primary">Demo Talep Et</a>
        <a href="insan-kaynaklari.html" class="btn btn-light">Kariyer Fırsatları</a>
      </div>
    </div>
  </div>
</section>
"""

# ---------------- İNSAN KAYNAKLARI ----------------
insan_body = f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Anasayfa</a> · Kurumsal · İnsan Kaynakları</div>
    <h1>Saha teknolojisinin geleceğini <span class="grad">birlikte kuralım.</span></h1>
    <p>25 yılı aşkın süredir, gerçek saha problemlerini çözen yazılımlar geliştiriyoruz. Ekibimize katılarak 18 ülkede kullanılan bir platformun gelişimine katkı sağlayabilirsiniz.</p>
  </div>
</section>

<section class="block" style="padding-top:48px">
  <div class="wrap">
    <span class="tag">Neden DBHSOFT?</span>
    <div class="vals" style="margin-top:22px">
      <div class="val"><span class="ic blue"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20"/></svg></span><h3>Global etki</h3><p>3 kıtada, 18 ülkede kullanılan bir ürünün parçası olun.</p></div>
      <div class="val"><span class="ic amber"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20v-6M6 20V10M18 20V4"/></svg></span><h3>Gelişim</h3><p>Modern teknolojiler, kurumsal entegrasyonlar ve sürekli öğrenme ortamı.</p></div>
      <div class="val"><span class="ic green"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span><h3>Güçlü ekip</h3><p>Deneyimli mühendisler ve saha uzmanlarıyla birlikte çalışın.</p></div>
    </div>
  </div>
</section>

<section class="block soft">
  <div class="wrap">
    <div class="sec-head left"><span class="tag">Açık Pozisyonlar</span><h2>Aradığımız yetenekler.</h2><p>Aşağıdaki alanlarda yetenekli ekip arkadaşları arıyoruz. Pozisyonunuzu görmeseniz bile özgeçmişinizi gönderebilirsiniz.</p></div>
    <div class="jobs">
      <div class="job"><div><div class="jt">Backend Yazılım Geliştirici</div><div class="jm">Kurumsal saha satış platformu</div></div><div class="spacer"></div><div class="tags"><span class="jtag">.NET / Java</span><span class="jtag">SQL</span><span class="jtag">Marmaris / Uzaktan</span></div></div>
      <div class="job"><div><div class="jt">Mobil Uygulama Geliştirici</div><div class="jm">SGO MatriX mobil istemcisi</div></div><div class="spacer"></div><div class="tags"><span class="jtag">Android / Kotlin</span><span class="jtag">Offline-first</span></div></div>
      <div class="job"><div><div class="jt">ERP Entegrasyon Danışmanı</div><div class="jm">SAP &amp; Netsis entegrasyonları</div></div><div class="spacer"></div><div class="tags"><span class="jtag">SAP</span><span class="jtag">Netsis</span><span class="jtag">Entegrasyon</span></div></div>
      <div class="job"><div><div class="jt">Saha Destek &amp; Uygulama Uzmanı</div><div class="jm">Müşteri kurulum ve eğitim</div></div><div class="spacer"></div><div class="tags"><span class="jtag">Müşteri ilişkileri</span><span class="jtag">Seyahat</span></div></div>
    </div>
    <div style="margin-top:40px; display:flex; gap:14px; flex-wrap:wrap; align-items:center">
      <a href="mailto:info@dbhsoft.com?subject=Kariyer Başvurusu" class="btn btn-primary">Özgeçmiş Gönder</a>
      <span style="color:var(--stardust); font-size:15px">Başvurularınızı <a href="mailto:info@dbhsoft.com" style="color:var(--violet); font-weight:600">info@dbhsoft.com</a> adresine iletebilirsiniz.</span>
    </div>
  </div>
</section>
"""

# ---------------- KVKK ----------------
kvkk_body = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Anasayfa</a> · KVKK &amp; Gizlilik</div>
    <h1>KVKK Aydınlatma Metni</h1>
    <p>6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında, kişisel verilerinizin işlenmesine ilişkin bilgilendirme.</p>
  </div>
</section>

<section class="block" style="padding-top:40px">
  <div class="wrap">
    <div class="prose">
      <h2>1. Veri Sorumlusu</h2>
      <p>Kişisel verileriniz, veri sorumlusu sıfatıyla <strong>DBHSOFT</strong> tarafından, aşağıda açıklanan kapsamda işlenebilecektir. İletişim: Armutalan Mah. Taşlıcalılar Cad. No: 12 Kat: 1 No: 3, Marmaris / Muğla · info@dbhsoft.com · +90 252 417 55 58.</p>
      <h2>2. İşlenen Veriler ve Amaçları</h2>
      <p>Web sitemizdeki iletişim/demo formu aracılığıyla paylaştığınız ad-soyad, şirket, e-posta, telefon ve mesaj içeriği gibi kişisel verileriniz; talebinizin değerlendirilmesi, sizinle iletişim kurulması, demo ve teklif süreçlerinin yürütülmesi amaçlarıyla işlenir.</p>
      <h2>3. Hukuki Sebep</h2>
      <p>Kişisel verileriniz, KVKK md. 5 kapsamında açık rızanıza ve bir sözleşmenin kurulması veya ifasıyla doğrudan ilgili olması hukuki sebeplerine dayanılarak işlenmektedir.</p>
      <h2>4. Verilerin Aktarılması</h2>
      <p>Kişisel verileriniz, yalnızca yukarıdaki amaçların gerçekleştirilmesi için gerekli olduğu ölçüde ve mevzuata uygun şekilde yetkili kişi, kurum ve kuruluşlarla paylaşılabilir.</p>
      <h2>5. Haklarınız (KVKK md. 11)</h2>
      <ul>
        <li>Kişisel verilerinizin işlenip işlenmediğini öğrenme,</li>
        <li>İşlenmişse buna ilişkin bilgi talep etme,</li>
        <li>İşlenme amacını ve amaca uygun kullanılıp kullanılmadığını öğrenme,</li>
        <li>Eksik veya yanlış işlenmiş verilerin düzeltilmesini isteme,</li>
        <li>Silinmesini veya yok edilmesini isteme,</li>
        <li>İşlemenin kanuna aykırı olması hâlinde zararın giderilmesini talep etme.</li>
      </ul>
      <p>Taleplerinizi <strong>info@dbhsoft.com</strong> adresine iletebilirsiniz.</p>
      <h2>6. Çerez (Cookie) Politikası</h2>
      <p>Web sitemiz, deneyiminizi kişiselleştirmek ve siteyi geliştirmek amacıyla çerezler kullanır. Tarayıcı ayarlarınızdan çerez tercihlerinizi her zaman değiştirebilirsiniz. Siteyi kullanmaya devam ederek çerez kullanımını kabul etmiş sayılırsınız.</p>
      <p style="margin-top:32px; font-size:14px; color:var(--ghost)">Not: Bu metin genel bir bilgilendirme şablonudur. Yayına almadan önce kurumsal hukuk biriminiz tarafından gözden geçirilmesi önerilir.</p>
    </div>
  </div>
</section>
"""

# ---------------- WRITE ALL ----------------
page("ozellikler.html", "SGO MatriX Özellikleri — DBHSOFT",
     "SGO MatriX özellikleri: raporlama, GPS takip, sipariş/tahsilat, soğuk-sıcak satış, stok takibi, iskonto ve promosyon ve daha fazlası.",
     "sgo", "ozellikler", ozellikler_body)
page("moduller.html", "SGO MatriX Modüller — DBHSOFT",
     "SGO MatriX modülleri: İş Onay, Hedef Takibi, Web Raporlama, B2B e-Ticaret, SAP ve Netsis entegrasyonu, rota optimizasyonu ve daha fazlası.",
     "sgo", "moduller", moduller_body)
page("kobi.html", "KOBİ'lere Özel Paketler — DBHSOFT",
     "KOBİ'ler için ölçeğinize uygun saha satış ve dağıtım paketleri. Hızlı kurulum, uygun maliyet, gerçek zamanlı görünürlük.",
     "sgo", "kobi", kobi_body)
page("musteriler.html", "Müşterilerimiz — DBHSOFT",
     "3 kıtada, 18 ülkede 150+ müşteri. Hızlı tüketim, içecek, gıda, ilaç ve dağıtım sektörlerinin önde gelen markalarının tercihi.",
     "musteriler", "", musteriler_body)
page("iletisim.html", "İletişim — DBHSOFT",
     "DBHSOFT ile iletişime geçin. Marmaris / Muğla · +90 252 417 55 58 · info@dbhsoft.com. Demo talep formu.",
     "iletisim", "", iletisim_body)
page("hakkimizda.html", "Hakkımızda — DBHSOFT",
     "DBHSOFT 1997'de kuruldu, 2005'te yazılım geliştirmeye başladı. 2006 ETİ MSDS, 2011 Coca-Cola İçecek VOYAGE. Misyon, vizyon ve ekipler.",
     "kurumsal", "hakkimizda", hakkimizda_body)
page("insan-kaynaklari.html", "İnsan Kaynakları — DBHSOFT",
     "DBHSOFT'ta kariyer. Saha teknolojilerinin geleceğini birlikte kuralım. Açık pozisyonlar ve başvuru bilgileri.",
     "kurumsal", "insan", insan_body)
page("kvkk.html", "KVKK & Gizlilik — DBHSOFT",
     "DBHSOFT KVKK aydınlatma metni, kişisel verilerin korunması ve çerez politikası.",
     "", "", kvkk_body, extra='\n<meta name="robots" content="noindex">')

print("OK - all pages generated")
