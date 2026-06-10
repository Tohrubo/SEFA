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

Korpus ini terdiri dari 40 dokumen berbahasa Indonesia dengan 2 topik utama:
  - Topik 1 : Ekonomi Indonesia (artikel_01-05, artikel_11-15, artikel_21-30)
  - Topik 2 : Teknologi Informasi & Kecerdasan Buatan / AI (artikel_06-10,
              artikel_16-20, artikel_31-40)

Seluruh artikel berporos pada tema yang sama, yaitu prospek, proyeksi, dan tren
Indonesia menghadapi tahun 2026, dengan dua sudut pandang: Ekonomi dan Teknologi/AI.

Semua artikel bersumber dari media dan institusi terpercaya, diterbitkan antara
Oktober 2025 hingga Juni 2026.

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

[TOPIK 1: EKONOMI - TAMBAHAN]

Artikel 11
  Judul   : Proyeksi Ekonomi Indonesia 2026: Mengejar Ambisi 8 Persen
  Sumber  : SINDOnews (SINDOscope)
  Tanggal : 7 Januari 2026
  URL     : https://scope.sindonews.com/artikel/707/proyeksi-ekonomi-indonesia-2026-mengejar-ambisi-8
  File    : artikel_11.txt

Artikel 12
  Judul   : Kementerian Investasi Dorong Investasi Digital, Target 100 Ribu Lapangan Kerja Baru di 2026
  Sumber  : Republika Online
  Tanggal : 16 Oktober 2025
  URL     : https://ekonomi.republika.co.id/berita/t47mt0423/kementerian-investasi-dorong-investasi-digital-target-100-ribu-lapangan-kerja-baru-di-2026
  File    : artikel_12.txt

Artikel 13
  Judul   : APBN Triwulan I 2026 Solid, Ekonomi Indonesia Tetap Tumbuh di Tengah Tekanan Global
  Sumber  : InfoPublik
  Tanggal : 8 Mei 2026
  URL     : https://infopublik.id/kategori/nasional-ekonomi-bisnis/969399/index.html
  File    : artikel_13.txt

Artikel 14
  Judul   : Menilik Angka Pertumbuhan Ekonomi Indonesia 2026
  Sumber  : The Indonesian Institute (Center for Public Policy Research)
  Tanggal : 11 Mei 2026
  URL     : https://www.theindonesianinstitute.com/menilik-angka-pertumbuhan-ekonomi-indonesia-2026/
  File    : artikel_14.txt

Artikel 15
  Judul   : BI-Rate Tetap 4,75 Persen: Mendorong Pertumbuhan Ekonomi, Mempertahankan Stabilitas
  Sumber  : Bank Indonesia
  Tanggal : 19 Februari 2026
  URL     : https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_284326.aspx
  File    : artikel_15.txt

[TOPIK 2: TEKNOLOGI INFORMASI & KECERDASAN BUATAN - TAMBAHAN]

Artikel 16
  Judul   : Kecerdasan Buatan 2026: Indonesia Masih jadi Pasar atau Pencipta Solusi?
  Sumber  : Bisnis.com (Teknologi)
  Tanggal : 1 Januari 2026
  URL     : https://teknologi.bisnis.com/read/20260101/84/1940895/kecerdasan-buatan-2026-indonesia-masih-jadi-pasar-atau-pencipta-solusi
  File    : artikel_16.txt

Artikel 17
  Judul   : Indonesia Pimpin Adopsi Kecerdasan Buatan di Asia Tenggara
  Sumber  : youngster.id
  Tanggal : 25 Mei 2026
  URL     : https://youngster.id/headline/technology/indonesia-pimpin-adopsi-kecerdasan-buatan-di-asia-tenggara/
  File    : artikel_17.txt

Artikel 18
  Judul   : Revolusi AI di Indonesia: Dari Tren Menjadi Jantung Strategi Bisnis
  Sumber  : youngster.id
  Tanggal : 27 Maret 2026
  URL     : https://youngster.id/headline/features-headline/revolusi-ai-indonesia-dari-tren-menjadi-jantung-strategi-bisnis/
  File    : artikel_18.txt

Artikel 19
  Judul   : Bagaimana AI Membentuk Masa Depan Data Center di Tahun 2026
  Sumber  : Digital Edge Indonesia
  Tanggal : 30 Maret 2026
  URL     : https://id.digitaledgedc.com/id/infrastruktur-ai/bagaimana-ai-membentuk-masa-depan-data-center-di-tahun-2026
  File    : artikel_19.txt

Artikel 20
  Judul   : Proyeksi Perkembangan dan Tren Teknologi Tahun 2026
  Sumber  : PT Mitra Integrasi Informatika (MII)
  Tanggal : 12 Desember 2025
  URL     : https://www.mii.co.id/proyeksi-perkembangan-dan-tren-teknologi-tahun-2026-en
  File    : artikel_20.txt

