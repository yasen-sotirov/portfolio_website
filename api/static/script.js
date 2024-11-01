let slideIndex = {};

function openModal(postId) {
    document.getElementById(`modal-${postId}`).style.display = "block";
    slideIndex[postId] = 1;
    showSlides(postId);
}

function closeModal(postId) {
    document.getElementById(`modal-${postId}`).style.display = "none";
}

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
