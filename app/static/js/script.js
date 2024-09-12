const CSlide = document.querySelector('.carousel-slide');
const images = document.querySelectorAll('.carousel-slide img');

// Get the text-carousel and the button
const textCarousel = document.querySelector('.text-carousel');
const spanText = textCarousel.querySelector('span');
const btn = textCarousel.querySelector('.btn');

// Array of text to display for each image
const textContent = [
  "Welcome to Our Hospital",
  "State of the Art Facilities",
  "Experienced Medical Staff"
];

let currentIndex = 0;
const imageWidth = CSlide.clientWidth;
const delay = 10000; // 10 seconds

const textDelay = 500; // Delay for text to appear after image
const textExit = 1000; // Time to exit text

function moveImage() {
  images[currentIndex].style.animation = 'zoomOut 1s forwards';

  // Hide text and button initially
  textCarousel.style.opacity = '0';
  btn.style.opacity = '0';

  setTimeout(() => {
    images[currentIndex].style.animation = '';
    currentIndex = (currentIndex + 1) % images.length;
    CSlide.style.transform = `translateX(-${currentIndex * imageWidth}px)`;

    // Update the text only in the span element
    spanText.textContent = textContent[currentIndex];

    setTimeout(() => {
      textCarousel.style.opacity = '1'; // Make text visible
      btn.style.opacity = '1'; // Show button after text appears
    }, textDelay);

  }, 1000);

  // Hide text and button before moving to the next image
  setTimeout(() => {
    textCarousel.style.opacity = '0';
    btn.style.opacity = '0';
  }, delay - textExit);
}

// Initial setup
CSlide.style.transform = `translateX(0)`;
spanText.textContent = textContent[0];
textCarousel.style.opacity = '1';
btn.style.opacity = '1';

// Start the carousel
setInterval(moveImage, delay);
