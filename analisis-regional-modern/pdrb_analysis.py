# pdrb_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. Membaca data
df = pd.read_csv("PDRB_2009-2014.csv", quotechar='"', engine='python')

# 2. Preprocessing
print("Info Data:\n", df.info())
print("\nStatistik Deskriptif:\n", df.describe())
print("\nData Null:\n", df.isnull().sum())

# Drop baris/kolom yang tidak perlu jika ada
# Misal ada kolom nama daerah, pindahkan ke variabel terpisah
if 'Provinsi' in df.columns or 'Daerah' in df.columns:
    daerah_col = 'Provinsi' if 'Provinsi' in df.columns else 'Daerah'
    daerah = df[daerah_col]
    df_num = df.drop(columns=[daerah_col])
else:
    daerah = None
    df_num = df.copy()

# Standarisasi data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_num)

# 3. Eksplorasi Data
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_num)
plt.title("Boxplot Distribusi PDRB per Tahun")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("boxplot_pdrb.png")
plt.show()

# Korelasi antar tahun
plt.figure(figsize=(8, 6))
sns.heatmap(df_num.corr(), annot=True, cmap='coolwarm')
plt.title("Matriks Korelasi PDRB")
plt.tight_layout()
plt.savefig("korelasi_pdrb.png")
plt.show()

# 4. Klastering (KMeans)
# Cari jumlah klaster optimal dengan metode Elbow
sse = []
K_range = range(2, 10)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    sse.append(kmeans.inertia_)

# Plot Elbow
plt.figure(figsize=(8, 5))
plt.plot(K_range, sse, marker='o')
plt.title("Metode Elbow untuk Menentukan Jumlah Klaster")
plt.xlabel("Jumlah Klaster")
plt.ylabel("SSE")
plt.tight_layout()
plt.savefig("elbow_method.png")
plt.show()

# Pilih jumlah klaster optimal, misal 3
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
labels = kmeans.fit_predict(df_scaled)

# Tambahkan label ke DataFrame
df['Cluster'] = labels
if daerah is not None:
    df.insert(0, daerah_col, daerah)

print("\nContoh hasil klastering:")
print(df[[daerah_col, 'Cluster']] if daerah is not None else df[['Cluster']].head())

# 5. Evaluasi Model Klaster
sil_score = silhouette_score(df_scaled, labels)
print(f"\nSilhouette Score untuk {optimal_k} klaster: {sil_score:.3f}")

# 6. Visualisasi Klaster (jika dimensi bisa direduksi ke 2D)
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_pca[:, 0], y=df_pca[:, 1], hue=labels, palette='Set2')
plt.title("Visualisasi Klaster PDRB (PCA)")
plt.xlabel("Komponen Utama 1")
plt.ylabel("Komponen Utama 2")
plt.legend(title="Klaster")
plt.tight_layout()
plt.savefig("pca_clusters.png")
plt.show()
