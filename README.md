# 🌐 Ağ Hız Testi Uygulaması

`speedtest-cli` mantığıyla çalışan, **customtkinter** ile geliştirilmiş modern ve koyu temalı bir masaüstü internet hız testi uygulaması.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

---

## 📸 Özellikler

- 🎨 **Modern koyu tema (Dark Mode)** arayüz
- ⬇️ **İndirme** ve ⬆️ **Yükleme** hızlarını büyük, okunaklı kartlarda gösterir (Mbps)
- 📶 **Ping (gecikme)** ve **sunucu/lokasyon** bilgisini gösterir
- 🔄 Test aşamalarını takip eden **dinamik durum etiketi** ve **ilerleme çubuğu**
- ⚡ Test sırasında arayüzün donmaması için **arka planda (thread) çalışan** ölçüm motoru
- 🛡️ İnternet bağlantısı olmadığında veya sunuculara erişilemediğinde **uygulamayı çökertmeyen** hata yönetimi

---

## 🛠️ Kullanılan Teknolojiler

| Kütüphane | Amaç |
|---|---|
| [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) | Modern grafik kullanıcı arayüzü (GUI) |
| [`speedtest-cli`](https://github.com/sivel/speedtest-cli) | İndirme/yükleme/ping ölçüm motoru |
| `threading` | GUI donmasın diye arka plan işlemleri (Python standart kütüphanesi) |

---

## 📦 Kurulum

### 1. Depoyu klonlayın (veya dosyayı indirin)

```bash
git clone https://github.com/Opus95/ag-hiz-testi.git
cd ag-hiz-testi
```

### 2. (Önerilir) Sanal ortam oluşturun

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Gerekli paketleri kurun

```bash
pip install -r requirements.txt
```

veya doğrudan:

```bash
pip install customtkinter speedtest-cli
```

> **Not:** PyPI'daki paket adı `speedtest-cli` olsa da, Python içinde `import speedtest` şeklinde kullanılır.

---

## ▶️ Çalıştırma

```bash
python ag_hiz_testi.py
```

Uygulama açıldığında **"TESTİ BAŞLAT"** butonuna tıklamanız yeterli. Uygulama sırasıyla:

1. En yakın/en hızlı sunucuyu bulur
2. Ping (gecikme) değerini ölçer
3. İndirme hızını test eder
4. Yükleme hızını test eder
5. Sonuçları Mbps cinsinden ekranda gösterir

---

## 📁 Proje Yapısı

```
ag-hiz-testi/
├── ag_hiz_testi.py     # Ana uygulama dosyası
├── requirements.txt    # Gerekli Python paketleri
└── README.md           # Bu dosya
```

---

## ❓ Sorun Giderme

**`ModuleNotFoundError: No module named 'customtkinter'`**
Kodu çalıştırdığınız Python ortamı ile paketi kurduğunuz ortam farklı olabilir. Şunu deneyin:

```bash
python -m pip install customtkinter speedtest-cli
```

**Test "İnternet bağlantınızı kontrol edin" hatası veriyor**
- İnternet bağlantınızı kontrol edin
- VPN/güvenlik duvarı `speedtest.net` sunucularına erişimi engelliyor olabilir
- Birkaç dakika sonra tekrar deneyin (sunucular geçici olarak yoğun olabilir)

---


---

