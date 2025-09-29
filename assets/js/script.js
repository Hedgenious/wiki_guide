// DaDa School Wiki Guide - Main JavaScript

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe material cards and guide cards
const cards = document.querySelectorAll('.material-card, .guide-card, .fact-card, .species-item, .toc-section');
cards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(card);
});

// Add scroll effect to header
const header = document.querySelector('.header');
let lastScrollTop = 0;

window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    // Добавляем класс при скроллинге
    if (scrollTop > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
    
    // Шапка всегда остается видимой
    header.style.transform = 'translateY(0)';
    
    lastScrollTop = scrollTop;
});

// Active navigation link
const currentLocation = location.pathname.split('/').pop();
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link => {
    const linkPath = link.getAttribute('href').split('/').pop();
    if (linkPath === currentLocation) {
        link.classList.add('active');
    }
});

// Console message
console.log('%c🎓 DaDa School Wiki Guide', 'color: #1E4EBD; font-size: 20px; font-weight: bold;');
console.log('%cCreated by Hedgenious', 'color: #4A5568; font-size: 14px;');
console.log('%c© 2025 DaDa School', 'color: #4A5568; font-size: 12px;');
