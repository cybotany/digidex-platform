document.addEventListener("DOMContentLoaded", function() {
    const speciesInput = document.getElementById('id_species');
    const taxonInput = document.getElementById('id_taxon_id');
    const suggestionsContainer = document.createElement('div');
    suggestionsContainer.classList.add('suggestions');
    document.body.appendChild(suggestionsContainer);

    speciesInput.addEventListener('input', function() {
        const query = speciesInput.value;
        if (query.length > 2) {
            fetch(`/species-autocomplete/?query=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsContainer.innerHTML = '';
                    data.forEach(item => {
                        const suggestionItem = document.createElement('div');
                        suggestionItem.classList.add('suggestion-item');
                        suggestionItem.textContent = item.name;
                        suggestionItem.addEventListener('click', () => {
                            speciesInput.value = item.name;
                            taxonInput.value = item.taxon_id;
                            suggestionsContainer.innerHTML = '';
                        });
                        suggestionsContainer.appendChild(suggestionItem);
                    });
                });
        } else {
            suggestionsContainer.innerHTML = '';
        }
    });

    document.addEventListener('click', (event) => {
        if (!suggestionsContainer.contains(event.target) && event.target !== speciesInput) {
            suggestionsContainer.innerHTML = '';
        }
    });
});