[TOPIK 1: EKONOMI - TAMBAHAN KEDUA]

Artikel 21
  Judul   : Surplus Neraca Dagang RI Berlanjut Berkat Ekspor Industri Pengolahan
  Sumber  : Readers.id
  Tanggal : 1 April 2026
  URL     : https://www.readers.id/surplus-neraca-dagang-ekspor-industri
  File    : artikel_21.txt

Artikel 22
  Judul   : IHSG 2026 Diproyeksikan Tembus 9.400
  Sumber  : M-STOCK (Mirae Asset Sekuritas Indonesia)
  Tanggal : 22 Desember 2025
  URL     : https://mstock.miraeasset.co.id/blog/ihsg-2026/
  File    : artikel_22.txt

Artikel 23
  Judul   : Pariwisata Indonesia di Jalur Positif, Menteri Pariwisata Optimistis Capai Target
  Sumber  : Merdeka.com
  Tanggal : 6 Juni 2026
  URL     : https://www.merdeka.com/peristiwa/pariwisata-indonesia-di-jalur-positif-menteri-pariwisata-optimis-capai-target-2029-580283-mvk.html
  File    : artikel_23.txt

Artikel 24
  Judul   : Kemenperin Tegaskan PMI Kembali Ekspansi, Bukti Daya Tahan Industri
  Sumber  : ANTARA News
  Tanggal : 2 Juni 2026
  URL     : https://mataram.antaranews.com/berita/556468/kemenperin-menegaskan-pmi-kembali-ekspansi-bukti-daya-tahan-industri
  File    : artikel_24.txt

Artikel 25
  Judul   : Transisi Energi Nasional Ditegaskan di Forum IndoEBTKE 2026
  Sumber  : Info Nasional
  Tanggal : 14 Maret 2026
  URL     : https://www.infonasional.com/transisi-energi-nasional-indoebtke-2026
  File    : artikel_25.txt

Artikel 26
  Judul   : Pemerintah Alokasikan Rp58 Triliun untuk Program 3 Juta Rumah di Tahun 2026
  Sumber  : Kontan.co.id
  Tanggal : 12 Februari 2026
  URL     : https://nasional.kontan.co.id/news/pemerintah-alokasikan-rp-58-triliun-untuk-program-3-juta-rumah-di-tahun-2026
  File    : artikel_26.txt

Artikel 27
  Judul   : Pengangguran Indonesia Turun ke 4,68 Persen pada Februari 2026
  Sumber  : Gotrade
  Tanggal : 5 Mei 2026
  URL     : https://www.heygotrade.com/id/news/pengangguran-indonesia-turun-468-persen-februari-2026/
  File    : artikel_27.txt

Artikel 28
  Judul   : Transaksi E-Commerce Indonesia Capai Rp96,7 Triliun pada Februari 2026
  Sumber  : Readers.id
  Tanggal : 17 April 2026
  URL     : https://www.readers.id/transaksi-ecommerce-indonesia-februari-2026
  File    : artikel_28.txt

Artikel 29
  Judul   : QRIS Antarnegara Indonesia-Korea Selatan Resmi Diluncurkan
  Sumber  : Asatunews
  Tanggal : 6 April 2026
  URL     : https://www.asatunews.co.id/daftar-bank-dompet-digital-qris-korsel
  File    : artikel_29.txt

Artikel 30
  Judul   : Subsidi EV 2026 Jadi Momentum Bangun Industri Baterai NMC Nasional
  Sumber  : CNBC Indonesia
  Tanggal : 26 Mei 2026
  URL     : https://www.cnbcindonesia.com/news/20260526132001-4-738115/subsidi-ev-2026-jadi-momentum-bangun-industri-baterai-nmc-nasional
  File    : artikel_30.txt

[TOPIK 2: TEKNOLOGI INFORMASI & KECERDASAN BUATAN - TAMBAHAN KEDUA]

Artikel 31
  Judul   : Serangan Siber di RI Melonjak hingga 714 Persen, Awal 2026 Tembus 1,52 Miliar
  Sumber  : CNBC Indonesia
  Tanggal : 2 Juni 2026
  URL     : https://www.cnbcindonesia.com/tech/20260602203559-37-739562/serangan-siber-di-ri-menggila-melonjak-sampai-714-awal-2026-segini
  File    : artikel_31.txt

Artikel 32
  Judul   : Sudah Seluas Apa Cakupan 5G di Indonesia Awal 2026?
  Sumber  : IDN Times
  Tanggal : 27 Maret 2026
  URL     : https://www.idntimes.com/tech/trend/sudah-seluas-apa-cakupan-5g-di-indonesia-awal-2026-c1c2-01-b11wj-8l50jh
  File    : artikel_32.txt

Artikel 33
  Judul   : Contoh Penerapan AI dalam Layanan Kesehatan 2026
  Sumber  : Biznet Gio
  Tanggal : 15 Februari 2026
  URL     : https://www.biznetgio.com/blog/penerapan-ai-di-bidang-kesehatan/
  File    : artikel_33.txt

