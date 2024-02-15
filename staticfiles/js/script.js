document.addEventListener("DOMContentLoaded", function() {
    let newsTitles = document.querySelectorAll(".side-items p");
    let carousel = document.getElementById("carouselNews");
    newsTitles.forEach(function(title, index) {
        title.addEventListener("click", function() {
            if (!carousel.querySelector('.carousel-item:nth-child(' + (index + 1) + ')').classList.contains('active')) {
                $('#carouselNews').carousel(index);
            }
        });
    });
});

