        document.addEventListener('DOMContentLoaded', function() {
            // --- Mobile Menu Toggle ---
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');
            if (mobileMenuButton && mobileMenu) {
                mobileMenuButton.addEventListener('click', () => {
                    mobileMenu.classList.toggle('hidden');
                    // Toggle ARIA expanded state for accessibility
                    const isExpanded = mobileMenuButton.getAttribute('aria-expanded') === 'true' || false;
                    mobileMenuButton.setAttribute('aria-expanded', !isExpanded);
                    mobileMenu.setAttribute('aria-hidden', isExpanded);
                });

                // Close mobile menu when a link is clicked
                mobileMenu.querySelectorAll('a').forEach(link => {
                    link.addEventListener('click', () => {
                        mobileMenu.classList.add('hidden');
                        mobileMenuButton.setAttribute('aria-expanded', 'false');
                        mobileMenu.setAttribute('aria-hidden', 'true');
                    });
                });
            }

            // --- Smooth Scrolling for Anchor Links ---
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    const targetId = this.getAttribute('href');
                    const targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        // Consider header height for accurate scroll position
                        const headerOffset = document.getElementById('header')?.offsetHeight || 0;
                        const elementPosition = targetElement.getBoundingClientRect().top;
                        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                        window.scrollTo({
                            top: offsetPosition,
                            behavior: 'smooth'
                        });
                    }
                });
            });
            
            // --- Active Navigation Link Highlighting ---
            const navLinks = document.querySelectorAll('nav a[href^="#"]');
            const sections = document.querySelectorAll('section[id]');
            const headerHeight = document.getElementById('header')?.offsetHeight || 70; // Estimate header height

            function changeNav() {
                let index = sections.length;

                while(--index && window.scrollY + headerHeight < sections[index].offsetTop) {}
                
                navLinks.forEach((link) => link.classList.remove('nav-link-active'));
                // Check if a corresponding navLink exists before adding class
                if (navLinks[index]) {
                     // Find the specific link that matches the section ID
                    const activeSectionId = sections[index].id;
                    const activeLink = document.querySelector(`nav a[href="#${activeSectionId}"]`);
                    if (activeLink) {
                        activeLink.classList.add('nav-link-active');
                    }
                }
            }
            // Initial check
            changeNav();
            window.addEventListener('scroll', changeNav);


            // --- Scroll Animations (Reveal on Scroll) ---
            const revealElements = document.querySelectorAll('.reveal-on-scroll');
            const revealObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        observer.unobserve(entry.target); // Optional: stop observing once visible
                    }
                });
            }, { threshold: 0.1 }); // Trigger when 10% of the element is visible

            revealElements.forEach(el => {
                revealObserver.observe(el);
            });

            // --- Sticky Header Shrink/Style on Scroll (Optional) ---
            const header = document.getElementById('header');
            if (header) {
                window.addEventListener('scroll', () => {
                    if (window.scrollY > 50) {
                        header.classList.add('py-3', 'shadow-xl');
                        header.classList.remove('py-4');
                    } else {
                        header.classList.add('py-4');
                        header.classList.remove('py-3', 'shadow-xl');
                    }
                });
            }

            // --- Contact Form Validation & Submission ---
            const contactForm = document.getElementById('contact-form');
            if (contactForm) {
                contactForm.addEventListener('submit', function(event) {
                    event.preventDefault(); // Prevent default submission for now

                    // Clear previous messages
                    document.getElementById('name-error').classList.add('hidden');
                    document.getElementById('email-error').classList.add('hidden');
                    document.getElementById('message-error').classList.add('hidden');
                    document.getElementById('form-success').classList.add('hidden');
                    document.getElementById('form-failure').classList.add('hidden');

                    // Get form values
                    const name = document.getElementById('name').value.trim();
                    const email = document.getElementById('email').value.trim();
                    const message = document.getElementById('message').value.trim();
                    let isValid = true;

                    // Basic Validation
                    if (name === '') {
                        document.getElementById('name-error').classList.remove('hidden');
                        isValid = false;
                    }
                    if (email === '' || !/^\S+@\S+\.\S+$/.test(email)) {
                        document.getElementById('email-error').classList.remove('hidden');
                        isValid = false;
                    }
                    if (message === '') {
                        document.getElementById('message-error').classList.remove('hidden');
                        isValid = false;
                    }

                    if (isValid) {
                        // Simulate form submission (replace with actual AJAX call to backend/service)
                        console.log('Form data:', { name, email, subject: document.getElementById('subject').value, message });
                        
                        // Show success message (simulation)
                        setTimeout(() => {
                            document.getElementById('form-success').classList.remove('hidden');
                            contactForm.reset(); // Clear the form
                        }, 1000);

                        // To simulate failure:
                        // setTimeout(() => {
                        //     document.getElementById('form-failure').classList.remove('hidden');
                        // }, 1000);
                    }
                });
            }

            // --- Footer: Current Year ---
            const currentYearSpan = document.getElementById('current-year');
            if (currentYearSpan) {
                currentYearSpan.textContent = new Date().getFullYear();
            }

            // --- Back to Top Button ---
            const backToTopButton = document.getElementById('back-to-top');
            if (backToTopButton) {
                window.addEventListener('scroll', () => {
                    if (window.pageYOffset > 300) { // Show button after scrolling 300px
                        backToTopButton.classList.remove('hidden');
                        backToTopButton.classList.add('opacity-100');
                    } else {
                        backToTopButton.classList.add('hidden');
                        backToTopButton.classList.remove('opacity-100');
                    }
                });

                backToTopButton.addEventListener('click', () => {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                });
            }
        });