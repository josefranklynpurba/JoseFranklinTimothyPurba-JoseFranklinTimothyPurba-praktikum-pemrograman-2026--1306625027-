# Program Konversi Suhu
nama = "Jose Franklin Timothy Purba"
nim = "1306625027"

suhu_awal = 0
suhu_akhir = 100
selang = 10

# Menampilkan Header Program
print(f"Program konversi Suhu")
print(f"Nama : {nama}")
print(f"NIM  : {nim}")
print()
print(f"-   Suhu awal  = {suhu_awal}")
print(f"-   Suhu akhir = {suhu_akhir}")
print(f"-   Selang     = {selang}")
print()

# Menampilkan Header Tabel dengan Garis Penutup Atas
print("TABEL KONVERSI")
print("+-----+-----------+----------+------------+")
print(f"| {'No.':<3} | {'Celcius':<9} | {'Reamur':<8} | {'Fahrenheit':<10} |")
print("+-----+-----------+----------+------------+")


# Proses Perulangan untuk Menghitung dan Menampilkan Data
no = 1
celcius = suhu_awal

while celcius <= suhu_akhir:
    # Rumus Konversi
    reamur = (4 / 5) * celcius
    fahrenheit = ((9 / 5) * celcius) + 32
    
    # Menampilkan baris tabel yang dipisah dengan garis vertikal
    print(f"| {no:<3} | {celcius:<9} | {reamur:<8.1f} | {fahrenheit:<10.1f} |")
    
    # Update nilai untuk iterasi berikutnya
    celcius += selang
    no += 1

# Menampilkan Garis Penutup Paling Bawah Tabel
print("+-----+-----------+----------+------------+")
