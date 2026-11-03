# Data nilai awal yang diberikan
nilai = [
    85, 13, 99, 34, 71, 15, 82, 24, 64, 61,
    67, 99, 50, 68, 25, 37, 32, 27, 14, 91,
    79, 15, 47, 48, 74, 88, 64, 53, 77, 50,
    24, 91, 87, 55, 60, 75, 91, 22, 47, 63,
    81, 88, 26, 48, 69, 59, 84, 77, 28, 36,
    59, 74, 89, 73, 91, 64, 55, 88, 90, 48,
    73, 97, 98, 40, 93, 50, 78, 60, 44, 77,
    82, 51, 53, 65, 98, 59, 94, 91, 52, 44,
    65, 85, 72, 92, 49, 67, 58, 48, 62, 54,
    89, 67, 58, 48, 85, 45, 77, 76, 81, 77
]

# Menampilkan header program sesuai identitas
print("Program Sorting")
print("Nama : Jose Franklin Timothy Purba")
print("NIM  : 1306625027")
print()

# Fungsi untuk mencetak data dengan format 10 elemen per baris
def cetak_data(data):
    i = 0
    while i < len(data):
        baris = data[i:i+10]
        teks_baris = ", ".join(map(str, baris))
        if i + 10 < len(data):
            teks_baris += ","
        print(teks_baris)
        i += 10

# Menampilkan data nilai awal
print("Data nilai awal :")
cetak_data(nilai)
print()

# Proses pengurutan (Sorting) menggunakan Bubble Sort dengan while loop
n = len(nilai)
i = 0
while i < n:
    j = 0
    while j < n - i - 1:
        if nilai[j] > nilai[j + 1]:
            # Menukar posisi jika elemen kiri lebih besar dari elemen kanan
            nilai[j], nilai[j + 1] = nilai[j + 1], nilai[j]
        j += 1
    i += 1

# Menampilkan data nilai yang sudah terurut
print("Data nilai terurut :")
cetak_data(nilai)
print("Selesai")