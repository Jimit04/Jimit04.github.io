Technical Portfolio
===================

.. raw:: html

    <style>
        .portfolio-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }
        
        .project-card {
            background: white;
            border-radius: 1rem;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #1a2332;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #1a2332, #64748b);
        }
        
        .project-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }
        
        .project-icon {
            width: 4rem;
            height: 4rem;
            background: #f1f5f9;
            border-radius: 0.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }
        
        .tech-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1rem 0;
        }
        
        .tech-badge {
            background: linear-gradient(135deg, #1a2332, #64748b);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 1rem;
            font-size: 0.75rem;
            font-weight: 500;
        }
        
        .project-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px solid #f1f5f9;
        }
        
        .impact-metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        
        .metric-card {
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            border-left: 4px solid #1a2332;
            transition: all 0.3s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }
        
        .metric-number {
            font-size: 3rem;
            font-weight: 700;
            color: #1a2332;
            margin-bottom: 0.5rem;
        }
        
        .metric-label {
            color: #64748b;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        
        .metric-description {
            color: #6b7280;
            font-size: 0.875rem;
        }
        
        .tech-categories {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        
        .tech-category {
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #1a2332;
            transition: all 0.3s ease;
        }
        
        .tech-category:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }
        
        .tech-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .tech-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 1rem;
            background: #f8fafc;
            border-radius: 0.5rem;
        }
        
        .tech-icon {
            width: 3rem;
            height: 3rem;
            background: #e2e8f0;
            border-radius: 0.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 0.5rem;
            font-weight: bold;
            font-size: 0.875rem;
        }
        
        .tech-name {
            font-weight: 600;
            margin-bottom: 0.25rem;
        }
        
        .tech-level {
            font-size: 0.75rem;
            padding: 0.25rem 0.5rem;
            border-radius: 1rem;
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
            .portfolio-grid {
                grid-template-columns: 1fr;
            }
            
            .tech-grid {
                grid-template-columns: 1fr;
            }
            
            .impact-metrics {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        @media (max-width: 480px) {
            .impact-metrics {
                grid-template-columns: 1fr;
            }
        }
    </style>

Featured Projects
-----------------

.. container:: portfolio-grid

    .. container:: project-card

        .. container:: project-icon
            ⚙️

        **CAE Workflow Automation**
        
        Developed comprehensive Python and TCL automation suite for CAE processes, achieving 60%+ reduction 
        in analysis turnaround time across multiple projects.
        
        .. container:: tech-badges

            .. container:: tech-badge Python
            .. container:: tech-badge TCL
            .. container:: tech-badge ANSYS
            .. container:: tech-badge HyperMesh

        .. container:: project-footer

            **TVS Motor Company**
            **60% Efficiency Gain**

    .. container:: project-card

        .. container:: project-icon
            🤖

        **AI-Driven Post-Processing**
        
        Integrated Design of Experiments with AI/ML techniques to accelerate post-processing and extract 
        insights from large simulation datasets.
        
        .. container:: tech-badges

            .. container:: tech-badge Python
            .. container:: tech-badge Machine Learning
            .. container:: tech-badge DoE
            .. container:: tech-badge VCollab APIs

        .. container:: project-footer

            **InfoVision | VCollab**
            **75% Time Savings**

    .. container:: project-card

        .. container:: project-icon
            📊

        **3D Digital Reporting System**
        
        Built custom tools and interfaces for generating 3D digital CAE reports, delivering client-specific 
        reporting workflows and enhanced functionality.
        
        .. container:: tech-badges

            .. container:: tech-badge Python
            .. container:: tech-badge 3D Visualization
            .. container:: tech-badge API Integration
            .. container:: tech-badge Web Development

        .. container:: project-footer

            **InfoVision | VCollab**
            **90% Manual Reduction**

    .. container:: project-card

        .. container:: project-icon
            🔧

        **Contact Optimization Technique**
        
        Developed and implemented CGAP-based contact simplification technique, reducing nonlinear solution 
        time by 90% for simulation-driven design iterations.
        
        .. container:: tech-badges

            .. container:: tech-badge ANSYS
            .. container:: tech-badge CGAP
            .. container:: tech-badge Nonlinear Analysis
            .. container:: tech-badge Optimization

        .. container:: project-footer

            **L&T Technology Services**
            **90% Time Reduction**

    .. container:: project-card

        .. container:: project-icon
            🦾

        **Robotic Arm Design**
        
        Designed a 3-DOF robotic arm with 30kg payload capacity and 1m reach for packaging applications, 
        including development of force sensor feedback systems.
        
        .. container:: tech-badges

            .. container:: tech-badge Mechanical Design
            .. container:: tech-badge Strain Gauges
            .. container:: tech-badge Control Systems
            .. container:: tech-badge Robotics

        .. container:: project-footer

            **Freelancer**
            **Innovation Award**

    .. container:: project-card

        .. container:: project-icon
            🏗️

        **Integrated Simulation Platform**
        
        Led team delivering integrated analytical, MBD, DEM, and FEA studies for load and operational 
        analysis of mining equipment systems.
        
        .. container:: tech-badges

            .. container:: tech-badge Team Leadership
            .. container:: tech-badge MBD
            .. container:: tech-badge DEM
            .. container:: tech-badge FEA

        .. container:: project-footer

            **Metso:Outotec**
            **Team Excellence**

Impact & Results
----------------

.. container:: impact-metrics

    .. container:: metric-card

        .. container:: metric-number
            60%

        .. container:: metric-label
            Process Efficiency

        .. container:: metric-description
            Average improvement across automation projects

    .. container:: metric-card

        .. container:: metric-number
            90%

        .. container:: metric-label
            Time Reduction

        .. container:: metric-description
            Nonlinear solution optimization

    .. container:: metric-card

        .. container:: metric-number
            75%

        .. container:: metric-label
            Manual Effort Saved

        .. container:: metric-description
            Post-processing automation

    .. container:: metric-card

        .. container:: metric-number
            4

        .. container:: metric-label
            Teams Led

        .. container:: metric-description
            Cross-functional engineering teams

Technologies & Tools
--------------------

.. container:: tech-categories

    .. container:: tech-category

        **CAE Software**

        .. container:: tech-grid

            .. container:: tech-item

                .. container:: tech-icon
                    **ANSYS**

                .. container:: tech-name ANSYS
                .. container:: tech-level level-expert Expert

            .. container:: tech-item

                .. container:: tech-icon
                    **HM**

                .. container:: tech-name HyperMesh
                .. container:: tech-level level-advanced Advanced

            .. container:: tech-item

                .. container:: tech-icon
                    **ABQ**

                .. container:: tech-name ABAQUS
                .. container:: tech-level level-advanced Advanced

            .. container:: tech-item

                .. container:: tech-icon
                    **NAS**

                .. container:: tech-name NASTRAN
                .. container:: tech-level level-intermediate Intermediate

    .. container:: tech-category

        **Programming Languages**

        .. container:: tech-grid

            .. container:: tech-item

                .. container:: tech-icon
                    **PY**

                .. container:: tech-name Python
                .. container:: tech-level level-expert Expert

            .. container:: tech-item

                .. container:: tech-icon
                    **TCL**

                .. container:: tech-name TCL
                .. container:: tech-level level-advanced Advanced

            .. container:: tech-item

                .. container:: tech-icon
                    **MAT**

                .. container:: tech-name MATLAB
                .. container:: tech-level level-intermediate Intermediate

            .. container:: tech-item

                .. container:: tech-icon
                    **C++**

                .. container:: tech-name C++
                .. container:: tech-level level-intermediate Intermediate

    .. container:: tech-category

        **Analysis Types**

        .. container:: tech-grid

            .. container:: tech-item

                .. container:: tech-icon
                    **FEA**

                .. container:: tech-name Structural FEA
                .. container:: tech-level level-expert Expert

            .. container:: tech-item

                .. container:: tech-icon
                    **MBD**

                .. container:: tech-name MBD
                .. container:: tech-level level-advanced Advanced

            .. container:: tech-item

                .. container:: tech-icon
                    **DEM**

                .. container:: tech-name DEM
                .. container:: tech-level level-advanced Advanced

            .. container:: tech-item

                .. container:: tech-icon
                    **FAT**

                .. container:: tech-name Fatigue Analysis
                .. container:: tech-level level-advanced Advanced

Ready to Innovate?
------------------

Let's discuss how my technical expertise can drive your next engineering project forward

* :doc:`Get In Touch <contact>`
* :doc:`View Experience <experience>`

.. raw:: html

    <script>
        // Add animation effects
        document.addEventListener('DOMContentLoaded', function() {
            // Animate project cards on scroll
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            }, { threshold: 0.1 });
            
            document.querySelectorAll('.project-card, .metric-card, .tech-category').forEach(item => {
                item.style.opacity = '0';
                item.style.transform = 'translateY(20px)';
                item.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                observer.observe(item);
            });
            
            // Animate metric numbers
            const animateNumbers = () => {
                const numbers = document.querySelectorAll('.metric-number');
                numbers.forEach(number => {
                    const finalValue = number.textContent;
                    if (finalValue.includes('%')) {
                        const numValue = parseInt(finalValue);
                        let currentValue = 0;
                        const increment = numValue / 50;
                        const timer = setInterval(() => {
                            currentValue += increment;
                            if (currentValue >= numValue) {
                                currentValue = numValue;
                                clearInterval(timer);
                            }
                            number.textContent = Math.floor(currentValue) + '%';
                        }, 50);
                    }
                });
            };
            
            // Trigger number animation when metrics section is visible
            const metricsObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        animateNumbers();
                        metricsObserver.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.5 });
            
            const metricsSection = document.querySelector('.impact-metrics');
            if (metricsSection) {
                metricsObserver.observe(metricsSection);
            }
        });
    </script>