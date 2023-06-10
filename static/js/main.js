document.getElementById("logoutButton").addEventListener("click",clearLocalStorage);

document.addEventListener('DOMContentLoaded', function() {
    setTimeout(loadProfileName, 10); // Menunda eksekusi selama 1 detik (1000 milidetik)
});



function clearLocalStorage(){
    if(localStorage.getItem("id_pelamar")){
        localStorage.removeItem("id_pelamar")
        localStorage.removeItem("nama_pelamar")
        localStorage.removeItem("email_pelamar")
        localStorage.removeItem("alamat_pelamar")
        localStorage.removeItem("pengalaman")
        localStorage.removeItem("pendidikan")
        window.location.href = "http://127.0.0.1:5000/loginPelamar";
    }
    if(localStorage.getItem("id_perusahaan")){
        localStorage.removeItem("id_perusahaan")
        localStorage.removeItem("nama_perusahaan")
        localStorage.removeItem("email_perusahaan")
        localStorage.removeItem("deskripsi_perusahaan")
        localStorage.removeItem("alamat_perusahaan")
        window.location.href = "http://127.0.0.1:5000/loginPerusahaan";
    }
}

function loadProfileName(){
    var username=localStorage.getItem("nama_pelamar")
    var companyUsername=localStorage.getItem("nama_perusahaan")
    if(localStorage.getItem("id_pelamar")){
        document.getElementById("username").textContent = username
    }else if(localStorage.getItem("id_perusahaan")){
        document.getElementById("username").textContent = companyUsername
    }
    else{
        window.location.href="http://127.0.0.1:5000/loginPelamar";
    }
}


(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').css('top', '0px');
        } else {
            $('.sticky-top').css('top', '-100px');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: true,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav : false,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    
})(jQuery);

