================================================================================
README.txt - KORPUS DOKUMEN TUGAS PEMROGRAMAN KELOMPOK
Mata Kuliah : Pengolahan Teks / Information Retrieval
Tugas       : Pemrograman Kelompok ke-2 (Sparse and Dense Word Vectors)
Topik       : TF-IDF, Pembobotan Term, Cosine Similarity
Tenggat     : Selasa, 25 Maret 2026 (setelah libur Lebaran) via eclass
================================================================================

NIM dan Nama Anggota Kelompok:
  1. [71230995] - [Alven Tendrawan]
  2. [71231058] - [Michael Chandra Mahanaim]

--------------------------------------------------------------------------------
DESKRIPSI KORPUS
--------------------------------------------------------------------------------

Korpus ini terdiri dari 10 dokumen berbahasa Indonesia dengan 2 topik utama:
  - Topik 1 : Ekonomi Indonesia (artikel_01 s.d. artikel_05)
  - Topik 2 : Teknologi Informasi & Kecerdasan Buatan / AI (artikel_06 s.d. artikel_10)

Semua artikel bersumber dari media dan institusi terpercaya, diterbitkan antara
Desember 2025 hingga Maret 2026.

--------------------------------------------------------------------------------
DAFTAR ARTIKEL DAN URL SUMBER
--------------------------------------------------------------------------------

[TOPIK 1: EKONOMI]

Artikel 01
  Judul   : Pemerintah Optimistis Pertumbuhan Ekonomi Indonesia 2026 Tembus 5,5 Persen Meski Ada Perang
  Sumber  : Suara.com
  Tanggal : 17 Maret 2026
  URL     : https://amp.suara.com/bisnis/2026/03/17/132000/pemerintah-optimistis-pertumbuhan-ekonomi-indonesia-2026-tembus-55-persen-meski-ada-perang
  File    : artikel_01.txt

Artikel 02
  Judul   : Ekonomi Indonesia Tumbuh Kuat di 2025, Pemerintah Targetkan 5,4-5,6% di 2026
  Sumber  : Kementerian Koordinator Bidang Perekonomian RI
  Tanggal : 2026
  URL     : https://www.ekon.go.id/publikasi/detail/6816/ekonomi-indonesia-tumbuh-kuat-di-2025-pemerintah-targetkan-54-56-di-2026-melalui-akselerasi-program-prioritas-dan-transformasi-tata-kelola
  File    : artikel_02.txt

Artikel 03
  Judul   : Pertumbuhan Ekonomi 2026 Stabil, Tapi Daya Dorong Melemah
  Sumber  : Universitas Muhammadiyah Yogyakarta (UMY)
  Tanggal : 31 Desember 2025
  URL     : https://www.umy.ac.id/pertumbuhan-ekonomi-2026-stabil-tapi-daya-dorong-melemah/
  File    : artikel_03.txt

Artikel 04
  Judul   : Pemerintah dan Bank Indonesia Perkuat Sinergi Menjaga Inflasi 2026
  Sumber  : Bank Indonesia
  Tanggal : 30 Januari 2026
  URL     : https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_282226.aspx
  File    : artikel_04.txt

Artikel 05
  Judul   : Investor Bersiap, Cek Sentimen Penting di Awal Maret 2026
  Sumber  : CNBC Indonesia
  Tanggal : 1 Maret 2026
  URL     : https://www.cnbcindonesia.com/research/20260301101339-128-714853/investor-bersiap-cek-sentimen-penting-di-awal-maret-2026
  File    : artikel_05.txt

[TOPIK 2: TEKNOLOGI INFORMASI & KECERDASAN BUATAN]

Artikel 06
  Judul   : 7 Inovasi Teknologi yang Diprediksi Mengubah Dunia di Tahun 2026
  Sumber  : School of Information Systems - BINUS University
  Tanggal : 19 Februari 2026
  URL     : https://sis.binus.ac.id/2026/02/19/7-inovasi-teknologi-yang-diprediksi-mengubah-dunia-di-tahun-2026/
  File    : artikel_06.txt

Artikel 07
  Judul   : Disrupsi AI Bikin Arah Bisnis 2026 Bukan Lagi soal Cepat, tapi Relevan
  Sumber  : Kompas.com
  Tanggal : 29 Januari 2026
  URL     : https://money.kompas.com/read/2026/01/30/070000026/disrupsi-ai-bikin-arah-bisnis-2026-bukan-lagi-soal-cepat-tapi-relevan
  File    : artikel_07.txt

Artikel 08
  Judul   : 6 Tren AI yang Diprediksi Akan Populer pada 2026, Bakal Secanggih Apa?
  Sumber  : Detik.com (detikEdu)
  Tanggal : Desember 2025
  URL     : https://www.detik.com/edu/detikpedia/d-8246803/6-tren-ai-yang-diprediksi-akan-populer-pada-2026-bakal-secanggih-apa
  File    : artikel_08.txt

Artikel 09
  Judul   : Prediksi Tren Industri 2026, AI dan Otomatisasi Jadi "Pemain Kunci"
  Sumber  : KompasTekno
  Tanggal : 24 Desember 2025
  URL     : https://tekno.kompas.com/read/2025/12/24/12080037/prediksi-tren-industri-2026-ai-dan-otomatisasi-jadi-pemain-kunci-
  File    : artikel_09.txt

Artikel 10
  Judul   : Reposisi Pasar AI dalam Ekonomi Berbiaya Tinggi 2026
  Sumber  : Kompas.com (Kolom)
  Tanggal : 6 Januari 2026
  URL     : https://money.kompas.com/read/2026/01/06/110350826/reposisi-pasar-ai-dalam-ekonomi-berbiaya-tinggi-2026
  File    : artikel_10.txt

--------------------------------------------------------------------------------
CARA MENJALANKAN PROGRAM
--------------------------------------------------------------------------------

Persyaratan:
  - Python 3.8 atau lebih baru
  - Library: nltk, sklearn, sastrawi (untuk stemming bahasa Indonesia)

Instalasi dependensi:
  pip install nltk scikit-learn PySastrawi

Download resource NLTK:
  import nltk
  nltk.download('stopwords')
  nltk.download('punkt')

Menjalankan program:
  python main.py

--------------------------------------------------------------------------------
CATATAN
--------------------------------------------------------------------------------

  - Dokumen menggunakan genre artikel berita dan opini berbahasa Indonesia
  - Stemming menggunakan Sastrawi (stemmer untuk Bahasa Indonesia)
  - Stopword menggunakan daftar stopword Bahasa Indonesia dari NLTK
  - Index TF-IDF disimpan dalam bentuk sparse matrix (sklearn) atau dictionary

================================================================================
