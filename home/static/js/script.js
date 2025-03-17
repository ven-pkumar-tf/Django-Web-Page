document.addEventListener("DOMContentLoaded", function () {
    /** Image Slideshow **/
    let slideIndex = 0;
    const slides = document.querySelectorAll(".image-slideshow img");

    function showSlides() {
        slides.forEach((slide, index) => {
            slide.style.display = index === slideIndex ? "block" : "none";
        });

        slideIndex = (slideIndex + 1) % slides.length;
    }

    if (slides.length > 0) {
        setInterval(showSlides, 3000); // Change image every 3 seconds
    }

    /** Text Content Swap **/
    const content1 = document.getElementById("content1");
    const content2 = document.getElementById("content2");
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");

    function swapContent() {
        if (content1.style.display === "none") {
            content1.style.display = "block";
            content2.style.display = "none";
        } else {
            content1.style.display = "none";
            content2.style.display = "block";
        }
    }

    if (prevButton && nextButton) {
        prevButton.addEventListener("click", swapContent);
        nextButton.addEventListener("click", swapContent);
    }

    // Initialize content visibility
    content1.style.display = "block";
    content2.style.display = "none";

    /** Form Validation **/
    const contactForm = document.getElementById("contact-form");

    if (contactForm) {
        contactForm.addEventListener("submit", function (event) {
            const name = document.getElementById("name").value.trim();
            const contactNumber = document.getElementById("contact_number").value.trim();
            const email = document.getElementById("email").value.trim();
            const message = document.getElementById("message").value.trim();

            if (name === "" || contactNumber === "" || email === "" || message === "") {
                alert("கிருப்பதற்காக எல்லா புலன்களும் நிரப்ப வேண்டும்! (All fields must be filled out!)");
                event.preventDefault();
            } else if (!/^\d{10}$/.test(contactNumber)) {
                alert("சரியான 10 இலக்க கைபேசி எண்ணை உள்ளிடவும்! (Enter a valid 10-digit contact number!)");
                event.preventDefault();
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                alert("சரியான மின்னஞ்சல் முகவரியை உள்ளிடவும்! (Enter a valid email address!)");
                event.preventDefault();
            }
        });
    }
});
