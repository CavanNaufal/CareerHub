//save as companyProfile.js
document.addEventListener('DOMContentLoaded', function() {
  loadCompanyProfile();
});

document.getElementById("updateform").addEventListener("click", function(event) {
  event.preventDefault(); // Prevent default click behavior

  editCompanyProfile();

  // Refresh halaman setelah 1 detik
  setTimeout(function() {
    location.reload();
  },1000);
});

function loadCompanyProfile(){
  var companyId = localStorage.getItem("id_perusahaan");
  const params = new URLSearchParams({ id_perusahaan: companyId }); // Membuat objek URLSearchParams dari data permintaan
  const url = `http://127.0.0.1:5000/getCompanyById?${params}`;
  const requestOptions = {
      method: "GET", // Metode request
      headers: {
      "Content-Type": "application/json"
      },
  };

  fetch(url,requestOptions)
  .then(response=>response.json())
  .then(data=>{
      if(data.success){
          localStorage.setItem("nama_perusahaan",data.nama_perusahaan);
          localStorage.setItem("email_perusahaan",data.email_perusahaan);
          localStorage.setItem("alamat_perusahaan",data.alamat_perusahaan);
          localStorage.setItem("deskripsi_perusahaan",data.deskripsi_perusahaan);

          document.getElementById("fullname").textContent = data.nama_perusahaan;
          document.getElementById("nama").value = data.nama_perusahaan;
          document.getElementById("email").value = data.email_perusahaan;
          document.getElementById("alamat").value = data.alamat_perusahaan;
          document.getElementById("deskripsi").value = data.deskripsi_perusahaan;
      }
      else{
          alert(data.message)
      }
  })
  .catch(error => {
      console.error("Error:", error);
      // Tangani kesalahan
  });
}


function editCompanyProfile(){
  var id_perusahaan = localStorage.getItem("id_perusahaan");
  var nama_perusahaan = document.getElementById("nama").value;
  var email_perusahaan = document.getElementById("email").value;
  var alamat_perusahaan = document.getElementById("alamat").value;
  var deskripsi_perusahaan = document.getElementById("deskripsi").value;

  var formData = {
      id_perusahaan: id_perusahaan,
      nama_perusahaan:nama_perusahaan,
      email_perusahaan:email_perusahaan,
      alamat_perusahaan:alamat_perusahaan,
      deskripsi_perusahaan:deskripsi_perusahaan
  };

  fetch("http://127.0.0.1:5000/editPerusahaan", {
  method: "PUT",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(formData)
})
.then(response => response.json())
      .then(data => {
        // Handle response data
        console.log(data);
      })
      .catch(error => {
        // Handle errors
        console.error(error);
      });
}