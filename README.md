# CareerHub - Portal Pencarian Pekerjaan Online

CareerHub adalah sebuah aplikasi web yang dirancang untuk menjadi portal pencarian dan perekrutan pekerjaan secara online. Aplikasi ini dibangun menggunakan framework Flask dengan bahasa pemrograman Python.

## Tabel Database

Proyek ini menggunakan basis data PostgreSQL dengan beberapa tabel yang digunakan:

### Tabel "Perusahaan"

- id_perusahaan (integer): ID unik perusahaan
- nama_perusahaan (string): Nama perusahaan
- deskripsi_perusahaan (string): Deskripsi perusahaan
- alamat_perusahaan (string): Alamat perusahaan

### Tabel "Kategori Pekerjaan"

- id_kategori (integer): ID unik kategori pekerjaan
- nama_kategori (string): Nama kategori pekerjaan

### Tabel "Pekerjaan"

- id_pekerjaan (integer): ID unik pekerjaan
- id_perusahaan (integer): ID perusahaan terkait
- id_kategori (integer): ID kategori pekerjaan
- posisi (string): Nama posisi pekerjaan
- deskripsi_pekerjaan (string): Deskripsi pekerjaan
- kualifikasi (string): Persyaratan kualifikasi pekerjaan
- gaji (integer): Gaji yang ditawarkan untuk pekerjaan

### Tabel "Pelamar"

- id_pelamar (integer): ID unik pelamar
- nama_pelamar (string): Nama pelamar
- alamat_pelamar (string): Alamat pelamar
- pengalaman_kerja (string): Riwayat pengalaman kerja pelamar
- pendidikan_terakhir (string): Pendidikan terakhir pelamar

### Tabel "Lamaran"

- id_lamaran (integer): ID unik lamaran
- id_pekerjaan (integer): ID pekerjaan terkait
- id_pelamar (integer): ID pelamar yang mengajukan lamaran
- tanggal_lamaran (date): Tanggal pengajuan lamaran
- status (string): Status lamaran (diterima, ditolak, dalam proses)

### Tabel "Ulasan Pekerjaan"

- id_ulasan (integer): ID unik ulasan
- id_pekerjaan (integer): ID pekerjaan yang ditinjau
- id_pelamar (integer): ID pelamar yang memberikan ulasan
- rating (integer): Rating yang diberikan (skala 1-5)
- komentar (string): Komentar terkait pekerjaan

## Fitur-Fitur

Berikut adalah fitur-fitur yang disediakan oleh CareerHub:

- Registrasi dan login pengguna (pelamar)
- Perusahaan dapat mempublikasikan pekerjaan yang tersedia
- Pencarian pekerjaan berdasarkan posisi, perusahaan, atau kategori pekerjaan
- Melihat detail pekerjaan termasuk deskripsi, kualifikasi, dan gaji yang ditawarkan
- Pelamar dapat mengirimkan lamaran untuk pekerjaan yang diminati
- Pengelolaan status lamaran oleh pelamar dan perusahaan
- Pelamar dapat memberikan ulasan dan rating terhadap pekerjaan yang pernah dilamar
- Melihat riwayat lamaran dan statusnya

## Kelengkapan Proyek

Proyek CareerHub menyediakan beberapa kelengkapan sebagai bagian dari proyek akhir:

- Skenario aplikasi
- Diagram UML
- Flowchart
- ERD (Entity Relationship Diagram)
- File dump database (file .sql)

