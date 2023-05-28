

document.getElementById("registrationPelamar").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get form values
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var alamat = document.getElementById("alamat").value;
    var pengalaman = document.getElementById("pengalaman").value;
    var pendidikan = document.getElementById("pendidikan").value;
    // Create an object with form data
    var formData = {
      nama_pelamar: name,
      email_pelamar: email,
      password: password,
      alamat_pelamar: alamat,
      pengalaman : pengalaman,
      pendidikan : pendidikan
    };
    console.log(name)
    // Send form data to server
    fetch("http://127.0.0.1:5000/registerPelamar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    })
    .then(response => {
      if(response.status=200){
        window.location.href = loginPelamar.html;
      }
      else{
        throw new Error("HTTP status code: "+response.status)
      }
    })
    .then(data => {
      console.log(data); // Handle response from the server
      // Reset form fields
    //   document.getElementById("name").value = "";
    //   document.getElementById("email").value = "";
    //   document.getElementById("password").value = "";
    //   document.getElementById("alamat").value = "";
    //   document.getElementById("pengalaman").value="";
    //   document.getElementById("pendidikan").value="";
    })
    .catch(error => {
      console.error("Error:", error);
      // Handle error
    });
  });
  