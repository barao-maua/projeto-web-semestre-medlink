// Animação dos números das estatísticas
function animateCounter(element, target) {
  let current = 0;
  const increment = target / 60;
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    element.textContent = Math.floor(current) + (element.dataset.suffix || '');
  }, 16);
}

document.addEventListener('DOMContentLoaded', () => {
  // Contador animado nas estatísticas
  const counters = document.querySelectorAll('[data-counter]');
  counters.forEach(el => {
    const target = parseInt(el.dataset.counter);
    animateCounter(el, target);
  });
});