Artikel 34
  Judul   : Adopsi AI dan Cloud Meningkat, Kesiapan Infrastruktur Perusahaan Masih Jadi Tantangan
  Sumber  : RealEstat.id
  Tanggal : 4 Januari 2026
  URL     : https://www.realestat.id/berita-properti/adopsi-ai-dan-cloud-meningkat-kesiapan-infrastruktur-perusahaan-masih-jadi-tantangan/
  File    : artikel_34.txt

Artikel 35
  Judul   : Kekurangan Talenta Digital Jadi Tantangan Optimalisasi Ekonomi Digital Indonesia
  Sumber  : InfoPublik
  Tanggal : 16 Desember 2025
  URL     : https://infopublik.id/kategori/nasional-sosial-budaya/951946/kekurangan-talenta-digital-jadi-tantangan-optimalisasi-potensi-ekonomi-digital-indonesia
  File    : artikel_35.txt

Artikel 36
  Judul   : Pasar Robotika RI Diproyeksi Melesat, Adopsi AI Fisik Kian Luas
  Sumber  : JawaPos.com
  Tanggal : 10 Juni 2026
  URL     : https://www.jawapos.com/oto-dan-tekno/2606100146/pasar-robotika-ri-diproyeksi-melesat-adopsi-ai-fisik-kian-luas
  File    : artikel_36.txt

Artikel 37
  Judul   : Sahabat-AI: LLM Open-Source Buatan Indonesia untuk Kedaulatan Digital 2026
  Sumber  : Sultra Media
  Tanggal : 25 Februari 2026
  URL     : https://www.sultramedia.id/teknologi/mobile/sahabat-ai-large-language-model-open-source-buatan-indonesia-siap-mendukung-kedaulatan-digital-nasional-di-2026/
  File    : artikel_37.txt

Artikel 38
  Judul   : Funding Startup Indonesia 2026, Dari Era Euforia Menuju Era Seleksi Alam
  Sumber  : Majalah ICT
  Tanggal : 1 Juni 2026
  URL     : https://www.majalahict.com/funding-startup-indonesia-2026-dari-era-euforia-menuju-era-seleksi-alam/
  File    : artikel_38.txt

Artikel 39
  Judul   : Contoh Penerapan IoT pada Smart City dan Manfaatnya
  Sumber  : XL Smart for Business
  Tanggal : 30 Mei 2025
  URL     : https://www.xlsmart.co.id/bisnis/insights/article/contoh-penerapan-iot-pada-smart-city-dan-manfaatnya/
  File    : artikel_39.txt

Artikel 40
  Judul   : Hadirkan Kemudahan Layanan Publik Melalui Transformasi Digital Pemerintah
  Sumber  : Kementerian PANRB
  Tanggal : 26 September 2025
  URL     : https://www.menpan.go.id/site/berita-terkini/hadirkan-kemudahan-layanan-publik-melalui-transformasi-digital-pemerintah
  File    : artikel_40.txt

--------------------------------------------------------------------------------
CARA MENJALANKAN PROGRAM
--------------------------------------------------------------------------------

Persyaratan:
  - Python 3.8 atau lebih baru
  - Library: scikit-learn, pandas, numpy, nltk, PySastrawi
  - tkinter (sudah termasuk dalam Python standar, untuk versi GUI)

Instalasi dependensi:
  pip install scikit-learn pandas numpy nltk PySastrawi

Download resource NLTK:
  (otomatis diunduh saat program pertama dijalankan; perlu koneksi internet)
  import nltk
  nltk.download('stopwords')
  nltk.download('punkt')

Menjalankan program:
  python search_gui.py docs        # versi antarmuka grafis (GUI)
  python search_engine.py docs     # versi terminal / CLI

  Catatan: folder dokumen ("docs") WAJIB diberikan sebagai argumen.
  Versi GUI memiliki mode terang/gelap (tombol di kanan atas) dan
  panel prediksi kata yang dapat di-scroll horizontal.

--------------------------------------------------------------------------------
CATATAN
--------------------------------------------------------------------------------

  - Dokumen menggunakan genre artikel berita dan opini berbahasa Indonesia
  - Pre-processing: lowercase, hapus tanda baca, lalu tokenisasi (split spasi)
  - Pembobotan TF-IDF dihitung dengan TfidfVectorizer (scikit-learn)
  - Pencarian memakai Cosine Similarity antara vektor query dan dokumen
  - Tersedia prediksi kata berikutnya berbasis model N-gram (NLTK)
  - Daftar stopword Bahasa Indonesia dan stemmer Sastrawi tersedia di kode
    sebagai komponen opsional (belum diaktifkan pada pipeline pre-processing)
  - Index TF-IDF disimpan dalam bentuk sparse matrix (sklearn) atau dictionary

================================================================================
