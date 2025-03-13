document.addEventListener('DOMContentLoaded', function () {
    let currentContentIndex = 0;
    const contentSections = document.querySelectorAll('.text-content');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');

    function showContent(index) {
        contentSections.forEach((content, i) => {
            if (i === index) {
                content.style.display = 'block';
            } else {
                content.style.display = 'none';
            }
        });
    }

    function updateButtons() {
        prevButton.disabled = currentContentIndex === 0;
        nextButton.disabled = currentContentIndex === contentSections.length - 1;
    }

    prevButton.addEventListener('click', function () {
        if (currentContentIndex > 0) {
            currentContentIndex--;
            showContent(currentContentIndex);
            updateButtons();
        }
    });

    nextButton.addEventListener('click', function () {
        if (currentContentIndex < contentSections.length - 1) {
            currentContentIndex++;
            showContent(currentContentIndex);
            updateButtons();
        }
    });

    // Initial setup
    showContent(currentContentIndex);
    updateButtons();
});
