document.getElementById("loginPelamar").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
  
    // Get form values
    var email = document.getElementById("emailLoginPelamar").value;
    var password = document.getElementById("pswdLoginPelamar").value;
    
    // Create an object with form data
    var formData = {
      email_pelamar: email,
      password: password
    };
    console.log(formData)
    // Send form data to server
    fetch("http://127.0.0.1:5000/loginPelamar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
      console.log(data); // Handle response from the server
      // Reset form fields
    })
    .catch(error => {
      console.error("Error:", error);
      // Handle error
    });
  });