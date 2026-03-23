const searchInput = document.querySelector("#especialidade-search");
const filterButtons = document.querySelectorAll(".filtro-btn");
const cards = document.querySelectorAll(".especialidade-card");
const statusText = document.querySelector("#especialidade-status");
const emptyState = document.querySelector("#especialidade-vazio");

// Só ativa os filtros quando todos os elementos esperados existem na página.
if (searchInput && filterButtons.length && cards.length && statusText && emptyState) {
  let activeFilter = "todas";

  // Recalcula a visibilidade dos cards com base na categoria ativa e na busca.
  const renderCards = () => {
    const query = searchInput.value.trim().toLowerCase();
    let visibleCount = 0;

    cards.forEach((card) => {
      // Os dados para busca e categoria ficam no próprio HTML via data attributes.
      const categories = (card.dataset.category || "").toLowerCase();
      const searchableText = (card.dataset.search || "").toLowerCase();
      const matchesFilter = activeFilter === "todas" || categories.includes(activeFilter);
      const matchesQuery = !query || searchableText.includes(query);
      const isVisible = matchesFilter && matchesQuery;

      card.classList.toggle("hidden", !isVisible);

      if (isVisible) {
        visibleCount += 1;
      }
    });

    emptyState.classList.toggle("hidden", visibleCount > 0);

    // Atualiza a mensagem de apoio para refletir o filtro atual.
    if (activeFilter === "todas") {
      statusText.textContent = query
        ? `Mostrando ${visibleCount} especialidade(s) para "${query}"`
        : "Exibindo todas as especialidades";
      return;
    }

    statusText.textContent = query
      ? `Mostrando ${visibleCount} resultado(s) em ${activeFilter} para "${query}"`
      : `Exibindo especialidades da categoria ${activeFilter}`;
  };

  // Troca o estilo do botão ativo e dispara nova filtragem.
  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      activeFilter = button.dataset.filter || "todas";

      filterButtons.forEach((item) => {
        item.classList.remove("btn-primary");
        item.classList.add("btn-outline");
      });

      button.classList.remove("btn-outline");
      button.classList.add("btn-primary");

      renderCards();
    });
  });

  // Mantem a grade responsiva enquanto o usuário digita.
  searchInput.addEventListener("input", renderCards);
  renderCards();
}
