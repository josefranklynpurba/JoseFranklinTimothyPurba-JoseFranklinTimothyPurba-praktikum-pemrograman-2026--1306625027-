import random

# 1. Inisialisasi Data Buah
databuah = [
    'anggur', 'apel', 'aprikot', 'asam', 'atap', 'arbei', 'abiu', 'alpukat', 
    'anjeng', 'bacang', 'baguk', 'belimbing', 'bengkuang', 'benda', 'binjai', 
    'bisbul', 'blueberry', 'burahol', 'blewah', 'bit', 'cempedak', 'ceplukan', 
    'cermai', 'ceri', 'cokelat', 'delima', 'duku', 'durian', 'duwet', 'enau', 
    'enamenam', 'frambos', 'hamoi', 'hamlam', 'holdi', 'jamblang', 'jambuair', 
    'jambubatu', 'jambubol', 'jambumawar', 'jambumede', 'jengkol', 'jeruk', 
    'jerukbali', 'jerukkeprok', 'jerukkingkit', 'jeruknipis', 'jerukpurut', 
    'kapulasan', 'kawista', 'kecapi', 'kedondong', 'kelapa', 'kelengkeng', 
    'kelubi', 'ketela', 'kemang', 'kepel', 'kersen', 'kesemek', 'kokosan', 
    'kiwi', 'koldi', 'kurma', 'kelawi', 'kenitu', 'lai', 'langsat', 'lemon', 
    'leci', 'lobak', 'maja', 'malaka', 'mangga', 'manggis', 'markisa', 'melon', 
    'mengkudu', 'menteng', 'matoa', 'mentimun', 'namnam', 'nanas', 'nangka', 
    'naga', 'nona', 'pepaya', 'persik', 'pir', 'pisang', 'pete', 'rambai', 
    'rambusa', 'rambutan', 'rukem', 'sawo', 'semangka', 'sirsak', 'siwalan', 
    'srikaya', 'stroberi', 'sukun', 'terap', 'terong', 'tomat', 'timunsuri', 
    'ubi', 'waluh', 'wuni', 'zaitun'
]

def main_game():
    print("=" * 50)
    print("Permainan Tebak Nama Buah")
    print("Oleh : Jose Franklin Timothy Purba")
    print("NIM  : 1306625027")
    print("=" * 50)
    
    while True:
        # Komputer memilih buah secara acak
        buah_terpilih = random.choice(databuah).lower()
        jumlah_huruf = len(buah_terpilih)
        
        # Inisialisasi tampilan tebakan (huruf tersembunyi dengan '-')
        tebakan_pemain = ['-'] * jumlah_huruf
        nyawa = jumlah_huruf
        huruf_tertebak = set()
        
        print(f"\nKomputer sedang memikirkan nama buah terdiri dari {jumlah_huruf} huruf.")
        print("Nama buah : " + " ".join(tebakan_pemain))
        
        # Loop proses tebak-menebak selama nyawa masih ada dan kata belum tertebak sempurna
        while nyawa > 0 and '-' in tebakan_pemain:
            print(f"Anda memiliki {nyawa} kesempatan untuk menebak huruf buah tersebut.")
            tebakan = input("Tebakan anda ? ").strip().lower()
            
            # Validasi input (harus 1 huruf alfabet)
            if len(tebakan) != 1 or not tebakan.isalpha():
                print("Masukkan hanya SATU huruf alfabet!\n")
                continue
                
            # Cek jika huruf sudah pernah ditebak sebelumnya
            if tebakan in huruf_tertebak:
                print(f"Anda sudah pernah menebak huruf '{tebakan}'. Coba huruf lain.\n")
                continue
                
            huruf_tertebak.add(tebakan)
            
            # Logika pengecekan huruf
            if tebakan in buah_terpilih:
                print(f"Benar. Huruf {tebakan} ada dalam nama buah tersebut.")
                # Update posisi huruf yang benar
                for i in range(jumlah_huruf):
                    if buah_terpilih[i] == tebakan:
                        tebakan_pemain[i] = tebakan
            else:
                print(f"Sayang sekali. Huruf {tebakan} tidak ada dalam nama buah tersebut.")
                nyawa -= 1  # Nyawa berkurang hanya jika tebakan salah
                
            print("Nama buah : " + " ".join(tebakan_pemain))
            print() # Baris baru untuk kerapian
            
        # Penentuan Kalah atau Menang
        if '-' not in tebakan_pemain:
            print("SELAMAT. Anda berhasil !!")
        else:
            # Memformat tampilan jawaban komputer dengan spasi seperti contoh: l a i
            jawaban_format = " ".join(list(buah_terpilih))
            print(f"Anda kalah !!. Nama buah tersebut: {jawaban_format}")
            
        # Pilihan untuk mengulang permainan
        main_lagi = input("Mau main lagi (y/t) ? ").strip().lower()
        if main_lagi != 'y':
            print("\n# SELESAI #")
            break

# Menjalankan program utama
if __name__ == "__main__":
    main_game()
