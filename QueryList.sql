 CREATE TABLE pelamar(
    id_pelamar SERIAL PRIMARY KEY,
    nama_pelamar text NOT NULL,
    email_pelamar text NOT NULL,
    password text NOT NULL,
    alamat_pelamar text NOT NULL,
    pengalaman text NOT NULL,
    pendidikan text NOT NULL);


INSERT INTO pelamar VALUES(DEFAULT,)
CREATE TABLE perusahaan(
    id_perusahaan SERIAL PRIMARY KEY,
    nama_perusahaan text UNIQUE NOT NULL,
    pswd_perusahaan text UNIQUE NOT NULL,
    deskripsi_perusahaan text,
    alamat_perusahaan text NOT NULL);

CREATE TABLE kategori(
    id_kategori SERIAL PRIMARY KEY,
    nama_kategori TEXT UNIQUE NOT NULL
);

CREATE TABLE pekerjaan (
    id_pekerjaan SERIAL PRIMARY KEY,
    id_perusahaan INTEGER REFERENCES perusahaan(id_perusahaan),
    id_kategori INTEGER REFERENCES kategori(id_kategori),
    posisi text NOT NULL,
    deskripsi_pekerjaan text,
    kualifikasi text NOT NULL,
    gaji bigint NOT NULL
);

INSERT INTO pekerjaan VALUES(DEFAULT,1,1,'DevOps Engineer','','2 tahun pengalaman',100000),
                            (DEFAULT,1,1,'Embedded System Engineer','','2 tahun pengalaman',100000),
                            (DEFAULT,1,1,'Data Scientist','','2 tahun pengalaman',100000),
                            (DEFAULT,1,1,'System Admin','','2 tahun pengalaman',50000),
                            (DEFAULT,1,1,'Cybersecurity Architect','','2 tahun pengalaman',100000);
INSERT INTO pekerjaan VALUES(DEFAULT,2,1,'AI Engineeer','','S2',75000);

CREATE TABLE lamaran(
    id_lamaran SERIAL PRIMARY KEY,
    id_pekerjaan INTEGER REFERENCES pekerjaan(id_pekerjaan),
    id_pelamar INTEGER REFERENCES pelamar(id_pelamar),
    tanggal_lamaran DATE NOT NULL,
    status_lamaran INTEGER NOT NULL,
);

CREATE TABLE ulasan(
    id_ulasan SERIAL PRIMARY KEY,
    id_pekerjaan INTEGER REFERENCES pekerjaan(id_pekerjaan),
    id_pelamar INTEGER REFERENCES pelamar(id_pelamar),
    rating INTEGER NOT NULL,
    komentar TEXT
);


SELECT pekerjaan.posisi,pekerjaan.gaji,perusahaan.nama_perusahaan,kategori.nama_kategori
FROM pekerjaan INNER JOIN perusahaan
ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan
INNER JOIN kategori 
ON pekerjaan.id_kategori = kategori.id_kategori
WHERE nama_perusahaan = 'IBM';

SELECT pekerjaan.posisi,pekerjaan.gaji,perusahaan.nama_perusahaan,kategori.nama_kategori
FROM pekerjaan INNER JOIN perusahaan
ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan
INNER JOIN kategori 
ON pekerjaan.id_kategori = kategori.id_kategori
WHERE nama_kategori = 'teknologi';

SELECT pekerjaan.posisi,pekerjaan.gaji,perusahaan.nama_perusahaan,kategori.nama_kategori
FROM pekerjaan INNER JOIN perusahaan
ON pekerjaan.id_perusahaan = perusahaan.id_perusahaan
INNER JOIN kategori 
ON pekerjaan.id_kategori = kategori.id_kategori
WHERE pekerjaan.posisi = 'DevOps Engineer';



INSERT INTO kategori VALUES (DEFAULT,'teknologi'),(DEFAULT,'finance'),(DEFAULT,'manufacture');





