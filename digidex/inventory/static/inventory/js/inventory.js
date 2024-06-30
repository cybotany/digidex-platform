document.addEventListener("DOMContentLoaded", function() {
  const trainerId = 'trainer-id';  // replace with the actual trainer ID you need to fetch

  fetch(`/api/v2/trainers/${trainerId}/`)
      .then(response => response.json())
      .then(data => {
          document.getElementById('trainer-link').dataset.id = data.uuid;
          const categoryList = document.getElementById('category-list');
          data.collection.forEach(category => {
              const categoryItem = document.createElement('div');
              categoryItem.setAttribute('role', 'listitem');
              categoryItem.classList.add('collection-item-categories', 'base-dyn-item');
              categoryItem.dataset.id = category.uuid;

              const categoryLink = document.createElement('a');
              categoryLink.href = category.url;
              categoryLink.classList.add('link-category', 'base-inline-block');

              const categoryImg = document.createElement('img');
              categoryImg.src = '{% static "base/images/nfc/directional/nfc_directional_mark_black.png" %}';
              categoryImg.loading = 'eager';
              categoryImg.alt = '';
              categoryImg.classList.add('icon-category');

              const categoryText = document.createElement('div');
              categoryText.classList.add('text-category');
              categoryText.textContent = category.title;

              categoryLink.appendChild(categoryImg);
              categoryLink.appendChild(categoryText);
              categoryItem.appendChild(categoryLink);
              categoryList.appendChild(categoryItem);
          });
      })
      .catch(error => console.error('Error fetching trainer data:', error));
});