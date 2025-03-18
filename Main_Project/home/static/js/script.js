// JavaScript to handle automatic image slideshow
document.addEventListener("DOMContentLoaded", function() {
    let index = 0;
    const images = document.querySelectorAll('.home-image-slideshow img');  // Get all the images in the slideshow
    const totalImages = images.length;  // Total number of images

    function showNextImage() {
        // Hide the current image
        images[index].style.opacity = 0;
        
        // Update the index to the next image (loop back to the first image if at the end)
        index = (index + 1) % totalImages;
        
        // Show the next image
        images[index].style.opacity = 1;
    }

    // Set an interval to swap images every 3 seconds (3000 milliseconds)
    setInterval(showNextImage, 3000);
});
