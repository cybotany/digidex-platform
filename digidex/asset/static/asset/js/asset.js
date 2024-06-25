document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.link-asset-category');
    const assetItemsList = document.querySelector('#asset-items-list .asset-item-collection');
    const noAssetsMessage = document.querySelector('#no-assets-message');
  
    function loadAssets(category) {
      fetch(`/api/${category}`)
        .then(response => response.json())
        .then(data => {
          assetItemsList.innerHTML = '';
          if (data.assets.length > 0) {
            data.assets.forEach(asset => {
              const assetCard = document.createElement('div');
              assetCard.className = 'asset-card';
              assetCard.innerHTML = `<div class="card-content">${asset.name}</div>`;
              assetItemsList.appendChild(assetCard);
            });
            noAssetsMessage.style.display = 'none';
          } else {
            noAssetsMessage.style.display = 'block';
          }
        })
        .catch(error => console.error('Error loading assets:', error));
    }
  
    tabs.forEach(tab => {
      tab.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default anchor behavior
        tabs.forEach(t => t.classList.remove('base--current'));
        tab.classList.add('base--current');
        const category = tab.getAttribute('data-category');
        loadAssets(category);
      });
    });
  
    // Load assets for the initial active tab
    const initialCategory = document.querySelector('.link-asset-category.base--current').getAttribute('data-category');
    loadAssets(initialCategory);
  });
  