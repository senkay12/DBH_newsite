# DBHSOFT — Yeni Web Sitesi (Modern Redesign)

www.dbhsoft.com içeriği **birebir** korunarak, UI/UX günümüz modern/elegant
standartlarına taşınmış tek dosyalık statik site.

## Önizleme
```bash
cd newsite
python3 -m http.server 8000
# http://localhost:8000
```
Build adımı yok — saf HTML + gömülü CSS + minimal vanilla JS.

## Dosyalar
- `index.html` — ana sayfa: SGO MatriX, Saha Satış Programı, Mobil Sıcak Satış, Rota Optimizasyonu, B2B Mobil, **10 Modül**, **13 Özellik**, KOBİ, Müşterilerimiz, Blog & Haberler, İletişim
- `hakkimizda.html` — Kurumsal/Hakkımızda (gerçek tarihçe: 1997 kuruluş, 2005 yazılım, 2006 ETİ MSDS, 2011 Coca-Cola İçecek VOYAGE; misyon/vizyon/ekipler)
- `insan-kaynaklari.html` — İK / kariyer + açık pozisyonlar
- `kvkk.html` — KVKK aydınlatma metni + çerez politikası (şablon)
- `assets/css/style.css` — paylaşılan tasarım sistemi (tüm sayfalar)
- `assets/js/main.js` — paylaşılan JS (mobil menü + form)
- `assets/dbhsoft-logo-512.png` — yüklenen resmi DBHSOFT logosu (header/footer/favicon)
- `assets/favicon.png` — 64px favicon
- `assets/dbhsoft-logo.png` — orijinal yüksek çözünürlük (yedek)

## Tasarım sistemi
- **Renk:** Logodan türetilen marka paleti — mavi `#1d83e2` (birincil), amber `#f6a21e`, yeşil `#3aa636`; nötr lacivert/slate taban. Üç renk yalnızca vurgu (başlık gradyanı, ikonlar, aksan) olarak kullanıldı.
- **Tipografi:** Plus Jakarta Sans (kurumsal B2B SaaS önerisi).
- **Stil:** Flat / elegant, yumuşak gölge ve 12–18px köşe yarıçapı, 150–200ms geçişler.
- **Erişilebilirlik:** semantik HTML, focus-visible halkaları, `prefers-reduced-motion`, 44px+ dokunma hedefleri, kontrast AA.

## İçerik kaynağı (birebir — fictional metin YOK)
Gerçek rakamlar: 25+ yıl · 150+ müşteri · 18 ülke · 3 kıta · 2.500+ distribütör.
Gerçek iletişim: Armutalan Mah. Taşlıcalılar Cad. No: 12 Kat: 1 No: 3, Marmaris / Muğla ·
+90 252 417 55 58 · info@dbhsoft.com.

## Yapılacaklar (gerçek varlık geldiğinde)
1. `Müşterilerimiz` bölümündeki kategori kutularını **gerçek müşteri logolarıyla** değiştir (izinli görseller).
2. Demo formunu (`#contactForm`) gerçek backend/e-posta endpoint'ine bağla.
3. İsteğe bağlı: ayrı `Kurumsal` ve `İnsan Kaynakları` sayfaları (şu an iletişime yönlendiriyor).
4. İsteğe bağlı: İngilizce (`/en`) sürüm.
