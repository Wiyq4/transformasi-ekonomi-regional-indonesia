# Transformasi Ekonomi-Spasial Indonesia: Analisis Historiskturnya, dan **bagaimana** orang lain bisa menggunakan atau mereplikasi pekerjaan Anda.

Berikut adalah draf lengkap `README.md` yang bisa Anda salin dan tempel langsung ke repositori Anda.
---
```markdown
# Transformasi Ekonomi-Spasial Indonesia: Analisis Historis dan Klasterisasi Regional

Selamat datang di repositori resmi dan Klasterisasi Regional

Selamat datang di repositori resmi untuk penelitian berjudul **"Transformasi Ekonomi-Spasial Indonesia: Analisis Historis dan Klasterisasi Regional dengan Studi Kasus Komparatif di Jawa dan Kalimantan"**.

Repositori ini berisi seluruh dataset dan kode sumber Python yang digunakan untuk menganalisis bagaimana struktur ekonomi regional modern di Indonesia merupakan manifestasi dari lintasan pembangunan historis yang dimulai sejak era 1970-an.

[**Baca Naskah Jurnal Lengkap di untuk penelitian berjudul **"Transformasi Ekonomi-Spasial Indonesia: Analisis Historis dan Klasterisasi Regional dengan Studi Kasus Komparatif di Jawa dan Kalimantan"**. Repositori ini berisi seluruh dataset dan kode sumber yang digunakan untuk menghasilkan temuan dalam penelitian tersebut.

## 📝 Deskripsi Proyek

Penelitian ini bertujuan untuk menganalisis bagaimana struktur ekonomi regional modern di Indonesia merupakan manifestasi dari lintasan pembangunan historis (*path dependency*) yang dimulai sejak era 1970- Sini**](#) <!-- Ganti tanda # dengan link ke file PDF jurnal Anda jika ada -->

## Struktur Repositori

Proyek ini disusun ke dalam beberapa modul analisis yang mandiri untuk kejelasan dan kemudahan replikasi. Setiap modul berisi data dan skripnya masing-masing.

-   `📁 analisis-historis/`
    -   Beran. Analisis ini mengintegrasikan data historis (PDB, demografi) dengan analisis daya saing modern menggunakan indeks **Net Revealed Comparative Advantage (NRCA)** dan algoritma klasterisasi **K-Means**.

Studi kasus komparatif pada **Kota Surabaya** dan **Kabupaten Hulu Sungai Utara** digunakan untuk memperdalam analisis dan mengungkap divergensi lintasan pembangunan antara pusat industri/jasa dengan daerah berbasis sumber daya alam.

## 📂 Struktur Reposisi data dan skrip yang digunakan untuk menganalisis fondasi ekonomi-demografi Indonesia pada era formatif (1970-1980an).
    -   `📄 analisis_pdb.py`: Skrip utama untuk analisis deskriptif data PDB historis.
    -   `/data/`: Folder berisi dataset `produk_domestik_bruto.csv`, `penduduk_1971.csv`, dan `rupiah_exchangeitori

Proyek ini disusun ke dalam beberapa modul analisis yang mandiri untuk kejelasan dan kemudahan replikasi:

-   `./analisis-historis/`
    -   Berisi data dan skrip yang digunakan untuk menganalisis fondasi ekonomi-demografi Indonesia pada era formatif (1970-1980an).
    -   `data/`: Berisi dataset PDB historis, data penduduk 1971, dan data kurs valas.
    -   `*.py`: Skrip Python untuk analisis deskriptif data historis.

-.csv`.

-   `📁 analisis-regional-modern/`
    -   Berisi data dan skrip untuk analisis keunggulan komparatif (NRCA) dan klasterisasi fungsional pada periode modern (2009-2014).
    -   `📄 pdrb_analysis.py`: Skrip utama untuk perhitungan NRCA, klasterisasi K-Means, dan pembuatan visualisasi.
    -   `/data/`: Folder berisi dataset `PDRB_2009-2014.csv` dan `dataset_analisis.csv   `./analisis-regional-modern/`
    -   Berisi data dan skrip untuk analisis keunggulan komparatif (NRCA) dan klasterisasi fungsional pada periode 2009-2014.
    -   `data/`: Berisi dataset PDRB modern.
    -   `pdrb_analysis.py`: Skrip utama untuk perhitungan NRCA, klasterisasi K-Means, dan pembuatan visualisasi terkait.

## 🛠️ Metodologi Utama

Metodologi inti yang diimplementasikan dalam kode adalah sebagai`.

-   `📄 README.md`
    -   Dokumen ini, yang menjelaskan keseluruhan proyek.

## Metodologi Inti

Metodologi utama yang diimplementasikan dalam kode adalah sebagai berikut:

1.  **Analisis Historis**: Menggunakan statistik deskriptif pada data PDB 1983-1986 untuk mengidentifikasi struktur dan tren pertumbuhan ekonomi pada masa lalu.
2.  **Analisis Keunggulan Komparatif**: Menghitung indeks **Net Revealed Comparative Advantage (NRCA)** dari data PDRB 2009-2014 untuk mengukur daya saing relatif setiap sektor ekonomi.
3.  **Klasterisasi F berikut:

1.  **Analisis Historis**: Menggunakan statistik deskriptif untuk mengidentifikasi struktur dan pertumbuhan ekonomi pada era formatif.
2.  **Analisis Keunggulan Komparatif**: Menghitung indeks **Net Revealed Comparative Advantage (NRCA)** dari data PDRB 2009-2014.
3.  **Klasterisasi Fungsional**: Menerapkan algoritma **K-Means (K=2)** pada nilai NRCA untuk mengelompokkan setiap observasi ke dalam klaster "Komparatif" atau "Tidak Komparatif".
4.  **Evaluasi Model**: Kualitas klaster dievaluasi menggunakan **Silhouette Score** dan **Davies-Bungsional**: Menerapkan algoritma **K-Means (K=2)** pada nilai NRCA untuk mengelompokkan setiap observasi (sektor per tahun) ke dalam klaster "Komparatif" atau "Tidak Komparatif".
4.  **Evaluasi Model**: Kualitas klaster dievaluasi menggunakan **Silhouette Score** dan **Davies-Bouldin Index** untuk memastikan validitas pengelompokan.

## Prasyarat dan Instalasi

Untuk menjalankan analisis ini di lingkungan lokal, pastikan Anda telah menginstal:

-   Python 3.8 atau versi yang lebih baru.
-   Pustaka-pustaka berikut: `pandas`, `matplotlib`, `seaborn`, `scouldin Index**.

## 🚀 Cara Menggunakan

Untuk mereplikasi analisis ini, ikuti langkah-langkah berikut:

### 1. Prasyarat
-   Python 3.8 atau versi lebih baru.
-   Pustaka Python: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`.

### 2. Instalasi
Clone repositori ini ke mesin lokal Anda:
```bash
git clone https://github.com/Wiyq4/transformasi-ekonomi-regional-indonesia.git
cd transformasi-ekonomi-regional-indonesia
