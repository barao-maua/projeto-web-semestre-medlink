// Função que anima um número de 0 até o valor alvo
// element → o elemento HTML que contém o número
// target → o número final que queremos mostrar (ex: 500, 10000)
function animateCounter(element, target) {
  let current = 0;           // começa do zero
  const increment = target / 60; // divide o total em 60 passos (equivale a ~1 segundo a 60fps)

  // setInterval → executa uma função repetidamente em um intervalo de tempo
  const timer = setInterval(() => {
    current += increment; // soma o incremento a cada execução

    // Se já chegou ou passou do valor alvo, para a animação
    if (current >= target) {
      current = target;      // garante que termina no valor exato
      clearInterval(timer);  // para o setInterval
    }

    // Atualiza o texto do elemento com o valor atual arredondado
    // Math.floor → arredonda para baixo (ex: 499.7 → 499)
    // element.dataset.suffix → pega o valor do atributo data-suffix do HTML ("+", "%")
    // || '' → se não tiver suffix, usa string vazia
    element.textContent = Math.floor(current) + (element.dataset.suffix || '');

  }, 16); // 16ms entre cada execução ≈ 60 vezes por segundo (60fps)
}

// DOMContentLoaded → espera o HTML carregar completamente antes de executar o código
document.addEventListener('DOMContentLoaded', () => {

  // querySelectorAll → busca TODOS os elementos que têm o atributo data-counter no HTML
  // ex: <p data-counter="500" data-suffix="+">
  const counters = document.querySelectorAll('[data-counter]');

  // forEach → percorre cada elemento encontrado e chama animateCounter
  counters.forEach(el => {
    const target = parseInt(el.dataset.counter); // pega o valor de data-counter e converte para número inteiro
    animateCounter(el, target); // inicia a animação desse elemento
  });

});