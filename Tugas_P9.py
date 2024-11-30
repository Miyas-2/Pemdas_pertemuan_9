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

# Soal nomor 1
print("Soal nomor 1 \nTampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.\n")
for i, j in data_panen.items():
    print(f"Lokasi panen: {i}")
    print(f"Nama lokasi panen: {j['nama_lokasi']}")
    print(f"Hasil panen padi: {j['hasil_panen']['padi']}")
    print(f"Hasil panen jagung: {j['hasil_panen']['jagung']}")
    print(f"Hasil panen kedelai: {j['hasil_panen']['kedelai']}\n")

# soal nomor 2
print("Soal no 2 \nTampilkan jumlah hasil panen jagung dari lokasi2.\n")
jmlh_jagung_2 = data_panen['lokasi2']['hasil_panen']['jagung']

print(f"Jumlah hasil panen jagung di lokasi 2: {jmlh_jagung_2}\n")

# soal nomor 3
print("Soal no 3 \nTampilkan nama lokasi dari lokasi3.\n")
lokasi3 = data_panen['lokasi3']['nama_lokasi']

print(f"Nama lokasi panen lokasi 3: {lokasi3}\n")

# soal nomor 4 dan 5
print("Soal no 4 dan 5 \nMasukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda: ")
print("Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi.\n")
hasil_padi = []
hasil_kedelai = []

for i,j in data_panen.items():
    hasil_padi.append(j['hasil_panen']['padi'])
    hasil_kedelai.append(j['hasil_panen']['kedelai'])

print(hasil_padi)
print(hasil_kedelai)
print("\n")

# soal nomor 6
print("Soal no 6 \nBuat Percabangan \nJika jumlah hasil panen padi lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi, \nmaka lokasi tersebut memerlukan perhatian khusus. Jika tidak, maka lokasi tersebut dalam kondisi baik.\n")
for i,j in data_panen.items():
    if j['hasil_panen']['padi'] > 1300 or j['hasil_panen']['jagung'] > 800:
        print(f"Lokasi {j['nama_lokasi']} memerlukan perhatian khusus")
    else:
        print(f"Lokasi {j['nama_lokasi']} dalam kondisi baik")

# soal nomor 7
