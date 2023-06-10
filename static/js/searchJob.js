document.getElementById("searchButton").addEventListener("click", searchData);

//function untuk me-load halaman 
function redirectToJobDetail(id_pekerjaan) {
  localStorage.setItem("id_pekerjaan", id_pekerjaan)
  //console.log(localStorage.getItem("id_pekerjaan"))
  window.location.href = `http://127.0.0.1:5000/getJobDetail?id_pekerjaan=${id_pekerjaan}`;
 // window.location.href=`http://127.0.0.1:5000/getJobDetail`
}

function searchData() {
  //get input data from HTML elemen
  var searchKey = document.getElementById("searchKey").value;
  var searchData = document.getElementById("searchData").value;
  console.log(searchKey)

  //set key request
  var requestData = {
    key: searchKey,
    data: searchData
  };

  const params = new URLSearchParams(requestData); // Membuat objek URLSearchParams dari data permintaan
  const url = `http://127.0.0.1:5000/searchJob?${params}`; // Membangun URL dengan parameter

  fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json"
    }
  })
    .then(response => response.json())
    .then(data => {
      var jobList = document.getElementById("jobList");
      jobList.innerHTML = "";
      if (data.success) {
        console.log("Success")
        //if(Array.isArray(data.data)){
        data.payload.forEach(jobItem => {
          //localStorage.setItem("id_pekerjaan",jobItem.id_pekerjaan)
          var jobItemElement = document.createElement("div");
          jobItemElement.className = "job-item p-4 mb-4";
          //title ganti posisi, location ganti nama_perusahaan, date atau time ganti jadi kategori
          var jobItemContent = `
            <div class="row g-4">
              <div class="col-sm-12 col-md-8 d-flex align-items-center">
                <img class="flex-shrink-0 img-fluid border rounded" src="/static/img/com-logo-1.jpg" alt="" style="width: 80px; height: 80px;">
                <div class="text-start ps-4">
                  <h5 class="mb-3">${jobItem.posisi}</h5>  
                  <span class="text-truncate me-3"><i class="fa fa-map-marker-alt text-primary me-2"></i>${jobItem.nama_perusahaan}</span>
                  <span class="text-truncate me-3"><i class="far fa-clock text-primary me-2"></i>${jobItem.nama_kategori}</span>
                  <span class="text-truncate me-0"><i class="far fa-money-bill-alt text-primary me-2"></i>${jobItem.gaji}</span>
                </div>
              </div>
              <div class="col-sm-12 col-md-4 d-flex flex-column align-items-start align-items-md-end justify-content-center">
                <div class="d-flex mb-3">
                  <a class="btn btn-light btn-square me-3" href=""><i class="far fa-heart text-primary"></i></a>
                  <a class="btn btn-primary" href="#" onclick="redirectToJobDetail(${jobItem.id_pekerjaan})">Apply Now</a>
                </div>
                <small class="text-truncate"><i class="far fa-calendar-alt text-primary me-2"></i>Date Line: 01 Jan, 2045</small>
              </div>
            </div>
            `;
          jobItemElement.innerHTML = jobItemContent;
          jobList.appendChild(jobItemElement);
        });
        //}
        // else{
        //   var message = data.message;
        //    console.log(message);
        // }  
      }
      else {
        console.log("fail at line 85")
        var message = data.success;
        console.log(message);
      }
    })
    .catch(error => {
      console.error("Error:", error);
    });
}

