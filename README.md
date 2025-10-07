# Jimit Vyas - Professional Website

A professional personal website built with Sphinx for a CAE & Automation Specialist with 9+ years of experience in structural FEA, process automation, and AI integration.

## 🚀 Features

- **Professional Design**: Modern, responsive design with sophisticated typography and color scheme
- **Interactive Elements**: 
  - Typewriter animation for dynamic text display
  - Interactive career timeline with expandable details
  - Skills visualization with radar chart
  - Contact form with real-time validation
- **Comprehensive Content**:
  - Professional experience timeline
  - Technical portfolio with project showcases
  - Skills and competencies visualization
  - Contact information and availability
- **Technical Excellence**:
  - Built with Sphinx documentation generator
  - Responsive design for all devices
  - SEO optimized structure
  - Fast loading and smooth animations

## 📁 Project Structure

```
├── docs/
│   └── source/
│       ├── _static/
│       │   └── css/
│       │       └── custom.css
│       ├── index.rst
│       ├── experience.rst
│       ├── portfolio.rst
│       ├── contact.rst
│       └── conf.py
├── .github/
│   └── workflows/
│       └── deploy.yml
├── requirements.txt
├── Makefile
├── .gitignore
└── README.md
```

## 🛠 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Local Development

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd personal-website
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Build the documentation**:
   ```bash
   make html
   ```

5. **View the website locally**:
   ```bash
   make livehtml
   ```
   The website will be available at `http://localhost:8000`

## 🚀 Deployment

### Automatic Deployment (GitHub Pages)

The website automatically deploys to GitHub Pages when you push to the `main` branch:

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Update website content"
   git push origin main
   ```

2. **GitHub Actions will automatically**:
   - Build the Sphinx documentation
   - Deploy to GitHub Pages
   - Update the live website

### Manual Deployment

To deploy manually:

```bash
make deploy
```

## 📖 Usage

### Building the Website

```bash
# Build HTML documentation
make html

# Build all formats (HTML, PDF, EPUB)
make all

# Clean build directory
make clean

# Check for broken links
make linkcheck
```

### Development Commands

```bash
# Start development server with auto-reload
make livehtml

# Run tests
make test

# Format code
make format

# Run linting
make lint
```

## 🎨 Customization

### Styling

The website uses custom CSS located in `docs/source/_static/css/custom.css`. You can modify:

- Color scheme by updating CSS variables
- Typography by changing font families
- Layout and spacing
- Animation effects

### Content

All content is written in reStructuredText (.rst) format:

- `index.rst`: Homepage content
- `experience.rst`: Professional experience timeline
- `portfolio.rst`: Projects and skills showcase
- `contact.rst`: Contact information and form

### Configuration

Update `docs/source/conf.py` to modify:

- Website title and metadata
- Theme settings
- Extensions and plugins
- Navigation structure

## 📱 Responsive Design

The website is fully responsive and optimized for:

- Desktop computers
- Tablets
- Mobile phones
- High-resolution displays

## 🔧 Technical Stack

- **Sphinx**: Documentation generator
- **Furo Theme**: Modern, responsive theme
- **reStructuredText**: Content markup language
- **CSS3**: Styling and animations
- **JavaScript**: Interactive elements
- **GitHub Pages**: Hosting platform

## 🎯 Content Sections

### 1. Homepage
- Professional introduction
- Core competencies
- Call-to-action buttons
- Statistics and achievements

### 2. Experience
- Interactive career timeline
- Detailed role descriptions
- Technical skills used
- Key achievements

### 3. Portfolio
- Featured projects
- Skills visualization
- Technology stack
- Impact metrics

### 4. Contact
- Professional contact form
- Contact information
- Social media links
- Availability status

## 🌟 Features in Detail

### Interactive Timeline
- Click to expand job details
- Smooth animations
- Responsive design
- Visual progression indicators

### Skills Visualization
- Radar chart for technical competencies
- Progress bars for skill levels
- Interactive hover effects
- Mobile-friendly design

### Contact Form
- Real-time validation
- Professional inquiry types
- Responsive layout
- Success/error notifications

### Animations
- Scroll-triggered animations
- Typewriter effect
- Hover interactions
- Loading states

## 📊 Performance

- Optimized for fast loading
- Minimal JavaScript usage
- Compressed images and assets
- Efficient CSS animations
- Mobile-first approach

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

For questions or support:

- **Email**: jimit.vyas@outlook.com
- **LinkedIn**: [linkedin.com/in/jimit04](https://linkedin.com/in/jimit04)
- **Location**: Bangalore, India

---

**Built with ❤️ using Sphinx and modern web technologies**