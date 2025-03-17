document.addEventListener("DOMContentLoaded", function () {
    /** Image Slideshow **/
    let slideIndex = 0;
    const slides = document.querySelectorAll(".image-slideshow img");
    const slideDuration = 3000; // Adjust duration here (in ms)

    function showSlides() {
        slides.forEach((slide, index) => {
            slide.style.display = index === slideIndex ? "block" : "none";
        });
        slideIndex = (slideIndex + 1) % slides.length;
    }

    if (slides.length > 0) {
        setInterval(showSlides, slideDuration);
    }

    /** Text Content Swap **/
    const content1 = document.getElementById("content1");
    const content2 = document.getElementById("content2");
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");

    function swapContent() {
        content1.classList.toggle('visible');
        content2.classList.toggle('visible');
    }

    if (prevButton && nextButton) {
        prevButton.addEventListener("click", swapContent);
        nextButton.addEventListener("click", swapContent);
    }

    // Initialize content visibility
    content1.classList.add('visible');
    content2.classList.remove('visible');

    /** Form Validation **/
    const contactForm = document.getElementById("contact-form");

    if (contactForm) {
        contactForm.addEventListener("submit", function (event) {
            const name = document.getElementById("name").value.trim();
            const contactNumber = document.getElementById("contact_number").value.trim();
            const email = document.getElementById("email").value.trim();
            const message = document.getElementById("message").value.trim();

            if (name === "" || contactNumber === "" || email === "" || message === "") {
                alert("All fields must be filled!");
                event.preventDefault();
            } else if (!/^\d{10}$/.test(contactNumber)) {
                alert("Enter a valid 10-digit contact number!");
                event.preventDefault();
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                alert("Enter a valid email address!");
                event.preventDefault();
            }
        });
    }
});
