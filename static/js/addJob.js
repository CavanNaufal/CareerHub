document.getElementById("addjob").addEventListener("submit", addJob);

function addJob(event) {
  event.preventDefault(); // Menghentikan perilaku bawaan saat submit

  var id_perusahaan = localStorage.getItem("id_perusahaan");
  var gaji = document.getElementById("gaji").value;
  var posisi = document.getElementById("posisi").value;
  var kualifikasi = document.getElementById("kualifikasi").value;
  var deskripsi = document.getElementById("deskripsi").value;
  var id_kategori = document.getElementById("kategori").value;

  const reqData = {
    id_perusahaan: id_perusahaan,
    id_kategori: id_kategori,
    gaji: gaji,
    posisi: posisi,
    kualifikasi: kualifikasi,
    deskripsi: deskripsi
  };

  console.log(reqData);

  fetch("http://localhost:5000/addJob", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(reqData),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        alert(data.message);
        // window.location.href = "http://127.0.0.1:5000/company";
      } else {
        alert(data.message);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      // Tangani kesalahan
    });
}
