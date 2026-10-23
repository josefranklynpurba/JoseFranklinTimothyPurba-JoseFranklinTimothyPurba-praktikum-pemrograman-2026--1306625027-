import openpyxl
import os

# Fungsi Klasifikasi Huruf Mutu (Logika IF - ELIF - ELSE)
def konversi_grade(nilai):
    if 86 <= nilai <= 100:
        return "A"
    elif 81 <= nilai < 86:
        return "A-"
    elif 76 <= nilai < 81:
        return "B+"
    elif 71 <= nilai < 76:
        return "B"
    elif 66 <= nilai < 71:
        return "B-"
    elif 61 <= nilai < 66:
        return "C+"
    elif 56 <= nilai < 61:
        return "C"
    elif 51 <= nilai < 56:
        return "C-"
    elif 46 <= nilai < 51:
        return "D"
    else:
        return "E"

# Memuat Database Langsung dari File Excel (.xlsx)
def muat_data_excel(nama_file):
    database_mahasiswa = {}
    try:
        # Membuka file Excel dan mengambil sheet pertama yang aktif
        wb = openpyxl.load_workbook(nama_file, data_only=True)
        sheet = wb.active
        
        # Membaca baris mulai dari baris ke-2 (melewati header kolom)
        for baris in sheet.iter_rows(min_row=2, values_only=True):
            if not baris or baris[0] is None:  # Berhenti jika ada baris kosong
                continue
                
            nama_mhs = str(baris[0]).strip()
            nomor_id = int(nama_mhs.split()[-1])  # Mengambil nomor angka paling belakang
            
            database_mahasiswa[nomor_id] = {
                "nama": nama_mhs,
                "tugas": float(baris[2]) if baris[2] is not None else 0.0,
                "uts": float(baris[3]) if baris[3] is not None else 0.0,
                "uas": float(baris[4]) if baris[4] is not None else 0.0
            }
        return database_mahasiswa
    except FileNotFoundError:
        print(f"[Error] File tidak ditemukan pada lokasi: {nama_file}")
        return None
    except Exception as e:
        print(f"[Error] Terjadi kegagalan membaca Excel: {e}")
        return None

# Alur Program Utama
def main():
    # SOLUSI JALUR PAKSA: Langsung arahkan ke lokasi file Excel yang sebenarnya
    # Gunakan salah satu baris di bawah ini yang sesuai dengan posisi asli file Anda:
    
    # Opsi A: Jika file Excel ada di dalam folder aneh berakhiran .py tersebut
    nama_file_excel = r"C:\Users\LOQ\Documents\Datanilai.xlsx\DataNilai.xlsx"
    
    # Opsi B: (Hapus tanda # di bawah jika Anda memindahkan file Excel langsung ke folder Documents)
    # nama_file_excel = r"C:\Users\LOQ\Documents\DataNilai.xlsx"
    
    data_mahasiswa = muat_data_excel(nama_file_excel)
    
    if not data_mahasiswa:
        return

    # Menampilkan Identitas Anda
    print("====================================================")
    print("Nama : Jose Franklin Timothy Purba")
    print("NIM  : 1306625027")
    print("====================================================")
    print("=== SISTEM PENCARIAN & PERHITUNGAN NILAI MAHASISWA ===")
    print(f"Berhasil memuat {len(data_mahasiswa)} data mahasiswa dari Excel.\n")

    # Menerima Input (Perulangan WHILE)
    while True:
        try:
            input_user = input("Ingin menginput/mencari data mahasiswa nomor berapa? (Ketik 'keluar' untuk berhenti): ")
            
            if input_user.lower() == 'keluar':
                print("Program selesai. Terima kasih!")
                break
                
            no_mhs = int(input_user)
            
            if no_mhs in data_mahasiswa:
                mhs = data_mahasiswa[no_mhs]
                rata_rata = (mhs["tugas"] * 0.45) + (mhs["uts"] * 0.25) + (mhs["uas"] * 0.30)
                grade = konversi_grade(rata_rata)
                print(f"-> {mhs['nama']} rata-ratanya {rata_rata:.2f} - {grade}\n")
            else:
                print(f"[Peringatan] Mahasiswa nomor {no_mhs} tidak ditemukan.\n")
                
        except ValueError:
            print("[Error] Masukkan tidak valid! Sila masukkan angka nomor mahasiswa saja.\n")

if __name__ == "__main__":
    main()