// Handle word rotation
const words = document.querySelectorAll('.tagline-word');
let currentIndex = 0;

function rotateWords() {
    words[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % words.length;
    words[currentIndex].classList.add('active');
}

// Rotate words every 3 seconds
setInterval(rotateWords, 3000);
