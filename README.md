# Proxy Scraper

Script ini digunakan untuk melakukan scraping proxy gratis dari beberapa situs penyedia proxy dan menyimpan hasil proxy terbaik ke dalam file `proxy.txt`.

## Fitur

- Mengambil proxy dari beberapa situs proxy gratis.
- Hanya menyimpan proxy yang mendukung HTTPS, memiliki uptime lebih dari 90%, dan latency di bawah 300ms.
- Menyimpan proxy yang di-scrape ke file `proxy.txt`.

## Prasyarat

Pastikan Anda telah menginstal pustaka berikut sebelum menjalankan script:
  - `requests`
  - `beautifulsoup4`

Anda bisa menginstalnya dengan perintah:
  ```bash
  pip install requests beautifulsoup4
  ```
## Cara Menggunakan
1. Clone repository atau salin script ini ke komputer Anda.
2. Jalankan script menggunakan Python:
 ``` bash
  python get.py
  ```
3. Proses scraping akan berjalan, dan proxy terbaik akan disimpan ke file proxy.txt di direktori yang sama dengan script.

## Struktur File
  - `get.py`: Script utama untuk scraping proxy.
  - `proxy.txt`: File yang berisi daftar proxy hasil scraping.

##Catatan
- Proxy yang diambil hanya yang mendukung HTTPS, memiliki uptime lebih dari 90%, dan latency di bawah 300ms.
- Proxy disimpan dalam format `IP:Port`

## Lisensi
Script ini bebas digunakan untuk tujuan pribadi.
```
README ini memberikan petunjuk dasar tentang apa yang dilakukan script, cara menginstal dependensi, dan bagaimana menjalankannya.
```


