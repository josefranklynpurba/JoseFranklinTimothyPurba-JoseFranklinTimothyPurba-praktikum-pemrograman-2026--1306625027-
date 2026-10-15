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
> 1. START (Mulai)
	> • Menampilkan identitas mahasiswa di terminal:
		> • Nama : Jose Franklin Timothy Purba
		> • NIM  : 1306625027

> 2. INISIALISASI DATA
	> • Membuka file spreadsheet bernama DataNilai.xlsx.
	> • Membaca dan memuat seluruh baris tabel berisi komponen nilai (Tugas, UTS, UAS) milik 124 mahasiswa ke dalam database memori program.

> 3. WHILE (Perulangan Menu Interaktif)
	> • 3.1. INPUT: Meminta pengguna memasukkan nomor urut mahasiswa atau mengetik kata 'keluar'.
	> • 3.2. Pengecekan Kondisi Keluar:
		> • JIKA input dari pengguna bernilai 'keluar', MAKA:
			> • Cetak pesan: "Program selesai. Terima kasih!"
			> • Jalankan perintah BREAK untuk menghentikan perulangan.
			> • Lompat langsung ke Langkah 4 (END).
	> • 3.3. Pengecekan Validitas Data:
		> • JIKA nomor mahasiswa yang diinput tidak ditemukan di database, MAKA:
			> • Cetak pesan: "[Peringatan] Mahasiswa nomor tidak ditemukan."
			> • Kembali mengulang ke Langkah 3 (INPUT).
		> • JIKA nomor mahasiswa ditemukan, MAKA:
			> • Ambil komponen Nilai Tugas, Nilai UTS, dan Nilai UAS dari data mahasiswa tersebut.
			> • Lanjutkan ke proses perhitungan di bawah ini.
	> • 3.4. PROSES PERHITUNGAN RATA-RATA TERTIMBANG:
		> • Hitung akumulasi skor akhir dengan rumus matematika:
> \(\text{Nilai\ Akhir}=(\text{Nilai\ Tugas}\times 0.45)+(\text{Nilai\ UTS}\times 0.25)+(\text{Nilai\ UAS}\times 0.30)\)
	> • 3.5. LOGIKA SELEKSI KONDISI HURUF MUTU (IF - ELIF - ELSE):
		> • JIKA Nilai Akhir ≥ 86 dan ≤ 100, MAKA Grade = "A"
		> • ELIF (Jika Tidak, Jika) Nilai Akhir ≥ 81, MAKA Grade = "A-"
		> • ELIF (Jika Tidak, Jika) Nilai Akhir ≥ 76, MAKA Grade = "B+"
		> • ELIF (Jika Tidak, Jika) Nilai Akhir ≥ 71, MAKA Grade = "B"
		> • ELIF (Jika Tidak, Jika) Nilai Akhir ≥ 66, MAKA Grade = "B-"
		> • ELIF (Jika Tidak, Jika) Nilai Akhir ≥ 61, MAKA Grade = "C+"
		> • ELIF (Jika Tidak, Jika) Nilai Akhir ≥ 56, MAKA Grade = "C"
		> • ELIF (Jika Tidak, Jika) Nilai Akhir ≥ 51, MAKA Grade = "C-"
		> • ELIF (Jika Tidak, Jika) Nilai Akhir ≥ 46, MAKA Grade = "D"
		> • ELSE (Selain itu / Di bawah 46), MAKA Grade = "E"
	> • 3.6. OUTPUT:
		> • Menampilkan informasi akhir ke layar berupa: Nama Mahasiswa, Hasil Nilai Rata-rata (format 2 angka di belakang koma), beserta Huruf Mutu (Grade).
		> • Kembali otomatis berputar ke Langkah 3 (INPUT).

> 4. END (Selesai)
	> • Seluruh alur eksekusi program resmi dihentikan.
