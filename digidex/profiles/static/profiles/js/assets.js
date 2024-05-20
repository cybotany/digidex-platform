document.addEventListener('DOMContentLoaded', function() {
  loadCategories();
});

function loadCategories() {
  fetch('/api/inventory-groups/')
      .then(response => response.json())
      .then(data => {
          const container = document.getElementById('asset-categories-list');
          container.innerHTML = `<a href="#" class="link-asset-category base-inline-block" onclick="loadAssets('party')">
              <div class="text-asset-category">Party</div>
          </a>`;
          data.forEach(group => {
              container.innerHTML += `<a href="#" class="link-asset-category base-inline-block" onclick="loadAssets('${group.name}')">
                  <div class="text-asset-category">${group.name}</div>
              </a>`;
          });
          loadAssets('party');  // Load assets for the 'party' category by default
      });
}

function loadAssets(category) {
  fetch(`/api/assets/${category}/`)
      .then(response => response.json())
      .then(data => {
          const container = document.getElementById('asset-items-list');
          container.innerHTML = '';
          if (data.length > 0) {
              data.forEach(asset => {
                  container.innerHTML += `
                      <div role="listitem" class="asset-item base-dyn-item">
                          <div class="block-icon-asset-item">
                              <img src="${asset.icon_url}" alt="" class="icon-asset-item">
                          </div>
                          <a href="#" class="link-asset-item base-inline-block">
                              <h3 class="heading-asset-item">${asset.name}</h3>
                          </a>
                          <p class="paragraph-description">${asset.description}</p>
                          <div class="subtitle-asset-item">${asset.subtitle}</div>
                          <a href="#" class="button base-button">View Details</a>
                      </div>`;
              });
          } else {
              container.innerHTML = `<div class="empty-state base-dyn-empty">
                  <div class="text-empty">No items found.</div>
              </div>`;
          }
      });
}