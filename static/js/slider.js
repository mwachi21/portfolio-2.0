// Select elements
const slides = document.querySelector('.custom-slider .slides');
const indicatorsContainer = document.getElementById('indicators');
const slideCount = document.querySelectorAll('.custom-slider .slide').length;
let currentIndex = 0;
let interval;

// Create indicators
for (let i = 0; i < slideCount; i++) {
  const indicator = document.createElement('div');
  indicator.classList.add('indicator');
  if (i === 0) indicator.classList.add('active');
  indicatorsContainer.appendChild(indicator);

  indicator.addEventListener('click', () => {
    clearInterval(interval);
    currentIndex = i;
    updateSlider();
    startAutoSlide();
  });
}

const indicators = document.querySelectorAll('.custom-slider .indicator');

// Update slider position
function updateSlider() {
  slides.style.transform = `translateX(-${currentIndex * 100}%)`;
  indicators.forEach((indicator, index) => {
    indicator.classList.toggle('active', index === currentIndex);
  });
}

// Auto-slide functionality
function autoSlide() {
  currentIndex = (currentIndex + 1) % slideCount;
  updateSlider();
}

function startAutoSlide() {
  interval = setInterval(autoSlide, 5000);
}

// Start the slider
startAutoSlide();

// Select elements
const menuToggle = document.getElementById('menu-toggle');
const navLinks = document.getElementById('nav-links');

// Toggle the menu on mobile
menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});