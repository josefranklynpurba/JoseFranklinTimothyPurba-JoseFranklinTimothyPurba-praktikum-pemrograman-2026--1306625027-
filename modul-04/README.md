# Modul [04] - [Perhitungan Data Nilai]

**Nama:** [Jose Franklin Timothy Purba]  
**NIM:** [1306625027]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Menghitung rata-rata nilai berdasarkan bobot yang sudah ditentukan (Tugas 45%, UTS 25%, UAS 30%), lalu mengubah nilai angka tersebut menjadi huruf mutu (A sampai E) secara otomatis saat dicari lewat terminal.

## 2. Mathematical Equation
> Rumus nilai Rata-rata akhir
> Nilai Akhir = (0.45 x Tugas) + (0.25 x UTS) + (0.30 x UAS)
> Acuan Pengubahan Huruf Mutu (Grade)
> • A : 86 - 100
> A- : 81 - 85
> B+ : 76 - 80
> B : 71 - 75
> B- : 66 - 70
> C+ : 61 - 65
> C : 56 - 60
> C- : 51 - 55
> D : 46 - 50
> E : 0 - 45.

## 3. Algorithm
> 1. Mulai (START)
Program aktif dan menampilkan informasi identitas mahasiswa (Nama: Jose Franklin Timothy Purba, NIM: 1306625027) pada layar terminal.

> 2. Memuat Database
Program membaca file DataNilai.xlsx lalu menyimpan seluruh data komponen nilai 124 mahasiswa ke dalam memori sistem.

> 3. Menerima Input (Mulai Perulangan WHILE)
Program meminta pengguna mengetikkan nomor mahasiswa yang ingin dicari atau mengetik kata 'keluar' untuk mengakhiri program.

> 4. Pengecekan Kondisi Keluar (Kondisi 1)
	> 4.1. JIKA pengguna mengetik kata 'keluar', MAKA program mencetak pesan "Program selesai. Terima kasih!", mengeksekusi perintah BREAK (keluar dari perulangan), lalu lompat ke Langkah 9 (SELESAI).
	> 4.2. JIKA TIDAK, program melanjutkan proses ke Langkah 5.
  
> 5. Pengecekan Keberadaan Data (Kondisi 2)
	> 5.1. JIKA nomor mahasiswa yang dimasukkan tidak terdaftar di database, MAKA program mencetak pesan error "Mahasiswa tidak ditemukan", lalu otomatis melompat kembali ke Langkah 3 untuk meminta input baru.
	> 5.2. JIKA nomor mahasiswa terdaftar, MAKA program mengambil data Nilai Tugas, UTS, dan UAS milik mahasiswa tersebut lalu lanjut ke Langkah 6.

> 6. Menghitung Nilai Rata-rata
Program melakukan operasi matematika untuk menghitung Nilai Akhir dengan rumus bobot tertimbang:
Nilai Akhir = (Nilai Tugas x 0.45) + (Nilai UTS x 0.25) + (Nilai UAS x 0.30)

> 7. Klasifikasi Huruf Mutu (Logika IF - ELIF - ELSE)
Program menyaring skor Nilai Akhir ke dalam fungsi bersyarat untuk menentukan Grade:
	• 7.1. JIKA Nilai Akhir >= 86 dan <= 100, MAKA Grade = A
	• 7.2. JIKA TIDAK, JIKA (ELIF) Nilai Akhir >= 81, MAKA Grade = A-
	• 7.3. JIKA TIDAK, JIKA (ELIF) Nilai Akhir >= 76, MAKA Grade = B+
	• 7.4. JIKA TIDAK, JIKA (ELIF) Nilai Akhir >= 71, MAKA Grade = B
	• 7.5. JIKA TIDAK, JIKA (ELIF) Nilai Akhir >= 66, MAKA Grade = B-
	• 7.6. JIKA TIDAK, JIKA (ELIF) Nilai Akhir >= 61, MAKA Grade = C+
	• 7.7. JIKA TIDAK, JIKA (ELIF) Nilai Akhir >= 56, MAKA Grade = C
	• 7.8. JIKA TIDAK, JIKA (ELIF) Nilai Akhir >= 51, MAKA Grade = C-
	• 7.9. JIKA TIDAK, JIKA (ELIF) Nilai Akhir >= 46, MAKA Grade = D
	• 7.10. SELAIN ITU (ELSE), MAKA Grade = E

> 8. Menampilkan Hasil (OUTPUT)
Program mencetak data Nama Mahasiswa, Hasil Nilai Rata-rata, serta Huruf Mutu (Grade) ke layar terminal. Setelah selesai, aliran program otomatis berputar kembali ke Langkah 3 (Looping WHILE).

> 9. Selesai.
