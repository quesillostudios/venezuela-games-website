const searchQuery = document.getElementById('search-query');
const autocompleteResults = document.getElementById('autocomplete-results');

async function search(query) {
    if (query.trim().length > 2) {
        const response = await fetch(`/search_videogames_ajax/?query=${query}`);
        const data = await response.json();

        autocompleteResults.innerHTML = '';

        if (data.length > 0) {
            data.forEach(game => {
                const item = document.createElement('div');
                item.classList.add('autocomplete-item');
                item.textContent = game.name;
                item.onclick = () => {
                    searchQuery.value = game.name;
                    autocompleteResults.innerHTML = '';
                };
                autocompleteResults.appendChild(item);
            });
            autocompleteResults.style.display = 'block';
        } else {
            autocompleteResults.innerHTML = '<div class="autocomplete-item">No se encontraron resultados</div>';
            autocompleteResults.style.display = 'block';
        }
    } else {
        autocompleteResults.innerHTML = '';
        autocompleteResults.style.display = 'none';
    }
}

searchQuery.addEventListener('input', function() {
    const query = searchQuery.value;
    search(query);
});