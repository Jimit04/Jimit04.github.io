// Universal helpers
document.addEventListener('DOMContentLoaded', () => {
  // Typewriter on hero
  const phrases = [
    'CAE & Automation Specialist',
    'Structural FEA Expert',
    'Python & TCL Developer',
    'AI/ML Integration Engineer',
    'Process Automation Leader'
  ];
  let i = 0, j = 0, deleting = false;
  const el = document.getElementById('typewriter-text');
  if (!el) return;
  function loop() {
    const curr = phrases[i];
    el.textContent = deleting ? curr.substring(0, j--) : curr.substring(0, ++j);
    if (!deleting && j === curr.length) deleting = true, setTimeout(loop, 2000);
    else if (deleting && j === 0) { deleting = false; i = (i + 1) % phrases.length; setTimeout(loop, 500); }
    else setTimeout(loop, deleting ? 50 : 100);
  }
  setTimeout(loop, 1000);
});