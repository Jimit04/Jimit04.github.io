document.getElementById('contact-form').addEventListener('submit', function (e) {
  e.preventDefault();
  // basic validation
  const required = this.querySelectorAll('[required]');
  let ok = true;
  required.forEach(r => {
    if (!r.value.trim()) (ok = false), r.classList.add('error');
    else r.classList.remove('error');
  });
  if (!ok) return alert('Please fill all required fields.');
  // mock submit
  const btn = this.querySelector('.submit-button');
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner"></span> Sending…';
  setTimeout(() => {
    btn.disabled = false;
    btn.textContent = 'Send Message';
    alert('Thank you! I will reply within 24 h.');
    this.reset();
  }, 1500);
});