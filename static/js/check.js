document.addEventListener('DOMContentLoaded',redirectToMainPage);

function redirectToMainPage(){
    if(localStorage.getItem("id_perusahaan")){
        var redir = document.getElementById("home1");
        redir.innerHTML = "";
        redir.innerHTML=`
        <nav class="navbar navbar-expand-lg bg-white navbar-light shadow sticky-top p-0">
            <a href="http://127.0.0.1:5000/company" class="navbar-brand d-flex align-items-center text-center py-0 px-4 px-lg-5">
                <h1 class="m-0 text-primary">CareerHub</h1>
            </a>
            <button type="button" class="navbar-toggler me-4" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <div class="navbar-nav ms-auto p-4 p-lg-0">
                    <a href="http://127.0.0.1:5000/company" class="nav-item nav-link active">Home</a>
                    <a href="http://127.0.0.1:5000/about" class="nav-item nav-link">About</a>
                    <!-- <div class="nav-item dropdown">
                        <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">Jobs</a>
                        <div class="dropdown-menu rounded-0 m-0">
                            <a href="http://127.0.0.1:5000/getJobList" class="dropdown-item">Job List</a>
                            <a href="http://127.0.0.1:5000/getJobDetail" class="dropdown-item">Job Detail</a>
                        </div>
                    </div> -->
                    <div class="nav-item dropdown">
                        <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">Pages</a>
                        <div class="dropdown-menu rounded-0 m-0">
                            <a href="http://127.0.0.1:5000/category" class="dropdown-item">Job Category</a>
                            <a href="http://127.0.0.1:5000/testimonial" class="dropdown-item">Testimonial</a>
                            <a href="http://127.0.0.1:5000/error404" class="dropdown-item">404</a>
                        </div>
                    </div>
                    <a href="http://127.0.0.1:5000/contact" class="nav-item nav-link">Contact</a>
                    <a href="http://127.0.0.1:5000/loginPelamar" id="logoutButton" class="nav-item nav-link" style="color: red;">Logout</a>
                    <a href="http://127.0.0.1:5000/companyprofile" id="username" class="nav-item nav-link" style="color: #00B074; text-decoration: underline;">user</a>
                </div>
                </div>
                <a href="http://127.0.0.1:5000/addJob" id="postJob" class="btn btn-primary rounded-0 py-4 px-lg-5 d-none d-lg-block">Post A Job<i class="fa fa-arrow-right ms-3"></i></a> 
            </div>
        </nav>
        `
    }
}