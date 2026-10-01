# Modul [02] - [Mencari Faktor Bilangan]

**Nama:** [Jose Franklin Timothy Purba]  
**NIM:** [1306625027]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Membuat program pencari faktor dari suatu bilangan bulat positif kurang dari 100. Program akan berjalan secara berulang untuk menerima input angka dan menampilkan daftar faktornya hingga pengguna memasukkan angka 0.
## 2. Mathematical Equation
> Faktor dari suatu bilangan n: n (mod f) = 0
> (Keterangan: f adalah faktor dari n jika sisa hasil bagi n dengan f adalah 0, di mana 1 <= f <= n).

## 3. Algorithm
> 1. Mulai
> 2. Cetak/Print Judul "Program Faktor Bilangan"
> 3. Print "Nama : Jose Franklin Timothy Purba"
> 4. Print "NIM  : 1306625027"
> 5. Lakukan perulangan terus-menerus (while True)
> 6. Input "Masukkan sembarang bilangan < 100 (masukan 0 untuk selesai) : "
> 7. Periksa apakah bilangan sama dengan 0
> 8. Jika ya, Print "*SELESAI*" dan hentikan perulangan (keluar program)
> 9. Inisialisasi list kosong daftar_faktor = []
> 10. Lakukan perulangan variabel i dari 1 sampai dengan nilai bilangan\
> 11. Jika bilangan habis dibagi i (bilangan % i == 0), masukkan nilai i ke dalam daftar_faktor
> 12. Print Hasil "Bilangan [bilangan] -> Faktornya = [daftar_faktor]"
> 13. Selesai.
