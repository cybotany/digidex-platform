document.addEventListener('DOMContentLoaded', function() {
  // Function to show selected inventory content and hide others
  function showInventoryContent(inventoryId) {
    fetch(`/api/inventories/${inventoryId}/`)
      .then(response => response.json())
      .then(data => {
        const contentWrapper = document.querySelector('.asset-item-collection.base-dyn-items');
        contentWrapper.innerHTML = '';  // Clear existing content

        data.asset_items.forEach(asset => {
          const assetItem = `
            <div role="listitem" class="base-dyn-item">
              <div class="asset-item">
                <div class="block-icon-asset-item">
                  <img src="{% static 'images/google/tree.svg' %}" alt="" loading="eager" class="icon-asset-item">
                </div>
                <a href="${asset.url}" class="link-asset-item base-inline-block">
                  <h3 class="heading-asset-item">${asset.name}</h3>
                </a>
                <div class="block-price">
                  <div class="text-price">${asset.new_price}</div>
                  <div class="compare-at-price">${asset.original_price}</div>
                </div>
                <p class="paragraph-description">${asset.description}</p>
                <div class="subtitle-asset-item">Features<br></div>
                <div class="block-features-asset-item">
                  ${asset.features.map(feature => `
                    <div class="features-asset-item">
                      <img src="{% static 'images/bx/check-green.svg' %}" loading="eager" alt="" class="icon-features-asset-item">
                      <h6 class="heading-features-asset-item">${feature}</h6>
                    </div>
                  `).join('')}
                </div>
                <a href="${asset.url}" class="button base-button">View Asset</a>
              </div>
            </div>
          `;
          contentWrapper.innerHTML += assetItem;
        });
      })
      .catch(error => console.error('Error fetching inventory data:', error));
  }

  // Add event listeners to inventory buttons
  document.querySelectorAll('.block-assets .link-asset').forEach(button => {
    button.addEventListener('click', function(event) {
      event.preventDefault();
      const inventoryId = this.getAttribute('data-inventory-id');
      showInventoryContent(inventoryId);
    });
  });

  // Show the first inventory by default
  const firstInventoryButton = document.querySelector('.block-assets .link-asset');
  if (firstInventoryButton) {
    showInventoryContent(firstInventoryButton.getAttribute('data-inventory-id'));
  }
});