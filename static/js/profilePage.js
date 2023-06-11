document.addEventListener('DOMContentLoaded', function() {
    loadUserProfile();
});

document.getElementById("updateform").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default click behavior
  
    editProfile();
  
    // Refresh halaman setelah 1 detik
    setTimeout(function() {
      location.reload();
    },1000);
  });
  
  



function loadUserProfile(){
  
    var userId = localStorage.getItem("id_pelamar");
    const params = new URLSearchParams({ id_pelamar: userId }); // Membuat objek URLSearchParams dari data permintaan
    const url = `http://127.0.0.1:5000/getprofileById?${params}`;
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
        localStorage.setItem("nama_pelamar",data.nama_pelamar);
        localStorage.setItem("email_pelamar",data.email_pelamar);
        localStorage.setItem("alamat_pelamar",data.alamat_pelamar);
        localStorage.setItem("pengalaman",data.pengalaman);
        localStorage.setItem("pendidikan",data.pendidikan);

        document.getElementById("fullname").textContent = data.nama_pelamar;
        document.getElementById("name").value = data.nama_pelamar;
        document.getElementById("email").value = data.email_pelamar;
        document.getElementById("alamat").value = data.alamat_pelamar;
        document.getElementById("education").value = data.pendidikan;
        document.getElementById("experience").value = data.pengalaman;
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

  function editProfile() {
    
  console.log("editProfile");
    var id_pelamar = localStorage.getItem("id_pelamar");
    var nama_pelamar = document.getElementById("name").value;
    var email_pelamar = document.getElementById("email").value;
    var alamat_pelamar = document.getElementById("alamat").value;
    var pendidikan = document.getElementById("education").value;
    var pengalaman = document.getElementById("experience").value;
  
    var formData = {
      id_pelamar: id_pelamar,
      nama_pelamar: nama_pelamar,
      email_pelamar: email_pelamar,
      alamat_pelamar: alamat_pelamar,
      pendidikan: pendidikan,
      pengalaman: pengalaman
    };
  
    console.log(formData);
  
    fetch("http://127.0.0.1:5000/editPelamar", {
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