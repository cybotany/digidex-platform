function loadCategories() {
    fetch('/api/inventory/')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('asset-categories');
            container.innerHTML = `<a href="#" class="link-asset-category base-inline-block" onclick="loadAssets('party')">
                <div class="text-asset-category">Party</div>
            </a>`;
            data.forEach(group => {
                container.innerHTML += `<a href="#" class="link-asset-category base-inline-block" onclick="loadAssets('${group.name}')">
                    <div class="text-asset-category">${group.name}</div>
                </a>`;
            });
        });
}

function loadAssets(category) {
    fetch(`/api/assets/?category=${category}`)
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