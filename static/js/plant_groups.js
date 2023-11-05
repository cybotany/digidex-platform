document.addEventListener('DOMContentLoaded', (event) => {
    const leftArrow = document.getElementById('leftArrow');
    const rightArrow = document.getElementById('rightArrow');
    const currentGroupName = document.getElementById('currentGroupName');
    const plantListContainer = document.getElementById('plantListContainer'); // Assuming the container ID is 'plantListContainer'

    leftArrow.addEventListener('click', function() {
        fetchPlantsForGroup(leftArrow.getAttribute('data-group-id'));
    });
    rightArrow.addEventListener('click', function() {
        fetchPlantsForGroup(rightArrow.getAttribute('data-group-id'));
    });

    function fetchPlantsForGroup(groupId) {
        fetch(`/api/get_group/${groupId}/`)
        .then(response => response.json())
        .then(data => {
            // Extract the 'plants' key and parse its string value into a JavaScript array
            const plantsArray = JSON.parse(data.plants);
            
            // Update the plant list
            updatePlantList(plantsArray);

            // Update the group's name
            currentGroupName.textContent = data.current_group_name;

            // Update the arrows' data-group-id
            leftArrow.setAttribute('data-group-id', data.prev_group_id);
            rightArrow.setAttribute('data-group-id', data.next_group_id);
        })
        .catch(error => {
            console.error("There was an error fetching the plants:", error);
        });
    }

    function updatePlantList(plantData) {
        let plantHtml = '';
        plantData.forEach(plant => {
            const hasNfcTag = plant.fields.nfc_tag ? '<div class="link-bubble-wrapper mr-2"><span class="link-bubble"></span></div>' : '';
            const plantImageUrl = plant.fields.images && plant.fields.images.length > 0 ? plant.fields.images[plant.fields.images.length-1].image.url : '';
            const plantImage = plantImageUrl ? `<img src="${plantImageUrl}" class="card-img" alt="Image of ${plant.fields.name}">` : '<div class="no-image-placeholder">No Image</div>';
            const wateringInfo = plant.fields.days_since_last_watering ? `Days since last watering: ${plant.fields.days_since_last_watering}` : 'This plant has not been watered yet.';

            plantHtml += `
                <div class="col-md-4 mb-4">
                    <a href="${plant.fields.get_absolute_url}" class="card-link">
                        <div class="card">
                            <!-- Card Header -->
                            <div class="card-header d-flex align-items-center">
                                ${hasNfcTag}
                                <span class="mx-auto">${plant.fields.name}</span>
                            </div>
                            <!-- Plant Image -->
                            <div class="card-image-wrapper">
                                ${plantImage}
                            </div>
                            <!-- Card Body -->
                            <div class="card-body">
                                <p class="card-text">${wateringInfo}</p>
                            </div>
                            <!-- Card Footer -->
                            <div class="card-footer text-center">${plant.fields.tsn.complete_name}</div>
                        </div>
                    </a>
                </div>
            `;
        });
        plantListContainer.innerHTML = plantHtml;
    }
});
