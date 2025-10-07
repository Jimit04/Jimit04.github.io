Professional Experience
=======================

.. raw:: html

    <style>
        .timeline {
            position: relative;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .timeline::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 4px;
            background: linear-gradient(to bottom, #64748b, #1a2332);
            transform: translateX(-50%);
        }
        
        .timeline-item {
            position: relative;
            margin-bottom: 4rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .timeline-item:hover {
            transform: scale(1.02);
        }
        
        .timeline-node {
            position: absolute;
            left: 50%;
            top: 2rem;
            width: 20px;
            height: 20px;
            background: #1a2332;
            border: 4px solid white;
            border-radius: 50%;
            transform: translateX(-50%);
            z-index: 10;
            transition: all 0.3s ease;
        }
        
        .timeline-item:hover .timeline-node {
            background: #64748b;
            transform: translateX(-50%) scale(1.2);
        }
        
        .timeline-content {
            background: white;
            border-radius: 1rem;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            width: 45%;
            border-left: 4px solid #1a2332;
        }
        
        .timeline-item:nth-child(odd) .timeline-content {
            margin-left: 55%;
        }
        
        .timeline-item:nth-child(even) .timeline-content {
            margin-right: 55%;
        }
        
        .timeline-item:hover .timeline-content {
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
            transform: translateY(-4px);
        }
        
        .timeline-details {
            display: none;
            margin-top: 1.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid #e5e7eb;
        }
        
        .timeline-item.active .timeline-details {
            display: block;
        }
        
        .achievement-badge {
            display: inline-block;
            background: linear-gradient(135deg, #1a2332, #64748b);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 2rem;
            font-size: 0.875rem;
            font-weight: 600;
            margin: 0.25rem;
        }
        
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        
        .tech-tag {
            background: rgba(100, 116, 139, 0.1);
            color: #64748b;
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.75rem;
            font-weight: 500;
        }
        
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        
        .skill-card {
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #1a2332;
            transition: all 0.3s ease;
        }
        
        .skill-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }
        
        .skill-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #f1f5f9;
        }
        
        .skill-name {
            font-weight: 500;
        }
        
        .skill-level {
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.875rem;
            font-weight: 600;
        }
        
        .level-expert {
            background: #dcfce7;
            color: #166534;
        }
        
        .level-advanced {
            background: #dbeafe;
            color: #1e40af;
        }
        
        .level-intermediate {
            background: #fef3c7;
            color: #92400e;
        }
        
        @media (max-width: 768px) {
            .timeline::before {
                left: 2rem;
            }
            
            .timeline-node {
                left: 2rem;
            }
            
            .timeline-content {
                width: calc(100% - 4rem);
                margin-left: 4rem !important;
                margin-right: 0 !important;
            }
        }
    </style>

Career Timeline
---------------

.. container:: timeline

    .. container:: timeline-item
        :onclick: "toggleDetails(this)"

        .. container:: timeline-node

        .. container:: timeline-content

            .. raw:: html

                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <div>
                        <h3 style="margin: 0; font-size: 1.5rem; font-weight: bold;">Deputy Manager</h3>
                        <p style="margin: 0; color: #3b82f6; font-weight: 600;">TVS Motor Company | Norton Motorcycles</p>
                    </div>
                    <div style="text-align: right;">
                        <span class="achievement-badge">Current</span>
                        <p style="margin: 0.5rem 0 0 0; color: #6b7280; font-size: 0.875rem;">Mar 2024 - Present</p>
                    </div>
                </div>

            Leading structural FEA activities for Super Premium NPD projects, ensuring durability and performance 
            through simulation-driven design validation.

            .. container:: timeline-details

                **Key Achievements:**

                * ✓ Developed custom automation tools achieving 60%+ reduction in turnaround time
                * ✓ Streamlined repetitive analysis workflows for global project reuse
                * ✓ Mentoring junior engineers on advanced simulation techniques
                * ✓ Cross-functional collaboration with design, testing, and product teams

                .. container:: tech-stack

                    .. container:: tech-tag Python
                    .. container:: tech-tag TCL
                    .. container:: tech-tag ANSYS
                    .. container:: tech-tag FEA
                    .. container:: tech-tag Team Leadership
                    .. container:: tech-tag Process Automation

    .. container:: timeline-item
        :onclick: "toggleDetails(this)"

        .. container:: timeline-node

        .. container:: timeline-content

            .. raw:: html

                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <div>
                        <h3 style="margin: 0; font-size: 1.5rem; font-weight: bold;">Senior Software Engineer</h3>
                        <p style="margin: 0; color: #3b82f6; font-weight: 600;">InfoVision | VCollab</p>
                    </div>
                    <div style="text-align: right;">
                        <span class="achievement-badge">2 Years</span>
                        <p style="margin: 0.5rem 0 0 0; color: #6b7280; font-size: 0.875rem;">May 2022 - Mar 2024</p>
                    </div>
                </div>

            Developed Python-based automation solutions with VCollab APIs to generate 3D digital CAE reports, 
            cutting manual post-processing effort significantly.

            .. container:: timeline-details

                **Key Achievements:**

                * ✓ Integrated DoE-driven AI/ML techniques for accelerated post-processing
                * ✓ Built custom tools for client-specific reporting workflows
                * ✓ Standardized batch workflows for improved speed and accuracy
                * ✓ Partnered with product managers and customers for tailored solutions

                .. container:: tech-stack

                    .. container:: tech-tag Python
                    .. container:: tech-tag VCollab APIs
                    .. container:: tech-tag AI/ML
                    .. container:: tech-tag DoE
                    .. container:: tech-tag Automation
                    .. container:: tech-tag 3D Reporting

    .. container:: timeline-item
        :onclick: "toggleDetails(this)"

        .. container:: timeline-node

        .. container:: timeline-content

            .. raw:: html

                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <div>
                        <h3 style="margin: 0; font-size: 1.5rem; font-weight: bold;">Structural Analyst</h3>
                        <p style="margin: 0; color: #3b82f6; font-weight: 600;">Metso:Outotec</p>
                    </div>
                    <div style="text-align: right;">
                        <span class="achievement-badge">2 Years</span>
                        <p style="margin: 0.5rem 0 0 0; color: #6b7280; font-size: 0.875rem;">Aug 2020 - May 2022</p>
                    </div>
                </div>

            Led a team of four engineers delivering structural simulations for crushers, screens, hoppers, and conveyors 
            in the mining and construction industry.

            .. container:: timeline-details

                **Key Achievements:**

                * ✓ Performed integrated analytical, MBD, DEM, and FEA studies
                * ✓ Correlated FEA/MBD results with physical test data
                * ✓ Automated repetitive ANSYS WB tasks with Python scripting
                * ✓ Developed scripts for post-processing test data from sensors

                .. container:: tech-stack

                    .. container:: tech-tag ANSYS
                    .. container:: tech-tag MBD
                    .. container:: tech-tag DEM
                    .. container:: tech-tag Python
                    .. container:: tech-tag Team Leadership
                    .. container:: tech-tag Test Correlation

    .. container:: timeline-item
        :onclick: "toggleDetails(this)"

        .. container:: timeline-node

        .. container:: timeline-content

            .. raw:: html

                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <div>
                        <h3 style="margin: 0; font-size: 1.5rem; font-weight: bold;">CAE Engineer</h3>
                        <p style="margin: 0; color: #3b82f6; font-weight: 600;">L&T Technology Services</p>
                    </div>
                    <div style="text-align: right;">
                        <span class="achievement-badge">2.5 Years</span>
                        <p style="margin: 0.5rem 0 0 0; color: #6b7280; font-size: 0.875rem;">Dec 2017 - Jun 2020</p>
                    </div>
                </div>

            Executed FEA simulations for wreckers, MEWPs, and tipper/mining trucks with focus on 
            simulation-driven design iterations.

            .. container:: timeline-details

                **Key Achievements:**

                * ✓ Developed CGAP-based contact simplification technique
                * ✓ Reduced nonlinear solution time by 90% for design iterations
                * ✓ Automated meshing and model setup via TCL in HyperMesh
                * ✓ Improved efficiency and consistency across projects

                .. container:: tech-stack

                    .. container:: tech-tag HyperMesh
                    .. container:: tech-tag TCL
                    .. container:: tech-tag ANSYS
                    .. container:: tech-tag CGAP
                    .. container:: tech-tag Design Optimization
                    .. container:: tech-tag Automation

    .. container:: timeline-item
        :onclick: "toggleDetails(this)"

        .. container:: timeline-node

        .. container:: timeline-content

            .. raw:: html

                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                    <div>
                        <h3 style="margin: 0; font-size: 1.5rem; font-weight: bold;">Research Engineer</h3>
                        <p style="margin: 0; color: #3b82f6; font-weight: 600;">Freelancer</p>
                    </div>
                    <div style="text-align: right;">
                        <span class="achievement-badge">2+ Years</span>
                        <p style="margin: 0.5rem 0 0 0; color: #6b7280; font-size: 0.875rem;">Aug 2015 - Nov 2017</p>
                    </div>
                </div>

            Designed and developed innovative robotic systems and sensor technologies for industrial applications.

            .. container:: timeline-details

                **Key Achievements:**

                * ✓ Designed 3-DOF robotic arm (30kg payload, 1m reach)
                * ✓ Developed 3-axis force sensor using strain gauges
                * ✓ Created robotic joint feedback systems
                * ✓ Specialized in packaging applications

                .. container:: tech-stack

                    .. container:: tech-tag Robotics
                    .. container:: tech-tag Strain Gauges
                    .. container:: tech-tag Sensor Design
                    .. container:: tech-tag Mechanical Design
                    .. container:: tech-tag Control Systems
                    .. container:: tech-tag Packaging Automation

Technical Expertise
-------------------

.. container:: skills-grid

    .. container:: skill-card

        **CAE Tools**

        .. container:: skill-item

            .. container:: skill-name ANSYS
            .. container:: skill-level level-expert Expert

        .. container:: skill-item

            .. container:: skill-name HyperMesh
            .. container:: skill-level level-advanced Advanced

        .. container:: skill-item

            .. container:: skill-name ABAQUS
            .. container:: skill-level level-advanced Advanced

        .. container:: skill-item

            .. container:: skill-name NASTRAN
            .. container:: skill-level level-intermediate Intermediate

    .. container:: skill-card

        **Programming Languages**

        .. container:: skill-item

            .. container:: skill-name Python
            .. container:: skill-level level-expert Expert

        .. container:: skill-item

            .. container:: skill-name TCL
            .. container:: skill-level level-advanced Advanced

        .. container:: skill-item

            .. container:: skill-name MATLAB
            .. container:: skill-level level-intermediate Intermediate

        .. container:: skill-item

            .. container:: skill-name C++
            .. container:: skill-level level-intermediate Intermediate

    .. container:: skill-card

        **Analysis Types**

        .. container:: skill-item

            .. container:: skill-name Structural FEA
            .. container:: skill-level level-expert Expert

        .. container:: skill-item

            .. container:: skill-name MBD
            .. container:: skill-level level-advanced Advanced

        .. container:: skill-item

            .. container:: skill-name DEM
            .. container:: skill-level level-advanced Advanced

        .. container:: skill-item

            .. container:: skill-name Fatigue Analysis
            .. container:: skill-level level-advanced Advanced

    .. container:: skill-card

        **Specializations**

        .. container:: skill-item

            .. container:: skill-name Process Automation
            .. container:: skill-level level-expert Expert

        .. container:: skill-item

            .. container:: skill-name AI/ML Integration
            .. container:: skill-level level-advanced Advanced

        .. container:: skill-item

            .. container:: skill-name Team Leadership
            .. container:: skill-level level-advanced Advanced

        .. container:: skill-item

            .. container:: skill-name Design Optimization
            .. container:: skill-level level-advanced Advanced

Let's Build the Future Together
-------------------------------

Ready to leverage my expertise in CAE automation and AI integration for your next project?

* :doc:`View My Portfolio <portfolio>`
* :doc:`Start a Conversation <contact>`

.. raw:: html

    <script>
        function toggleDetails(element) {
            const details = element.querySelector('.timeline-details');
            const isActive = element.classList.contains('active');
            
            // Close all other details
            document.querySelectorAll('.timeline-item.active').forEach(item => {
                if (item !== element) {
                    item.classList.remove('active');
                }
            });
            
            // Toggle current item
            if (isActive) {
                element.classList.remove('active');
            } else {
                element.classList.add('active');
            }
        }
        
        // Add smooth scrolling and animation effects
        document.addEventListener('DOMContentLoaded', function() {
            // Animate timeline items on scroll
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, { threshold: 0.1 });
            
            document.querySelectorAll('.timeline-item').forEach(item => {
                item.style.opacity = '0';
                item.style.transform = 'translateY(20px)';
                item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                observer.observe(item);
            });
        });
    </script>