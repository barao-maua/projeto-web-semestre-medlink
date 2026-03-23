// Escalona pequenos atrasos para sugerir progressao visual entre os cards.
document.querySelectorAll(".timeline-card").forEach((card, index) => {
  card.style.transitionDelay = `${index * 80}ms`;
});
