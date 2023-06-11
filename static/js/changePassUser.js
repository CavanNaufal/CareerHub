//changePass.js

document.getElementById("changePassUser").addEventListener("click", function(event) {
    event.preventDefault(); // Mencegah pengiriman formulir secara default
    changePassUser();
});

function changePassUser() {
    var id_pelamar = localStorage.getItem("id_pelamar");
    var oldPass = document.getElementById("oldPass").value;
    var newPass = document.getElementById("newPass").value;
    var confirmPass = document.getElementById("confirmPass").value;

    if (newPass !== confirmPass) {
        alert("New password and confirm password do not match.");
        return;
    }

    const reqData = {
        id_pelamar: id_pelamar,
        oldPass: oldPass,
        newPass: newPass
    };

    fetch("http://127.0.0.1:5000/changePassUser", {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(reqData)
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
                window.location.href = "http://127.0.0.1:5000/userprofile"
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            console.error("Error:", error);
            // Handle the error
        });
}
