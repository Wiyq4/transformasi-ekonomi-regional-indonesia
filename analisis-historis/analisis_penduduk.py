from src.preprocessing import load_data, bersihkan_data
from src.eksplorasi import eksplorasi_data
from src.klastering import klaster_data

def main():
    print("==== ANALISIS DATA PENDUDUK INDONESIA 1971 ====\n")
    
    # Step 1: Load dan Preprocessing
    df = load_data("data/penduduk_1971.csv")
    df = bersihkan_data(df)
    
    # Step 2: Eksplorasi Data
    eksplorasi_data(df)

    # Step 3: Klastering dan Visualisasi
    klaster_data(df)

    print("\n==== ANALISIS SELESAI ====")

if __name__ == "__main__":
    main()
