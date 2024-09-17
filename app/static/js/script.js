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


window.addEventListener('scroll', function() {
  const section = document.querySelector('.welcome');
  const image = document.querySelector('.welcome-img');
  const heading = document.querySelector('.welcome-heading');
  const paragraph = document.querySelector('.welcome-paragraph');
  const button = document.querySelector('.welcome-btn');

  const sectionPosition = section.getBoundingClientRect().top;
  const screenPosition = window.innerHeight / 5; // Adjust to trigger earlier or later

  if (sectionPosition < screenPosition) {
    // Start image zoom-in
    section.classList.add('show-image');

    // After image is fully shown, show heading, paragraph, and button sequentially
    setTimeout(() => {
      section.classList.add('show-heading');
    }, 5500); // Delay for image animation

    setTimeout(() => {
      section.classList.add('show-paragraph');
    }, 8000); // seconds after heading

    setTimeout(() => {
      section.classList.add('show-button');
    }, 10000); // seconds after paragraph
  }
});


let currentClient = 0;
const clients = document.querySelectorAll('.client');

function showNextClient() {
  // Hide the current client
  clients[currentClient].classList.remove('active');

  // Move to the next client, looping back if necessary
  currentClient = (currentClient + 1) % clients.length;

  // Show the next client
  clients[currentClient].classList.add('active');
}

// Initialize the first client as active
clients[currentClient].classList.add('active');

// Change feedback every 5 seconds
setInterval(showNextClient, 10000);


document.addEventListener("DOMContentLoaded", function () {
  const welcomeSection = document.querySelector(".welcome-section");

  // Show image after 0.5 seconds
  setTimeout(function () {
    welcomeSection.classList.add("show-image");
  }, 500);

  // Show heading after 5.5 seconds
  setTimeout(function () {
    welcomeSection.classList.add("show-heading");
  }, 5500);

  // Show paragraph after 6.5 seconds
  setTimeout(function () {
    welcomeSection.classList.add("show-paragraph");
  }, 6500);

  // Show button after 7.5 seconds
  setTimeout(function () {
    welcomeSection.classList.add("show-button");
  }, 7500);
});
