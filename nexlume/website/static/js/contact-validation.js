document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM Content Loaded'); // Debug log

    // Check if the form exists
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) {
        console.error('Contact form not found in the DOM');
        return;
    }
    console.log('Form found successfully'); // Debug log

    // Email validation regex
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    // Phone validation regex (exactly 10 digits)
    const phoneRegex = /^\d{10}$/;

    function showError(input, message) {
        if (!input) {
            console.error('Invalid input element provided to showError');
            return;
        }

        const parentElement = input.parentElement;
        if (!parentElement) {
            console.error('Input element has no parent');
            return;
        }

        // Remove any existing error message
        const existingError = parentElement.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }

        // Create and append new error message
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message text-red-500 text-sm mt-1';
        errorDiv.textContent = message;
        parentElement.appendChild(errorDiv);

        // Add red border to input
        input.classList.add('border-red-500');
    }

    function removeError(input) {
        if (!input || !input.parentElement) return;

        const errorDiv = input.parentElement.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
        input.classList.remove('border-red-500');
    }

    function validateField(input, fieldName) {
        if (!input) {
            console.error('${fieldName} input element not found');
            return false;
        }

        if (!input.value || typeof input.value.trim !== 'function') {
            console.error('${fieldName} input value is invalid');
            return false;
        }

        return true;
    }

    function validateForm(e) {
        e.preventDefault();
        console.log('Form validation started'); // Debug log

        let isValid = true;

        // Clear all previous errors
        document.querySelectorAll('.error-message').forEach(error => error.remove());

        try {
            // Name validation
            const name = document.getElementById('name');
            if (validateField(name, 'Name')) {
                if (!name.value.trim()) {
                    showError(name, 'Name is required');
                    isValid = false;
                } else {
                    removeError(name);
                }
            }

            // Organization validation
            const organization = document.getElementById('organization');
            if (validateField(organization, 'Organization')) {
                if (!organization.value.trim()) {
                    showError(organization, 'Organization is required');
                    isValid = false;
                } else {
                    removeError(organization);
                }
            }

            // Email validation
            const email = document.getElementById('email');
            if (validateField(email, 'Email')) {
                if (!email.value.trim()) {
                    showError(email, 'Email is required');
                    isValid = false;
                } else if (!emailRegex.test(email.value.trim())) {
                    showError(email, 'Please enter a valid email address');
                    isValid = false;
                } else {
                    removeError(email);
                }
            }

            // Contact validation
            const contact = document.getElementById('contact');
            if (validateField(contact, 'Contact')) {
                if (!contact.value.trim()) {
                    showError(contact, 'Contact number is required');
                    isValid = false;
                } else if (!phoneRegex.test(contact.value.trim())) {
                    showError(contact, 'Please enter a valid 10-digit phone number');
                    isValid = false;
                } else {
                    removeError(contact);
                }
            }

            // Services validation
            const services = document.querySelectorAll('input[name="services"]:checked');
            const servicesGroup = document.querySelector('.checkbox-group');
            if (servicesGroup && services.length === 0) {
                showError(servicesGroup, 'Please select at least one service');
                isValid = false;
            } else {
                removeError(servicesGroup);
            }

            // Investment validation
            const investment = document.getElementById('investment');
            if (validateField(investment, 'Investment')) {
                if (investment.value === 'select') {
                    showError(investment, 'Please select an investment range');
                    isValid = false;
                } else {
                    removeError(investment);
                }
            }

            // Source validation
            const source = document.getElementById('source');
            if (validateField(source, 'Source')) {
                if (source.value === 'select') {
                    showError(source, 'Please select how you heard about us');
                    isValid = false;
                } else {
                    removeError(source);
                }
            }

            // Message validation
            const message = document.getElementById('message');
            if (validateField(message, 'Message')) {
                if (!message.value.trim()) {
                    showError(message, 'Message is required');
                    isValid = false;
                } else {
                    removeError(message);
                }
            }
        } catch (error) {
            console.error('Validation error:', error);
            isValid = false;
        }

        // If form is valid, show success message and submit
        if (isValid) {
            try {
                // Create success popup
                const successPopup = document.createElement('div');
                successPopup.className =
                    'fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-md shadow-lg z-50';
                successPopup.innerHTML = `
                    <div class="flex items-center">
                        <div class="py-1">
                            <svg class="fill-current h-6 w-6 text-green-500 mr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                <path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM6.7 9.29L9 11.6l4.3-4.3 1.4 1.42L9 14.4l-3.7-3.7 1.4-1.42z"/>
                            </svg>
                        </div>
                        <p><strong>Success!</strong> Your message has been sent successfully.</p>
                    </div>
                `;

                document.body.appendChild(successPopup);

                // Remove popup after 3 seconds and submit form
                setTimeout(() => {
                    successPopup.remove();
                    contactForm.submit();
                }, 3000);
            } catch (error) {
                console.error('Error showing success message:', error);
            }
        }
    }

    // Add form submit event listener
    contactForm.addEventListener('submit', validateForm);
    console.log('Submit event listener added'); // Debug log

    // Real-time phone number validation
    const contactInput = document.getElementById('contact');
    if (contactInput) {
        contactInput.addEventListener('input', function () {
            this.value = this.value.replace(/\D/g, '').slice(0, 10);
        });

        contactInput.addEventListener('blur', function () {
            if (!phoneRegex.test(this.value)) {
                showError(this, 'Please enter a valid 10-digit phone number');
            } else {
                removeError(this);
            }
        });
    } else {
        console.error('Contact input element not found');
    }
});