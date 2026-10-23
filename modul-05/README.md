# Modul [05] - [Mengurutkan (Sorting)]

**Nama:** [Jose Franklin Timothy Purba]  
**NIM:** [1306625027]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Menyusun dan menyajikan data acak tersebut secara terstruktur sehingga berurutan dari nilai yang paling kecil hingga nilai yang paling besar (ascending order).

## 2. Mathematical Equation
> {Kondisi Perbandingan:} \quad A[j] > A[j+1] \quad \text{dimana } 0 \le j < n - i - 1
> {Operasi Pertukaran:} \quad 
\begin{cases} 
\text{temp} = A[j] \\ 
A[j] = A[j+1] \\ 
A[j+1] = \text{temp} 
\end{cases}.

## 3. Algorithm
> 1. Mulai program.
> 2. Inisialisasi variabel nilai berisi 100 data nilai ujian dari soal.
> 3. Tampilkan identitas praktikan (Nama: Jose Franklin Timothy Purba, NIM: 1306625027).
4. Tampilkan teks "Data nilai awal :".
5. Set nilai awal variabel idx menjadi 0.
6. Lakukan perulangan cetak awal selama idx kurang dari total panjang nilai:
	• 6.1. Ambil 10 elemen dari indeks idx.
	• 6.2. Gabungkan elemen dengan pemisah koma , .
	• 6.3. Jika bukan 10 elemen terakhir, tambahkan tanda koma , di ujung baris.
	• 6.4. Cetak baris tersebut ke layar.
	• 6.5. Tambahkan nilai idx dengan 10 (idx = idx + 10).
7. Hitung jumlah elemen di dalam list nilai dan simpan ke variabel n.
8. Set variabel i = 0 untuk perulangan luar sorting.
9. Lakukan perulangan luar selama i < n:
	• 9.1. Set variabel j = 0 untuk perulangan dalam.
	• 9.2. Lakukan perulangan dalam selama j < n - i - 1:
		• 9.2.1. Jika nilai[j] > nilai[j + 1], tukar posisi kedua elemen tersebut dengan bantuan variabel temp.
		• 9.2.2. Tambahkan nilai j dengan 1 (j = j + 1).
	• 9.3. Tambahkan nilai i dengan 1 (i = i + 1).
10. Tampilkan teks "Data nilai terurut :".
11. Set ulang nilai variabel idx menjadi 0.
12. Lakukan perulangan cetak akhir selama idx kurang dari total panjang nilai:
	• 12.1. Ambil 10 elemen terurut dari indeks idx.
	• 12.2. Gabungkan elemen dengan pemisah koma , .
	• 12.3. Jika bukan 10 elemen terakhir, tambahkan tanda koma , di ujung baris.
	• 12.4. Cetak baris tersebut ke layar.
	• 12.5. Tambahkan nilai idx dengan 10 (idx = idx + 10).
13. Tampilkan teks "*selesai*".
14. Selesai program.
