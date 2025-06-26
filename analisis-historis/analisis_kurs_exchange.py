import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

# Dataset
data = {
    "Tahun": [1975, 1976, 1977, 1978, 1979, 1980, 1981],
    "Dollar_Amerika": [415, 415, 415, 625, 625, 625, 625],
    "Deutsche_Mark": [165.02, 170.11, 170.23, 314.69, 329.37, 339.79, 311.01],
    "Dollar_Singapura": [190.84, 191.6, 191.6, 307.64, 311.99, 314.74, 312.1],
    "Dollar_Hongkong": [84.47, 83.29, 83.29, 126.88, 126.99, 126.97, 120.55],
    "Yen_Jepang": [1.39, 1.44, 1.44, 2.8, 2.84, 2.86, 2.71],
    "Harga_Emas": [4430, 4430, 4430, 7550, 10595, 20550, 20895]
}
df = pd.DataFrame(data)

# Normalisasi
X = df.drop(columns=['Tahun'])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Clustering K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

# Evaluasi
inertia = kmeans.inertia_
silhouette = silhouette_score(X_scaled, labels)
db_index = davies_bouldin_score(X_scaled, labels)

# Tambahkan cluster ke dataframe
df['Cluster'] = labels

# Visualisasi dengan garis antar titik
plt.figure(figsize=(10, 6))
for i in range(len(df) - 1):
    plt.plot([df['Tahun'][i], df['Tahun'][i+1]],
             [df['Harga_Emas'][i], df['Harga_Emas'][i+1]],
             color='gray', linestyle='--', alpha=0.5)

scatter = plt.scatter(df['Tahun'], df['Harga_Emas'], c=df['Cluster'], cmap='viridis', s=100)

# Evaluasi ditampilkan di grafik
plt.text(1975.5, 18000,
         f'Inertia: {inertia:.2f}\nSilhouette Score: {silhouette:.2f}\nDavies-Bouldin Index: {db_index:.2f}',
         fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

plt.xlabel("Tahun")
plt.ylabel("Harga Emas")
plt.title("Clustering K-Means: Tahun vs Harga Emas + Evaluasi")
plt.grid(True)
plt.colorbar(scatter, label="Cluster")
plt.tight_layout()
plt.show()
