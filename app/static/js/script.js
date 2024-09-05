const CSlide = document.querySelector('.carousel-slide');
const images = document.querySelectorAll('.carousel-slide img');

let currentIndex = 0;
const imageWidth = CSlide.clientWidth;
const delay = 10000; // 10 seconds

function moveImage() {
    // Apply zoom-in effect
    images[currentIndex].style.animation = 'zoomOut 1s forwards';

    setTimeout(() => {
        // Reset animation
        images[currentIndex].style.animation = '';

        // Forward to next image
        currentIndex = (currentIndex + 1) % images.length;
        CSlide.style.transform = `translateX(-${currentIndex * imageWidth}px)`;
    }, 3000); // finish zoom out
}

// set up
CSlide.style.transform = `translateX(0)`;

// call function to start carousel
setInterval(moveImage, delay);
