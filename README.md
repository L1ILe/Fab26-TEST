# Fab Academy 2026 Documentation Website

A modern, responsive documentation website for Fab Academy 2026 with dynamic interactions.

## Features

- **Modern Dark Theme**: Inspired by mixlab.top design
- **Klein Blue Accents**: Using #002FA7 for typography and UI elements
- **Dynamic Interactions**: 
  - Particle animations
  - Card hover effects with 3D tilt
  - Smooth scroll animations
  - Ripple effects on buttons
- **Responsive Design**: Works on desktop, tablet, and mobile
- **20 Weekly Assignments**: Complete navigation structure

## Pages

- `index.html` - Home page with hero section and previews
- `dailywork.html` - All 20 weekly assignments with status indicators
- `finalproject.html` - Final project documentation
- `aboutme.html` - Personal introduction and skills
- `weeks/week1-20.html` - Individual week documentation pages

## Design Specifications

- **Font**: Arial
- **Primary Color**: Klein Blue (#002FA7)
- **Background**: Dark gradient (inspired by mixlab.top)
- **Animations**: CSS transitions and JavaScript interactions

## Local Development

To run locally:

```bash
cd Fab26-TEST
python3 -m http.server 8080
```

Then open http://localhost:8080 in your browser.

## Structure

```
Fab26-TEST/
├── index.html
├── dailywork.html
├── finalproject.html
├── aboutme.html
├── style.css
├── script.js
├── README.md
└── weeks/
    ├── week1.html
    ├── week2.html
    ├── ...
    └── week20.html
```

## Customization

1. Update personal information in `aboutme.html`
2. Add your final project details in `finalproject.html`
3. Document each week's work in `weeks/weekX.html`
4. Add images to a new `images/` folder and reference them in your HTML

## License

Created for Fab Academy 2026 documentation purposes.
