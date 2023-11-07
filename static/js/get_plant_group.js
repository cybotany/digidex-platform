document.addEventListener('DOMContentLoaded', (event) => {
    const leftArrow = document.getElementById('leftArrow');
    const rightArrow = document.getElementById('rightArrow');
    const currentGroupName = document.getElementById('currentGroupName');
    const plantListContainer = document.getElementById('plantListContainer'); 

    leftArrow.addEventListener('click', function() {
        fetchPlantsForGroup(leftArrow.getAttribute('data-group-id'));
    });
    rightArrow.addEventListener('click', function() {
        fetchPlantsForGroup(rightArrow.getAttribute('data-group-id'));
    });

    function fetchPlantsForGroup(groupId) {
        const accessToken = localStorage.getItem('accessToken');

        fetch(`/api/get_plant_group/${groupId}/`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${accessToken}`,
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            const plantsArray = data.plants;
            
            // Update the plant list
            updatePlantList(plantsArray);

            // Update the group's name
            currentGroupName.textContent = data.current_group_name;

            // Update the arrows' data-group-id
            leftArrow.setAttribute('data-group-id', data.prev_group_id);
            rightArrow.setAttribute('data-group-id', data.next_group_id);

            // Show or hide the 'No plants found' message
            const noPlantsMessage = document.getElementById('noPlantsMessage');
            if (plantsArray.length === 0) {
                noPlantsMessage.style.display = 'block';
            } else {
                noPlantsMessage.style.display = 'none';
            }
        })
        .catch(error => {
            console.error("There was an error fetching the plants:", error);
        });
    }

    function updatePlantList(plantData) {
        let plantHtml = '';
        plantData.forEach(plant => {
            // Add checks to ensure the object and its nested properties exist before trying to access them
            const hasNfcTag = plant.nfc_tag 
                ? '<div class="link-bubble-wrapper mr-2"><span class="link-bubble"></span></div>' 
                : '';
            const plantImages = plant.images 
                ? plant.fields.images 
                : [];
            const plantImageUrl = plantImages.length > 0 
                ? plantImages[plantImages.length - 1].image.url 
                : '';
            const plantImage = plantImageUrl 
                ? `<img src="${plantImageUrl}" class="card-img" alt="Image of ${plant.name}">` 
                : '<div class="no-image-placeholder">No Image</div>';
            const wateringInfo = plant.days_since_last_watering 
                ? `Days since last watering: ${plant.days_since_last_watering}` 
                : 'This plant has not been watered yet.';
            const plantName = plant.name 
                ? plant.name 
                : 'Unknown Plant';
            const plantUrl = plant.get_absolute_url 
                ? plant.get_absolute_url 
                : '#';
            const plantTsnName = plant.tsn.complete_name 
                ? plant.tsn.complete_name 
                : 'No TSN Available';
    
            plantHtml += `
                <div class="col-md-4 mb-4">
                    <a href="${plantUrl}" class="card-link">
                        <div class="card">
                            <!-- Card Header -->
                            <div class="card-header d-flex align-items-center">
                                ${hasNfcTag}
                                <span class="mx-auto">${plantName}</span>
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
                            <div class="card-footer text-center">${plantTsnName}</div>
                        </div>
                    </a>
                </div>
            `;
        });
        plantListContainer.innerHTML = plantHtml;
    }    

    // Load the initial plant set
    const initialGroupId = plantListContainer.getAttribute('data-current-group-id');
    fetchPlantsForGroup(initialGroupId);
});
