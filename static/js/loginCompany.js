function redirecttomain(){
    window.location.href= "http://127.0.0.1:5000/company";
  }
  
  function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var formData = {
        email_perusahaan: email,
        pswd_perusahaan: password
  };
  
  // Kirim permintaan POST ke backend
  fetch("http://localhost:5000/loginPerusahaan", {
    method: "POST",
    headers: {
    "Content-Type": "application/json"
    },
    body: JSON.stringify(formData)
  })
  .then(response => {
    if(response.status=200){
    console.log('OK')
    return response.json();
    }
    else{
    throw new Error("HTTP status code: "+response.status)
    }
  })
  .then(data => {
    // Tangani respons dari backend
    if (data.success) {
      console.log(data);
      localStorage.setItem("id_perusahaan",data.id_perusahaan)
      localStorage.setItem("nama_perusahaan",data.nama_perusahaan)
      localStorage.setItem("email_perusahaan",data.email_perusahaan)
      localStorage.setItem("deskripsi_perusahaan",data.deskripsi_perusahaan)
      localStorage.setItem("alamat_perusahaan",data.alamat_perusahaan)
  
      redirecttomain();
    } else {
    // Jika login gagal, tampilkan pesan kesalahan
    alert(data.message);
    }
  })
  .catch(error => {
    console.error("Error:", error);
    // Tangani kesalahan
  });
  }
  
  // Event listener untuk tombol login
  document.getElementById("loginPelamar").addEventListener("submit", function(event) {
  event.preventDefault(); // Mencegah pengiriman formulir secara default
  login();
  });
