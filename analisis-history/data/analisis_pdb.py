import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Memuat Dataset ---
try:
    df = pd.read_csv('produk_domestik_bruto.csv')
    print("Dataset 'produk_domestik_bruto.csv' berhasil dibaca.")
except FileNotFoundError:
    print("Error: File 'produk_domestik_bruto.csv' tidak ditemukan.")
    print("Pastikan file berada di direktori yang sama dengan script.")
    exit()

# --- 2. Pra-pemrosesan Data ---
print("\n--- Memulai Pra-pemrosesan Data ---")

# PERBAIKAN UTAMA UNTUK KeyError: 'No.'
# Jika kolom pertama di CSV Anda adalah 'No' (tanpa titik), maka ganti namanya menjadi 'No.'
# Jika kolom pertama di CSV Anda sudah 'No.' (dengan titik), Anda bisa hapus baris ini.
if 'No' in df.columns and 'No.' not in df.columns:
    df.rename(columns={'No': 'No.'}, inplace=True)
    print("Kolom 'No' diganti namanya menjadi 'No.'.")
elif 'No.' not in df.columns:
    print("Peringatan: Kolom 'No.' tidak ditemukan setelah pembacaan CSV. Periksa header file.")
    # Jika Anda yakin ada kolom No. tetapi ada karakter tersembunyi, coba ini:
    # df.columns = [col.strip() for col in df.columns]
    # if 'No.' not in df.columns:
    #     print("Peringatan: 'No.' masih belum ditemukan setelah stripping header.")

# Lanjutkan pra-pemrosesan seperti biasa
# Baris ini sekarang seharusnya bekerja karena kolom 'No.' sudah ada (atau diganti namanya)
df['No.'] = df['No.'].astype(str).str.replace('.', '', regex=False)
df.rename(columns={'Lapang usaha': 'Sektor'}, inplace=True)
df['Sektor'] = df['Sektor'].str.strip()


# Verifikasi nama sektor unik setelah pembersihan spasi
print("\n--- Semua Nama Sektor Unik Setelah Pembersihan Spasi ---")
print(df['Sektor'].unique())

# Perbaikan untuk numeric_cols: pastikan hanya kolom tahun yang teridentifikasi sebagai numerik
# Tambahkan filter untuk hanya menyertakan kolom yang berisi angka tahun dalam namanya
numeric_cols = [col for col in df.columns if 'harga' in col and '(' in col and ')' in col]


for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
print("Kolom-kolom numerik telah diubah tipenya menjadi float.")

print("\n--- Dataset Setelah Pra-pemrosesan ---")
print(df.head())
print("\n--- Info Dataset Setelah Pra-pemrosesan ---")
df.info()

# --- Pemeriksaan Data Sebelum Plotting ---
print("\n--- Pemeriksaan Data Sebelum Plotting ---")
print("Jumlah nilai NaN per kolom:\n", df.isnull().sum())
print("\nNilai unik kolom 'Sektor' setelah preprocessing:\n", df['Sektor'].unique())
print("\nContoh data PDB Total setelah preprocessing:")
print(df[df['Sektor'] == 'Produk Domestik Bruto'][['1983 (harga berlaku)', '1984 (harga berlaku)', '1985 (harga berlaku)', '1986 (harga berlaku)']])
print("\nContoh data Sektor Pertanian setelah preprocessing:")
print(df[df['Sektor'] == 'Pertanian, kehutanan, dan perikanan'][['1983 (harga berlaku)', '1984 (harga berlaku)', '1985 (harga berlaku)', '1986 (harga berlaku)']])


# --- 3. Eksplorasi Data ---
print("\n--- Memulai Eksplorasi Data ---")
print("\n--- Statistik Deskriptif (Harga Berlaku) ---")
# Gunakan list comprehension untuk memilih kolom harga berlaku secara dinamis
harga_berlaku_cols = [col for col in numeric_cols if '(harga berlaku)' in col]
print(df[harga_berlaku_cols].describe())

print("\n--- Statistik Deskriptif (Harga Konstan) ---")
# Gunakan list comprehension untuk memilih kolom harga konstan secara dinamis
harga_konstan_cols = [col for col in numeric_cols if '(harga konstan)' in col]
print(df[harga_konstan_cols].describe())


df['Pertumbuhan_PDB_Konstan_1983-1986'] = df['1986 (harga konstan)'] - df['1983 (harga konstan)']
df_sorted_growth = df.sort_values(by='Pertumbuhan_PDB_Konstan_1983-1986', ascending=False)

print("\n--- Sektor dengan Pertumbuhan PDB Konstan Tertinggi (1983-1986) ---")
# Filter keluar NaN dari hasil sort jika ada
print(df_sorted_growth[['Sektor', 'Pertumbuhan_PDB_Konstan_1983-1986']].dropna().head(5))

