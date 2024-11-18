import requests
from bs4 import BeautifulSoup

# Daftar URL situs proxy gratis
proxy_sites = [
    'https://www.sslproxies.org/',
    'https://free-proxy-list.net/',
    'https://www.us-proxy.org/',
    'https://www.proxy-list.download/HTTPS',
    'https://www.proxy-list.download/HTTP',
    'https://www.socks-proxy.net/',
    'https://hidemy.name/en/proxy-list/?type=hs',
    'https://www.proxynova.com/proxy-server-list/',
    'https://www.spys.one/en/https-ssl-proxy/',
    'https://geonode.com/free-proxy-list/'
]

# Fungsi untuk scrape proxy dari halaman HTML
def scrape_proxies(url):
    proxies = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Cari tabel atau elemen HTML yang berisi data proxy
        for row in soup.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) >= 6:
                ip = cols[0].text.strip()
                port = cols[1].text.strip()
                https_support = cols[6].text.strip().lower() == 'yes'  # Hanya ambil proxy yang mendukung HTTPS
                
                # Uptime dan Latency bisa diambil dari atribut lain jika tersedia
                # Tangani error parsing dengan pengecekan dan ignore jika gagal parsing
                try:
                    uptime = int(cols[7].text.strip('%')) if len(cols) > 7 else 0  # Ambil uptime dari kolom (jika ada)
                except ValueError:
                    uptime = 0  # Jika tidak bisa diparsing, set ke 0
                
                try:
                    latency = float(cols[5].text.strip()) if len(cols) > 5 and cols[5].text.strip().isdigit() else 1000  # Hanya angka yang valid
                except ValueError:
                    latency = 1000  # Jika tidak bisa diparsing, set default latency tinggi
                
                # Filter hanya proxy yang mendukung HTTPS, uptime lebih dari 90%, dan latency di bawah 300ms
                if https_support and uptime >= 90 and latency <= 300:
                    proxies.append(f'{ip}:{port}')
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    return proxies

# Menyimpan proxy ke file
def save_proxies_to_file(proxies, filename='proxy.txt'):
    with open(filename, 'w') as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")

if __name__ == "__main__":
    all_proxies = []
    for site in proxy_sites:
        print(f"Scraping proxies from: {site}")
        proxies = scrape_proxies(site)
        all_proxies.extend(proxies)

    # Simpan semua proxy terbaik ke proxy.txt
    save_proxies_to_file(all_proxies)
    print(f"Saved {len(all_proxies)} best proxies to proxy.txt")
