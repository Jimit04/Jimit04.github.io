Contact & Collaboration
=======================

.. raw:: html

    <style>
        .contact-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            margin: 2rem 0;
        }
        
        .contact-card {
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #1a2332;
            transition: all 0.3s ease;
        }
        
        .contact-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-label {
            display: block;
            font-weight: 600;
            color: #374151;
            margin-bottom: 0.5rem;
        }
        
        .form-input, .form-select, .form-textarea {
            width: 100%;
            padding: 1rem;
            border: 2px solid #e5e7eb;
            border-radius: 0.5rem;
            font-size: 1rem;
            transition: all 0.3s ease;
            background: white;
            font-family: inherit;
        }
        
        .form-input:focus, .form-select:focus, .form-textarea:focus {
            outline: none;
            border-color: #64748b;
            box-shadow: 0 0 0 3px rgba(100, 116, 139, 0.1);
        }
        
        .form-input.error, .form-select.error, .form-textarea.error {
            border-color: #ef4444;
            box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
        }
        
        .form-textarea {
            resize: vertical;
            min-height: 120px;
        }
        
        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }
        
        .submit-button {
            background: linear-gradient(135deg, #1a2332, #64748b);
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 0.5rem;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .submit-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        
        .submit-button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        
        .contact-info-item {
            display: flex;
            align-items: center;
            padding: 1rem;
            background: #f8fafc;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }
        
        .contact-info-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .contact-icon {
            width: 3rem;
            height: 3rem;
            background: linear-gradient(135deg, #1a2332, #64748b);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 1rem;
            flex-shrink: 0;
            color: white;
        }
        
        .social-links {
            display: flex;
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .social-link {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 3rem;
            height: 3rem;
            background: white;
            border-radius: 50%;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            color: #374151;
            text-decoration: none;
        }
        
        .social-link:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
            color: #1a2332;
        }
        
        .availability-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .availability-item {
            background: #f8fafc;
            padding: 1rem;
            border-radius: 0.5rem;
            text-align: center;
        }
        
        .availability-type {
            font-weight: 600;
            color: #1a2332;
            margin-bottom: 0.5rem;
        }
        
        .availability-status {
            color: #059669;
            font-weight: 500;
        }
        
        .faq-section {
            margin: 3rem 0;
        }
        
        .faq-item {
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 4px solid #1a2332;
            transition: all 0.3s ease;
        }
        
        .faq-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }
        
        .faq-question {
            font-size: 1.25rem;
            font-weight: 600;
            color: #1a2332;
            margin-bottom: 1rem;
        }
        
        .faq-answer {
            color: #6b7280;
            line-height: 1.6;
        }
        
        .notification {
            position: fixed;
            top: 2rem;
            right: 2rem;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            color: white;
            font-weight: 600;
            z-index: 1000;
            transform: translateX(100%);
            transition: transform 0.3s ease;
        }
        
        .notification.show {
            transform: translateX(0);
        }
        
        .notification.success {
            background: #10b981;
        }
        
        .notification.error {
            background: #ef4444;
        }
        
        .floating-element {
            position: absolute;
            width: 20px;
            height: 20px;
            background: rgba(100, 116, 139, 0.1);
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        
        @media (max-width: 768px) {
            .contact-grid {
                grid-template-columns: 1fr;
            }
            
            .form-grid {
                grid-template-columns: 1fr;
            }
            
            .social-links {
                justify-content: center;
            }
        }
    </style>

Get In Touch
------------

.. container:: contact-grid

    .. container:: contact-card

        **Send a Message**

        Fill out the form below and I'll get back to you within 24 hours.

        .. raw:: html

            <form id="contact-form">
                <div class="form-grid">
                    <div class="form-group">
                        <label for="name" class="form-label">Full Name *</label>
                        <input type="text" id="name" name="name" class="form-input" placeholder="Your full name" required>
                        <div class="error-message" style="color: #ef4444; font-size: 0.875rem; margin-top: 0.25rem; display: none;"></div>
                    </div>
                    <div class="form-group">
                        <label for="email" class="form-label">Email Address *</label>
                        <input type="email" id="email" name="email" class="form-input" placeholder="your.email@example.com" required>
                        <div class="error-message" style="color: #ef4444; font-size: 0.875rem; margin-top: 0.25rem; display: none;"></div>
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="company" class="form-label">Company/Organization</label>
                    <input type="text" id="company" name="company" class="form-input" placeholder="Your company name">
                </div>
                
                <div class="form-group">
                    <label for="subject" class="form-label">Subject *</label>
                    <select id="subject" name="subject" class="form-select" required>
                        <option value="">Select a topic</option>
                        <option value="consultation">Engineering Consultation</option>
                        <option value="automation">CAE Automation Project</option>
                        <option value="ai-ml">AI/ML Integration</option>
                        <option value="collaboration">Research Collaboration</option>
                        <option value="job-opportunity">Job Opportunity</option>
                        <option value="other">Other</option>
                    </select>
                    <div class="error-message" style="color: #ef4444; font-size: 0.875rem; margin-top: 0.25rem; display: none;"></div>
                </div>
                
                <div class="form-group">
                    <label for="message" class="form-label">Message *</label>
                    <textarea id="message" name="message" rows="6" class="form-textarea" placeholder="Tell me about your project, requirements, or how I can help..." required></textarea>
                    <div class="error-message" style="color: #ef4444; font-size: 0.875rem; margin-top: 0.25rem; display: none;"></div>
                </div>
                
                <div class="form-group">
                    <label for="timeline" class="form-label">Project Timeline</label>
                    <select id="timeline" name="timeline" class="form-select">
                        <option value="">Select timeline</option>
                        <option value="immediate">Immediate (ASAP)</option>
                        <option value="1-month">Within 1 month</option>
                        <option value="3-months">Within 3 months</option>
                        <option value="6-months">Within 6 months</option>
                        <option value="flexible">Flexible</option>
                    </select>
                </div>
                
                <button type="submit" class="submit-button">
                    <span class="submit-text">Send Message</span>
                    <span class="loading-text" style="display: none;">Sending...</span>
                </button>
            </form>

    .. container:: contact-card

        **Contact Information**

        Based in Bangalore, India, I'm available for projects worldwide. Let's discuss how we can work together.

        .. container:: contact-info-item

            .. container:: contact-icon
                📧

            .. container:: contact-details

                **Email**
                jimit.vyas@outlook.com

        .. container:: contact-info-item

            .. container:: contact-icon
                📞

            .. container:: contact-details

                **Phone**
                +91 8200500169

        .. container:: contact-info-item

            .. container:: contact-icon
                📍

            .. container:: contact-details

                **Location**
                Bangalore, India

        .. container:: contact-info-item

            .. container:: contact-icon
                ⏰

            .. container:: contact-details

                **Response Time**
                Within 24 hours

        **Professional Networks**

        .. container:: social-links

            .. raw:: html

                <a href="https://linkedin.com/in/jimit04" target="_blank" class="social-link" title="LinkedIn">
                    <svg style="width: 1.5rem; height: 1.5rem;" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                    </svg>
                </a>
                <a href="mailto:jimit.vyas@outlook.com" class="social-link" title="Email">
                    <svg style="width: 1.5rem; height: 1.5rem;" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.89 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                    </svg>
                </a>

        **Availability**

        .. container:: availability-grid

            .. container:: availability-item

                .. container:: availability-type
                    Project Consultation
                .. container:: availability-status
                    Available

            .. container:: availability-item

                .. container:: availability-type
                    Full-time Opportunities
                .. container:: availability-status
                    Open to discussion

            .. container:: availability-item

                .. container:: availability-type
                    Research Collaboration
                .. container:: availability-status
                    Actively seeking

            .. container:: availability-item

                .. container:: availability-type
                    Mentoring
                .. container:: availability-status
                    Available for junior engineers

Frequently Asked Questions
--------------------------

.. container:: faq-section

    .. container:: faq-item

        .. container:: faq-question
            What types of projects do you typically work on?

        .. container:: faq-answer
            I specialize in CAE process automation, structural FEA analysis, AI/ML integration for engineering workflows, 
            and simulation-driven design optimization across automotive, off-highway, and mining industries.

    .. container:: faq-item

        .. container:: faq-question
            Do you work remotely or on-site?

        .. container:: faq-answer
            I'm flexible with both arrangements. Based in Bangalore, I can work remotely for global projects or 
            be available for on-site consultations when needed. Many automation projects can be effectively managed remotely.

    .. container:: faq-item

        .. container:: faq-question
            What's your typical project timeline?

        .. container:: faq-answer
            Project timelines vary based on complexity. Automation scripts can take 2-4 weeks, while comprehensive 
            CAE workflow overhauls might take 2-3 months. I provide detailed timelines after initial consultation.

    .. container:: faq-item

        .. container:: faq-question
            Do you provide training for teams?

        .. container:: faq-answer
            Yes, I offer comprehensive training programs for teams on CAE automation, Python/TCL scripting, 
            and advanced simulation techniques. I also provide ongoing mentoring for junior engineers.

    .. container:: faq-item

        .. container:: faq-question
            What industries have you worked with?

        .. container:: faq-answer
            My experience spans automotive (TVS Motor, Norton Motorcycles), mining equipment (Metso:Outotec), 
            construction machinery (L&T Technology Services), and software development (InfoVision | VCollab).

Ready to Start Your Project?
----------------------------

Let's discuss how CAE automation and AI integration can transform your engineering workflows

* :doc:`View My Work <portfolio>`
* :doc:`Check Experience <experience>`

.. raw:: html

    <div class="notification" id="notification"></div>
    
    <script>
        // Enhanced contact form validation and submission
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('contact-form');
            const submitButton = form.querySelector('.submit-button');
            const submitText = form.querySelector('.submit-text');
            const loadingText = form.querySelector('.loading-text');
            const notification = document.getElementById('notification');
            
            // Real-time validation
            const inputs = form.querySelectorAll('.form-input, .form-select, .form-textarea');
            inputs.forEach(input => {
                input.addEventListener('blur', function() {
                    validateField(this);
                });
                
                input.addEventListener('input', function() {
                    if (this.classList.contains('error')) {
                        validateField(this);
                    }
                });
            });
            
            function validateField(field) {
                const value = field.value.trim();
                const fieldName = field.name;
                let isValid = true;
                let errorMessage = '';
                
                // Clear previous errors
                field.classList.remove('error');
                const errorDiv = field.parentNode.querySelector('.error-message');
                if (errorDiv) {
                    errorDiv.style.display = 'none';
                }
                
                // Validation rules
                if (field.hasAttribute('required') && !value) {
                    isValid = false;
                    errorMessage = 'This field is required';
                } else if (fieldName === 'email' && value) {
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailRegex.test(value)) {
                        isValid = false;
                        errorMessage = 'Please enter a valid email address';
                    }
                } else if (fieldName === 'message' && value && value.length < 10) {
                    isValid = false;
                    errorMessage = 'Message must be at least 10 characters long';
                }
                
                // Show error if invalid
                if (!isValid) {
                    field.classList.add('error');
                    if (errorDiv) {
                        errorDiv.textContent = errorMessage;
                        errorDiv.style.display = 'block';
                    }
                }
                
                return isValid;
            }
            
            function validateForm() {
                let isValid = true;
                inputs.forEach(input => {
                    if (!validateField(input)) {
                        isValid = false;
                    }
                });
                return isValid;
            }
            
            function showNotification(message, type = 'success') {
                notification.textContent = message;
                notification.className = `notification ${type} show`;
                
                setTimeout(() => {
                    notification.classList.remove('show');
                }, 5000);
            }
            
            function setLoading(loading) {
                if (loading) {
                    submitButton.disabled = true;
                    submitText.style.display = 'none';
                    loadingText.style.display = 'inline';
                } else {
                    submitButton.disabled = false;
                    submitText.style.display = 'inline';
                    loadingText.style.display = 'none';
                }
            }
            
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                if (!validateForm()) {
                    showNotification('Please correct the errors above', 'error');
                    return;
                }
                
                setLoading(true);
                
                // Simulate form submission
                setTimeout(() => {
                    setLoading(false);
                    showNotification('Thank you for your message! I will get back to you within 24 hours.', 'success');
                    form.reset();
                }, 2000);
            });
        });
    </script>