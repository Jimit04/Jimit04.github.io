// Animate numbers when metrics visible
const observer = new IntersectionObserver((es) => {
  es.forEach(e => {
    if (!e.isIntersecting) return;
    const numEl = e.target.querySelector('.metric-number');
    const final = parseInt(numEl.textContent);
    let curr = 0;
    const inc = final / 50;
    const t = setInterval(() => {
      curr += inc;
      if (curr >= final) { curr = final; clearInterval(t); }
      numEl.textContent = Math.floor(curr) + '%';
    }, 50);
    observer.unobserve(e.target);
  });
}, { threshold: 0.5 });
document.querySelectorAll('.metric-card').forEach(c => observer.observe(c));