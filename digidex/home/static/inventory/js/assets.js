document.addEventListener("DOMContentLoaded", function() {
  fetchAssets();

  function fetchAssets() {
    fetch('/api/v2/assets/')
      .then(response => response.json())
      .then(data => {
        renderAssets(data);
      })
      .catch(error => console.error('Error fetching assets:', error));
  }

  function renderAssets(data) {
    const assetCollectionWrapper = document.querySelector('#assetCollectionWrapper .assets__collection');
    assetCollectionWrapper.innerHTML = '';

    data.results.forEach(asset => {
      const assetItem = document.createElement('div');
      assetItem.classList.add('w-dyn-item');
      assetItem.innerHTML = `
        <div class="asset__block" onclick="showLargeAsset(this)" data-id="${asset.id}">
          <img alt="${asset.title}" loading="eager" src="${asset.image_url}" class="asset__thumbnail">
          <div class="asset">
            <div class="date">${new Date(asset.date).toLocaleDateString()}</div>
            <h4 class="asset__heading">${asset.title}</h4>
            <p class="asset__paragraph">${asset.description}</p>
          </div>
        </div>
      `;
      assetCollectionWrapper.appendChild(assetItem);
    });
  }

  window.showLargeAsset = function(element) {
    const assetId = element.getAttribute('data-id');
    
    fetch(`/api/v2/assets/${assetId}/`) // Update this URL to your actual API endpoint for a single asset
      .then(response => response.json())
      .then(asset => {
        const largeAssetWrapper = document.getElementById('largeAssetWrapper');
        const largeAssetImage = document.getElementById('largeAssetImage');
        const largeAssetDate = document.getElementById('largeAssetDate');
        const largeAssetHeading = document.getElementById('largeAssetHeading');
        const largeAssetParagraph = document.getElementById('largeAssetParagraph');

        largeAssetImage.src = asset.image_url;
        largeAssetDate.textContent = new Date(asset.date).toLocaleDateString();
        largeAssetHeading.textContent = asset.title;
        largeAssetParagraph.textContent = asset.description;

        largeAssetWrapper.style.display = 'block';
        largeAssetWrapper.style.opacity = '1';

        document.querySelectorAll('.asset__block').forEach(block => {
          block.classList.remove('selected');
        });

        element.classList.add('selected');
      })
      .catch(error => console.error('Error fetching asset details:', error));
  }
});
