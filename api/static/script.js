let slideIndex = {};

function openModal(postId) {
    document.getElementById(`modal-${postId}`).style.display = "block";
    slideIndex[postId] = 1;
    showSlides(postId);
}

function closeModal(postId) {
    document.getElementById(`modal-${postId}`).style.display = "none";
}

// затваряне с Esc
document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
        // Намерете всички отворени модални прозорци и ги затворете
        const openModals = document.querySelectorAll(".modal");
        openModals.forEach(modal => {
            if (modal.style.display === "block") {
                modal.style.display = "none";
            }
        });
    }
});


function changeSlide(n, postId) {
    slideIndex[postId] += n;
    showSlides(postId);
}

function showSlides(postId) {
    let slides = document.querySelectorAll(`#modal-${postId} .slide`);
    if (slideIndex[postId] > slides.length) { slideIndex[postId] = 1 }
    if (slideIndex[postId] < 1) { slideIndex[postId] = slides.length }
    slides.forEach((slide, index) => {
        slide.style.display = (index === slideIndex[postId] - 1) ? "block" : "none";
    });
}


