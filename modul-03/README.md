# Modul [03] - [Trigonometry]

**Nama:** [Jose Franklin Timothy Purba]  
**NIM:** [1306625027]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Membuat Program untuk menghitung nilai sin dan cos dengan pendekatan deret Mc Laurin.

## 2. Mathematical Equation
> Deret McLaurin untuk Sinus : \sin x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots
> Deret McLaurin untuk Cosinus : \cos x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots


## 3. Algorithm
> 1. Mulai
> 2. Inisialisasi variabel data diri:
	• nama = "Jose Franklin Timothy Purba"
	• nim = "1306625027"
> 3. Perulangan Utama (Outer Loop): Mulai blok perulangan untuk menjalankan program secara berulang.
> 3.1. Tampilkan judul program, Nama, dan NIM pengguna di atas layar.
> 3.2. Input besar sudut dalam satuan derajat.
> 3.3. Hitung konversi sudut dari derajat ke radian: \(\text{radian} = \text{sudut} \times \frac{\pi}{180}\).
> 3.4. Hitung True Value (TV) sinus dan cosinus menggunakan fungsi matematika bawaan sistem komputer (math.sin dan math.cos).
> 3.5. Tampilkan nilai True Value sinus dan cosinus yang telah dihitung.
> 3.6. Inisialisasi variabel awal untuk tabel komponen:
* Jumlah Suku = 1
* AV_sinus = 0
* AV_cosinus = 0
* ER_sinus = 100 (nilai awal 100% agar lolos masuk ke dalam perulangan)
* ER_cosinus = 100 (nilai awal 100% agar lolos masuk ke dalam perulangan)
> 3.7. Tampilkan struktur header tabel kolom (Jumlah Suku, AV sinus, ER sinus, AV cosinus, ER cos).
> 3.8. Perulangan Deret (Inner Loop): Lakukan perulangan selama (ER_sinus >= 5) ATAU (ER_cosinus >= 5).
> 3.8.1. Hitung nilai pendekatan sinus (AV_sinus) dengan menambahkan nilai suku ke-Jumlah Suku menggunakan rumus deret Maclaurin Sinus.
> 3.8.2. Hitung nilai pendekatan cosinus (AV_cosinus) dengan menambahkan nilai suku ke-Jumlah Suku menggunakan rumus deret Maclaurin Cosinus.
> 3.8.3. Hitung nilai error relatif sinus: \(ER\_sinus = \left\vert{} \frac{AV\_sinus - TV\_sinus}{TV\_sinus} \right\vert{} \times 100\%\). (Jika TV sinus bernilai 0, ER otomatis disesuaikan agar tidak membagi dengan nol).
> 3.8.4. Hitung nilai error relatif cosinus: \(ER\_cosinus = \left\vert{} \frac{AV\_cosinus - TV\_cosinus}{TV\_cosinus} \right\vert{} \times 100\%\). (Jika TV cosinus bernilai 0, ER otomatis disesuaikan agar tidak membagi dengan nol).
> 3.8.5. Tampilkan hasil perhitungan ke dalam baris tabel sesuai dengan kolomnya masing-masing.
> 3.8.6. Tambahkan indeks suku untuk iterasi berikutnya: Jumlah Suku = Jumlah Suku + 1.
> 3.8.7. Pemeriksaan Batas Keamanan: Jika Jumlah Suku > 50, hentikan perulangan deret secara paksa untuk menghindari infinite loop pada sudut-sudut ekstrem.
> 3.9. Input pilihan pengguna untuk pertanyaan "Mau menghitung lagi (y/t) ?".
> 3.10. Periksa Kondisi: Jika pengguna menginput 't' atau 'T', maka keluar dari Perulangan Utama dan lanjut ke langkah berikutnya. Jika menginput 'y' atau 'Y', sistem akan otomatis mengulang kembali dari langkah 3.1.
> 4. Selesai.
