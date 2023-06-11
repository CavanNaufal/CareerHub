// document.getElementById("applyButton").addEventListener("click",function(event){
//   event.stopPropagation();
//   applyJob()
// });

// document.getElementById("applyButton").addEventListener("click", function(event) {
//   event.preventDefault(); // Prevent default click behavior
//   applyJob()
// });

document.addEventListener('DOMContentLoaded', function() {
  displayJobDetail();

  setTimeout(function() {
    document.getElementById("delete").style.visibility = "hidden";
  }, 1000); // Menunda pengaturan visibilitas selama 1 detik (1000 milidetik)

  document.getElementById("apply").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default click behavior
  
    setTimeout(function() {
      applyJob();
    }, 1000); // Menunda eksekusi fungsi applyJob selama 1 detik (1000 milidetik)
  });

  document.getElementById("delete").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent default click behavior
  
    setTimeout(function() {
      deleteApply();
    }, 1000); // Menunda eksekusi fungsi deleteApply selama 1 detik (1000 milidetik)
  });
});

//save As jobDetail.js
function displayJobDetail() {
    // Mendapatkan id_pekerjaan dari localStorage yang di-set oleh searchJob.js
    var jobDetailId = localStorage.getItem("id_pekerjaan");
    console.log(jobDetailId);
  
    // Mengirimkan request ke /getJobDetail
    const params = new URLSearchParams({ id_pekerjaan: jobDetailId }); // Membuat objek URLSearchParams dari data permintaan
    const url = `http://127.0.0.1:5000/getJobDetail?${params}`; // Membangun URL dengan parameter
  
    // Membuat objek request
    const requestOptions = {
      method: "POST", // Metode request
      headers: {
        "Content-Type": "application/json",
      },
    };
  
    // Melakukan permintaan menggunakan fetch API
    fetch(url, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        var jobDetailDisplay = document.getElementById("jobDetail");
        jobDetailDisplay.className = "container-xxl py-5 wow fadeInUp";
        jobDetailDisplay.innerHTML = "";
        if (data.success) {
          console.log("success");
        //   var jobDetailDisplay = document.getElementById("jobDetail");
        //   jobDetailDisplay.className = "container-xxl py-5 wow fadeInUp";
        //   jobDetailDisplay.innerHTML = "";
  
          // Memasukkan field posisi, deskripsi, gaji, kualifikasi, nama_perusahaan, kategori ke HTML
          jobDetailDisplay.innerHTML = `
            <div class="container">
              <div class="row gy-5 gx-4">
                <div class="col-lg-8">
                  <div class="d-flex align-items-center mb-5">
                    <img class="flex-shrink-0 img-fluid border rounded" src="/static/img/com-logo-2.jpg" alt="" style="width: 80px; height: 80px;">
                    <div class="text-start ps-4">
                      <h3 class="mb-3">${data.posisi}</h3>
                      <span class="text-truncate me-3"><i class="fa fa-map-marker-alt text-primary me-2"></i>${data.nama_perusahaan}</span>
                      <span class="text-truncate me-3"><i class="far fa-clock text-primary me-2"></i>${data.nama_kategori}</span>
                      <span class="text-truncate me-0"><i class="far fa-money-bill-alt text-primary me-2"></i>${data.gaji}</span>
                    </div>
                  </div>
  
                  <div class="mb-5">
                    <h4 class="mb-3">Job description</h4>
                    <p>${data.deskripsi_pekerjaan}</p>
  
                    <h4 class="mb-3">Responsibility</h4>
                    <p>lorem</p>
  
                    <h4 class="mb-3">Qualifications</h4>
                    <p>${data.kualifikasi}</p>
                  </div>
  
                  <div class="">
                        <h4 class="mb-4">Apply For The Job</h4>
                    
                            <div class="row g-3">
                                <div class="col-12 col-sm-6">
                                  <input type="text" id="tanggal" class="form-control" placeholder="Tanggal">
                                </div>
                                <div class="col-12 col-sm-6">
                                    <input type="text" id="filename" class="form-control" placeholder="Filename">
                                </div>
                                
                                <div class="col-12">
                                    <button id="delete" class="btn btn-primary w-100" type="click">Delete</button>
                                </div>
                            </div>
                
                        
                    </div>
                    <div>
							<button id="apply" type="click" class="btn btn-primary">Update</button>
						      </div>
                </div>
  
                <div class="col-lg-4">
                  <div class="bg-light rounded p-5 mb-4 wow slideInUp" data-wow-delay="0.1s">
                    <h4 class="mb-4">Job Summery</h4>
                    <p><i class="fa fa-angle-right text-primary me-2"></i>Published On: 01 Jan, 2045</p>
                    <p><i class="fa fa-angle-right text-primary me-2"></i>Vacancy: 123 Position</p>
                    <p><i class="fa fa-angle-right text-primary me-2"></i>Job Nature: Full Time</p>
                    <p><i class="fa fa-angle-right text-primary me-2"></i>Salary: $123 - $456</p>
                    <p><i class="fa fa-angle-right text-primary me-2"></i>Location: New York, USA</p>
                    <p class="m-0"><i class="fa fa-angle-right text-primary me-2"></i>Date Line: 01 Jan, 2045</p>
                  </div>
                  <div class="bg-light rounded p-5 wow slideInUp" data-wow-delay="0.1s">
                    <h4 class="mb-4">Company Detail</h4>
                    <p class="m-0">${data.deskripsi_perusahaan}</p>
                  </div>
                </div>
              </div>
            </div>            
          `;
          // localStorage.removeItem("id_pekerjaan");
  
        } else {
          console.log("fail at line 85");
          var message = data.message;
          console.log(message);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }



  function applyJob(){
    console.log("applyJob");
    //get data: tanggal and filename from HTML
    var id_pekerjaan = localStorage.getItem("id_pekerjaan")
    var tanggal = document.getElementById("tanggal").value;
    var filename = document.getElementById("filename").value;

    const reqData={
        id_pekerjaan:id_pekerjaan,
        tanggal:tanggal,
        filename:filename
    };

    fetch("http://127.0.0.1:5000/addLetter",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(reqData)
    })
    .then(response => response.json())
    .then(data=>{
        if(data.success){
            document.getElementById("applyJobButton").style.visibility="hidden";
            //unhide tombol edit dan delete?
            //document.getElementById("edit").style.visibility="visible";  //untuk style.displat: none untuk hide, block untuk unhide
            document.getElementById("delete").style.visibility="visible";
            alert("Lamaran ditambahkan")
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

function deleteApply(){
    var id_pekerjaan = localStorage.getItem("id_pekerjaan")

    const reqData={
        id_pekerjaan:id_pekerjaan
    }

    fetch("http://localhost:5000/removeLetter",{
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(reqData)
    })
    .then(response=>response.json())
    .then(data=>{
        if(data.success){
            document.getElementById("applyJobButton").style.visibility="visible";
            //unhide tombol edit dan delete?
            //document.getElementById("edit").style.visibility="visible";  //untuk style.displat: none untuk hide, block untuk unhide
            document.getElementById("delete").style.visibility="hidden";
            alert("Lamaran dihapus")
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