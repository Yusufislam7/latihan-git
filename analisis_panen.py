data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}
#print(data_panen)
#Panen_Jagung_lok2 = data_panen['lokasi2']['hasil_panen']['jagung']
#print(f"Hasil Panen Jagung lokasi 2: {Panen_Jagung_lok2}")
#Nama_Lokasi_3 = data_panen['lokasi3']['nama_lokasi']
#print(f"Ini Nama Lokasi 3: {Nama_Lokasi_3}")
# Data awal
# 1. Menampilkan seluruh data
print("Seluruh Data Panen:")
for lokasi, data in data_panen.items():
    nama_lokasi = data['nama_lokasi']
    hasil_panen = data['hasil_panen']
    print(f"{nama_lokasi}:")
    for komoditas, jumlah in hasil_panen.items():
        print(f"  {komoditas.capitalize()}: {jumlah}")
print("\n")

# 2. Menampilkan jumlah hasil panen jagung dari lokasi2
hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil panen jagung dari lokasi2: {hasil_jagung_lokasi2}")
print("\n")

# 3. Menampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}")
print("\n")

# 4. Menyimpan jumlah hasil panen padi dan kedelai setiap lokasi ke variabel terpisah
hasil_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
hasil_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}

print("Jumlah Hasil Panen Padi Setiap Lokasi:")
print(hasil_padi)
print("Jumlah Hasil Panen Kedelai Setiap Lokasi:")
print(hasil_kedelai)
print("\n")

# 5. Membuat percabangan untuk lokasi dengan perhatian khusus
print("Status Lokasi:")
for lokasi, data in data_panen.items():
    nama_lokasi = data['nama_lokasi']
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{nama_lokasi} memerlukan perhatian khusus.")
    else:
        print(f"{nama_lokasi} dalam kondisi baik.")

#6 asdadasd