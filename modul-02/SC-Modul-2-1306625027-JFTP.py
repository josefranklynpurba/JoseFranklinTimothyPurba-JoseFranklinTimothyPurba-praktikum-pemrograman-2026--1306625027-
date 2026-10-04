# Program Faktor Bilangan
print("Program Faktor Bilangan")
print("Nama : Jose Franklin Timothy Purba")
print("NIM  : 1306625027")
print()

# --- Perulangan Utama ---
while True:
    # Meminta input dari user
    bilangan = int(input("Masukkan sembarang bilangan < 100  (masukan 0 untuk selesai) = "))
    
    # Kondisi untuk keluar dari program
    if bilangan == 0:
        print("\n*SELESAI*")
        break
    
    # List untuk menyimpan faktor bilangan
    daftar_faktor = []
    
    # Mencari faktor bilangan
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            daftar_faktor.append(i)
            
    # Menampilkan output hasil
    print(f"Bilangan  {bilangan} -> Faktornya = {daftar_faktor}\n")