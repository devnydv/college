import { config } from './config.js';

// Populate contact information
// document.querySelector('.contact-info').innerHTML = `
//     <p><i class="fas fa-map-marker-alt"></i> ${config.address}</p>
//     <p><i class="fas fa-phone"></i> ${config.phone}</p>
//     <p><i class="fas fa-envelope"></i> ${config.email}</p>
// `;

// Populate social links
document.querySelector('.social-links').innerHTML = `
    <a href="${config.socialLinks.facebook}"><i class="fab fa-facebook"></i></a>
    <a href="${config.socialLinks.twitter}"><i class="fab fa-twitter"></i></a>
    <a href="${config.socialLinks.linkedin}"><i class="fab fa-linkedin"></i></a>
    <a href="${config.socialLinks.instagram}"><i class="fab fa-instagram"></i></a>
`;

// Add active class to current nav item
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', function(e) {
        document.querySelector('.active')?.classList.remove('active');
        this.classList.add('active');
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const href = this.getAttribute('href');
        if (href !== '#') {
            document.querySelector(href).scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Login page functionality
document.querySelectorAll('.login-option').forEach(option => {
    option.addEventListener('click', function() {
        // Hide all forms first
        document.querySelectorAll('.login-form').forEach(form => {
            form.classList.add('hidden');
        });
        // Show clicked option's form
        this.querySelector('.login-form').classList.remove('hidden');
    });
});

// Login form handling
// document.querySelectorAll('.login-form').forEach(form => {
//     form.addEventListener('submit', function(e) {
//         e.preventDefault();
//         const formId = this.closest('.login-option').id;
        
//         // Basic validation - you would typically do this server-side
//         const id = this.querySelector('input[type="text"]').value;
//         const password = this.querySelector('input[type="password"]').value;
        
//         if (id && password) {
//             switch(formId) {
//                 case 'student-login':
//                     window.location.href = 'student-profile.html';
//                     break;
//                 case 'faculty-login':
//                     window.location.href = 'faculty-profile.html';
//                     break;
//                 case 'admin-login':
//                     window.location.href = 'admin-profile.html';
//                     break;
//             }
//         } else {
//             alert('Please fill in all fields');
//         }
//     });
// });

// News filter functionality
document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const filter = this.dataset.filter;
        
        // Update active button
        document.querySelector('.filter-btn.active').classList.remove('active');
        this.classList.add('active');
        
        // Filter news items
        document.querySelectorAll('.news-item').forEach(item => {
            if (filter === 'all' || item.dataset.category === filter) {
                item.style.display = 'flex';
            } else {
                item.style.display = 'none';
            }
        });
    });
});

// Contact form submission
// const contactForm = document.querySelector('.contact-form');
// if (contactForm) {
//     contactForm.addEventListener('submit', function(e) {
//         e.preventDefault();
//         // Add form submission logic here
//         alert('Message sent successfully!');
//         this.reset();
//     });
// }

// Hamburger menu functionality
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger) {
    hamburger.addEventListener('click', (e) => {
        e.stopPropagation();
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
    });
}

// Close menu when clicking a nav link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
    });
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
    if (!hamburger?.contains(e.target) && !navLinks?.contains(e.target)) {
        hamburger?.classList.remove('active');
        navLinks?.classList.remove('active');
    }
});