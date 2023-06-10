function redirecttomain(){
  window.location.href= "http://127.0.0.1:5000/";
}

function login(){
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  //crafting request
  var formData = {
    email_pelamar: email,
    password: password
  };

  // Kirim permintaan POST ke backend
  fetch("http://localhost:5000/loginPelamar",{
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
      //var userloginData=JSON.stringify(data)
      localStorage.setItem("id_pelamar",data.id_pelamar)
      localStorage.setItem("nama_pelamar",data.nama_pelamar)
      localStorage.setItem("email_pelamar",data.email_pelamar)
      localStorage.setItem("alamat_pelamar",data.alamat_pelamar)
      localStorage.setItem("pengalaman",data.pengalaman)
      localStorage.setItem("pendidikan",data.pendidikan)
      // Simpan respons ke localStorage
      //localStorage.setItem("userloginData", JSON.stringify(data));
      // Redirect ke halaman lain
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