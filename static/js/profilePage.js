document.addEventListener('DOMContentLoaded', function() {
    loadUserProfile();
});

function loadUserProfile(){
var nama = localStorage.getItem("nama_pelamar")
var email = localStorage.getItem("email_pelamar")
var alamat = localStorage.getItem("alamat_pelamar")
var edu = localStorage.getItem("pendidikan")
var exp = localStorage.getItem("pengalaman")

document.getElementById("nama").textContent = nama

document.getElementById("namaValue").value = nama
document.getElementById("email").value = email
document.getElementById("alamat").value = alamat
document.getElementById("education").value = edu
document.getElementById("experience").value = exp

}