document.querySelectorAll('.kingdom-link').forEach(item => {
    item.addEventListener('click', function(e) {
      e.preventDefault();
      const kingdomId = this.getAttribute('data-kingdom-id');
      fetch(`/path-to-kingdom-details-view/${kingdomId}/`)
        .then(response => response.json()) // or .text() if you're returning HTML
        .then(data => {
          // Update the page content with the data
          // For example, if returning HTML:
          document.querySelector('#kingdom-details-container').innerHTML = data;
        });
    });
  });
  