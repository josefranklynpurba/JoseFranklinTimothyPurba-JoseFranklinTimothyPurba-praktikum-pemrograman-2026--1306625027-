import math

# Data Diri
NAMA = "Jose Franklin Timothy Purba"
NIM = "1306625027"

def tampilkan_identitas():
    """Menampilkan header program dan identitas mahasiswa."""
    print("\n" + "="*65)
    print("Program Sinus-Cosinus (Deret Maclaurin)")
    print(f"Nama : {NAMA}")
    print(f"NIM  : {NIM}")
    print("="*65 + "\n")

def proses_deret(x_rad, tv_sin, tv_cos):
    """Menghitung deret sinus dan cosinus sesuai dengan logika di gambar."""
    suku = 1
    av_sin = 0.0
    av_cos = 0.0
    
    # Header tabel disesuaikan dengan format spasi cetak di gambar
    print(f"| {'Suku':^11} | {'AV Sinus':^12} | {'ER Sinus':^10} | {'AV Cosinus':^12} | {'ER Cosinus':^10} |")
    print("-" * 73)
    
    while True:
        # 1. Perhitungan term suku deret sesuai gambar
        term_sin = ((-1)**(suku - 1)) * (x_rad**(2*suku - 1)) / math.factorial(2*suku - 1)
        term_cos = ((-1)**(suku - 1)) * (x_rad**(2*suku - 2)) / math.factorial(2*suku - 2)
        
        # 2. Akumulasi perkiraan nilai (AV)
        av_sin += term_sin
        av_cos += term_cos
        
        # 3. Hitung Error Relatif (ER) menggunakan inline if-else dari gambar
        er_sin = abs((av_sin - tv_sin) / tv_sin) * 100 if tv_sin != 0 else 0.0
        er_cos = abs((av_cos - tv_cos) / tv_cos) * 100 if tv_cos != 0 else 0.0
        
        # 4. Mencetak baris data sesuai format string di gambar
        print(f"| {suku:^11} | {av_sin:^12.6f} | {er_sin:^9.2f}% | {av_cos:^12.6f} | {er_cos:^9.2f}% |")
        
        # 5. Cek kondisi berhenti: kedua error harus di bawah 5%
        if er_sin < 5 and er_cos < 5:
            break
            
        suku += 1
        
        # Batasan pengaman jika iterasi terlalu tinggi (mencegah lag berat)
        if suku > 50:
            print("\n[Catatan: Batas maksimum 50 iterasi tercapai]")
            break

def main():
    """Fungsi utama untuk mengatur alur jalannya program (Outer Loop)."""
    while True:
        tampilkan_identitas()
        
        # Input besar sudut dalam derajat
        sudut_derajat = float(input("Besar sudut (derajat) = "))
        
        # Konversi derajat ke radian
        x_rad = math.radians(sudut_derajat)
        
        # Hitung True Value (TV)
        tv_sin = math.sin(x_rad)
        tv_cos = math.cos(x_rad)
        
        # Menampilkan Informasi True Value
        print(f"\nTrue value sin({sudut_derajat}) = {tv_sin:.6f}")
        print(f"True value cos({sudut_derajat}) = {tv_cos:.6f}")
        print("-" * 73)
        
        # Memproses perhitungan deret Maclaurin
        proses_deret(x_rad, tv_sin, tv_cos)
        print("-" * 73)
        
        # Opsi perulangan program utama
        ulang = input("Mau menghitung lagi (y/t) ? ").strip().lower()
        if ulang == 't':
            print("\nProgram selesai. Terima kasih!")
            break

# Titik masuk utama program Python
if __name__ == "__main__":
    main()