print("\n--- Sektor dengan Pertumbuhan PDB Konstan Terendah (1983-1986) ---")
# Filter keluar NaN dari hasil sort jika ada
print(df_sorted_growth[['Sektor', 'Pertumbuhan_PDB_Konstan_1983-1986']].dropna().tail(5))


# --- 4. Tampilkan Output Visual (matplotlib/seaborn) ---

# Visualisasi 1: PDB Berlaku dan Konstan Total per Tahun (Grafik Garis)
plt.figure(figsize=(12, 6))
pdb_total_row = df[df['Sektor'] == 'Produk Domestik Bruto']

if not pdb_total_row.empty:
    # Memastikan tahun-tahun diambil dari numeric_cols
    years_berlaku = [col.split(' ')[0] for col in harga_berlaku_cols] # Ambil '1983', '1984', dst.
    years_konstan = [col.split(' ')[0] for col in harga_konstan_cols]

    plt.plot(years_berlaku, pdb_total_row[harga_berlaku_cols].values.flatten(),
             marker='o', label='PDB Berlaku Total')
    plt.plot(years_konstan, pdb_total_row[harga_konstan_cols].values.flatten(),
             marker='x', linestyle='--', label='PDB Konstan Total')
    plt.title('Tren Produk Domestik Bruto Total (1983-1986)')
    plt.xlabel('Tahun')
    plt.ylabel('Nilai PDB (Milyar Rupiah)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("Peringatan: Baris 'Produk Domestik Bruto' tidak ditemukan untuk visualisasi PDB Total. Gambar tidak akan ditampilkan.")


# Visualisasi 2: Perbandingan PDB Berlaku vs Konstan untuk Sektor-sektor Utama (Grafik Garis)
sectors_to_plot = ['Pertanian, kehutanan, dan perikanan', 'Industri pengolahan', 'Perdagangan', 'Produk Domestik Bruto']

plt.figure(figsize=(15, 10))
for i, sector in enumerate(sectors_to_plot):
    sector_data = df[df['Sektor'] == sector]
    if not sector_data.empty:
        sector_data = sector_data.iloc[0]

        plt.subplot(2, 2, i + 1)
        years = ['1983', '1984', '1985', '1986'] # Asumsi tahun-tahun ini ada dan urut
        pdb_berlaku_values = [sector_data.get(f'{year} (harga berlaku)', float('nan')) for year in years]
        pdb_konstan_values = [sector_data.get(f'{year} (harga konstan)', float('nan')) for year in years]

        plt.plot(years, pdb_berlaku_values, marker='o', label='Harga Berlaku')
        plt.plot(years, pdb_konstan_values, marker='x', linestyle='--', label='Harga Konstan')
        plt.title(f'PDB Sektor: {sector}')
        plt.xlabel('Tahun')
        plt.ylabel('Nilai PDB (Milyar Rupiah)')
        plt.grid(True)
        plt.legend()
    else:
        print(f"Peringatan: Sektor '{sector}' tidak ditemukan untuk visualisasi perbandingan.")

plt.tight_layout()
plt.show()

# Visualisasi 3: Kontribusi PDB per Sektor (Harga Konstan) Tahun 1986 (Grafik Garis/Dot Plot)
pdb_1986_konstan = df[df['Sektor'] != 'Produk Domestik Bruto'][['Sektor', '1986 (harga konstan)']]
# Hanya sertakan baris yang tidak NaN untuk plotting
pdb_1986_konstan = pdb_1986_konstan.dropna(subset=['1986 (harga konstan)'])
pdb_1986_konstan_sorted = pdb_1986_konstan.sort_values(by='1986 (harga konstan)', ascending=True)

if not pdb_1986_konstan_sorted.empty:
    plt.figure(figsize=(12, 8))
    plt.plot(pdb_1986_konstan_sorted['1986 (harga konstan)'], pdb_1986_konstan_sorted['Sektor'],
             marker='o', linestyle='-', markersize=8, linewidth=1)
    plt.title('Kontribusi PDB per Sektor (Harga Konstan) Tahun 1986')
    plt.xlabel('Nilai PDB (Milyar Rupiah)')
    plt.ylabel('Sektor')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
else:
    print("Peringatan: Tidak ada data PDB Konstan 1986 yang valid untuk visualisasi kontribusi sektor.")


# Visualisasi 4: Pertumbuhan PDB Konstan Sektor (1983-1986) (Grafik Garis/Dot Plot)
plt.figure(figsize=(12, 8))
df_filtered_growth_plot = df_sorted_growth[df_sorted_growth['Sektor'] != 'Produk Domestik Bruto'].copy()
# Hanya sertakan baris yang tidak NaN untuk plotting
df_filtered_growth_plot = df_filtered_growth_plot.dropna(subset=['Pertumbuhan_PDB_Konstan_1983-1986'])
df_filtered_growth_plot = df_filtered_growth_plot.sort_values(by='Pertumbuhan_PDB_Konstan_1983-1986', ascending=True)

if not df_filtered_growth_plot.empty:
    plt.plot(df_filtered_growth_plot['Pertumbuhan_PDB_Konstan_1983-1986'], df_filtered_growth_plot['Sektor'],
             marker='o', linestyle='-', markersize=8, linewidth=1, color='purple')
    plt.title('Pertumbuhan PDB Konstan per Sektor (1983-1986)')
    plt.xlabel('Perubahan PDB (Milyar Rupiah)')
    plt.ylabel('Sektor')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
else:
    print("Peringatan: Tidak ada data pertumbuhan PDB Konstan yang valid untuk visualisasi pertumbuhan sektor.")


# --- 5. Evaluasi Pola Data ---
print("\n--- Analisis Pola Data ---")

print("\n--- Analisis Tren PDB Total ---")
pdb_total_row_eval = df[df['Sektor'] == 'Produk Domestik Bruto']

if not pdb_total_row_eval.empty:
    # Memastikan kolom yang digunakan untuk perhitungan tidak NaN
    total_pdb_berlaku_1983 = pdb_total_row_eval.get('1983 (harga berlaku)', float('nan')).values[0]
    total_pdb_berlaku_1986 = pdb_total_row_eval.get('1986 (harga berlaku)', float('nan')).values[0]
    total_pdb_konstan_1983 = pdb_total_row_eval.get('1983 (harga konstan)', float('nan')).values[0]
    total_pdb_konstan_1986 = pdb_total_row_eval.get('1986 (harga konstan)', float('nan')).values[0]

    if not pd.isna(total_pdb_berlaku_1983) and not pd.isna(total_pdb_berlaku_1986) and total_pdb_berlaku_1983 != 0:
        pertumbuhan_berlaku = ((total_pdb_berlaku_1986 - total_pdb_berlaku_1983) / total_pdb_berlaku_1983) * 100
        print(f"Pertumbuhan PDB Total (Harga Berlaku, 1983-1986): {pertumbuhan_berlaku:.2f}%")
    else:
        print("Data PDB Berlaku Total tidak lengkap untuk perhitungan pertumbuhan.")

    if not pd.isna(total_pdb_konstan_1983) and not pd.isna(total_pdb_konstan_1986) and total_pdb_konstan_1983 != 0:
        pertumbuhan_konstan = ((total_pdb_konstan_1986 - total_pdb_konstan_1983) / total_pdb_konstan_1983) * 100
        print(f"Pertumbuhan PDB Total (Harga Konstan, 1983-1986): {pertumbuhan_konstan:.2f}%")

        if pertumbuhan_berlaku > pertumbuhan_konstan: # Hanya bandingkan jika keduanya ada
            print("Indikasi: Terdapat pengaruh inflasi yang signifikan pada pertumbuhan PDB.")
        else:
            print("Indikasi: Pengaruh inflasi relatif kecil atau tidak signifikan pada pertumbuhan PDB.")
    else:
        print("Data PDB Konstan Total tidak lengkap untuk perhitungan pertumbuhan.")

else:
    print("Peringatan: Baris 'Produk Domestik Bruto' tidak ditemukan untuk analisis tren PDB Total.")


print("\n--- Sektor dengan Perubahan PDB Konstan yang Perlu Perhatian ---")
df_filtered_growth = df_sorted_growth[df_sorted_growth['Sektor'] != 'Produk Domestik Bruto']
df_filtered_growth = df_filtered_growth.dropna(subset=['Pertumbuhan_PDB_Konstan_1983-1986']) # Hapus NaN di kolom pertumbuhan

if not df_filtered_growth.empty:
    # Handle kasus jika hanya ada sedikit data setelah dropna (misal hanya 1 atau 2 data)
    if len(df_filtered_growth) >= 4: # Minimal 4 data untuk perhitungan kuartil 80% yang bermakna
        growth_threshold_high = df_filtered_growth['Pertumbuhan_PDB_Konstan_1983-1986'].quantile(0.8)
    else: # Jika data kurang, ambil nilai max sebagai threshold jika ingin identifikasi tertinggi
        growth_threshold_high = df_filtered_growth['Pertumbuhan_PDB_Konstan_1983-1986'].max()

    for index, row in df_filtered_growth.iterrows():
        if row['Pertumbuhan_PDB_Konstan_1983-1986'] < 0:
            print(f"Sektor '{row['Sektor']}' mengalami penurunan PDB konstan sebesar {row['Pertumbuhan_PDB_Konstan_1983-1986']:.2f} Milyar Rupiah.")
        elif row['Pertumbuhan_PDB_Konstan_1983-1986'] > growth_threshold_high:
            print(f"Sektor '{row['Sektor']}' mengalami pertumbuhan PDB konstan yang tinggi sebesar {row['Pertumbuhan_PDB_Konstan_1983-1986']:.2f} Milyar Rupiah.")
else:
    print("Tidak ada data sektor yang tersedia untuk analisis perubahan PDB konstan.")