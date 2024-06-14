# Perkenalan
Perkenalkan kami dari kelompok 'Asli Pekalongan' (5)
Anggota Kelompok: - Andi Muh Fachry (1710623111)
                  - Jauza Aqhna Kamila (1710623098)
                  - Juan Wody Romansa (1710623094)
                  - Muhammad Fathir Fairuzzi (1710623089)
                  - Muhammad Ferry Hidayat (1710623006)
                  - Nazwa Jelita Soleha (1710623112)
                 
# Seperti apa aplikasi ini?
    Ini adalah aplikasi berbasis web streamlit, yang menyajikan member dari sebuah toko. Web ini berisikan informasi berupa
    data pembelian pembeli, promo yang sedang berlangsung, dan jumlah point yang dapat ditukarkan.

## Fungsi Aplikasi ini
   - Pembeli tidak perlu datang ke kasir untuk mengecheck data pembelian, promo, dan point belanja mereka
   - Selain dengan media sosial kita juga bisa memanfaatkan aplikasi ini untuk menaruh beberapa promo
   - Membuat toko lebih inovatif dan modern

# Cara Menjalankan Dashboard Streamlit
    - Sebelumnya kami sudah menyiapkan google form untuk membantu pemilik toko membuat data CSV dari pembeli berisi Timestamp, 
    Email,Nama,Kode Member,Tanggal Belanja,Total Belanja,Total Point.
    - Saran: Akan lebih mudah apabila CSV terhubung langsung dengan aplikasi kasir khusus

## Persiapan Awal

1. **Persiapkan Environment atau Notebook:**

   - Pastikan Anda memiliki Python dan pip terinstal di komputer Anda.

2. **Instalasi Library:**

   - Buka terminal atau command prompt.
   - Jalankan perintah: `pip install streamlit`.
   - Jalankan perintah: `pip install pandas`.
   - Jalankan perintah: `pip install base64`.

3. **Download CSV:**
   - Pastikan CSV yang akan digunakan sudah tersedia
   - CSV berasal dari google docs yang terhubung oleh CSV untuk mengisi data pembeli

## Menjalankan Dashboard

1. **Buka Terminal atau Command Prompt:**

   - Buka terminal atau command prompt di komputer Anda.

2. **Navigasi ke Direktori Tempat File Dashboard Disimpan:**

   - Gunakan perintah `cd` untuk berpindah ke direktori dashboard dimana file dashboard.

3. **Jalankan Perintah Streamlit:**

   - Ketik perintah: `streamlit run dashboard.py`.

4. **Tunggu Proses Eksekusi:**

   - Setelah menjalankan perintah di atas, Streamlit akan memulai server lokal dan dashboard akan dapat diakses melalui browser.

5. **Akses Dashboard:**

   - Akan muncul tulisan di terminal berupa:
        Warning: to view this Streamlit app on a browser, run it with the following
        command:

        streamlit run /Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/poin.py

   - Copy "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/Streamlit_member/poin.py" dan jalankan di terminal yang
     Berada di PC kalian, Browser akan ottomatis terbuka

6. **Interaksi dengan Dashboard:**

   - Sekarang Anda dapat berinteraksi dengan visualisasi dan tampilan yang disediakan di dalam dashboard Streamlit.

7. **Menghentikan Server:**
   - Untuk menghentikan server Streamlit, kembali ke terminal atau command prompt dan tekan `Ctrl + C`.

### Catatan Penting:

- Jika ada dependensi tambahan atau package yang dibutuhkan oleh dashboard, pastikan untuk menginstalnya sebelum menjalankan dashboard.
