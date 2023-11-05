const plantListContainer = document.getElementById('plantListContainer');
const leftArrow = document.getElementById('leftArrow');
const rightArrow = document.getElementById('rightArrow');
const currentGroupName = document.getElementById('currentGroupName');

// Event listeners for arrows remain unchanged

function fetchPlantsForGroup(groupId) {
    fetch(`/api/get_group/${groupId}/`)
    .then(response => response.json())
    .then(data => {
        // Update the plant list
        updatePlantList(data.plants);

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
    // Parse the plantData since it's a JSON string
    let plants = JSON.parse(plantData);
    let plantHtml = '';
    plants.forEach(plant => {
        plantHtml += `
            <div class="col-md-4 mb-4">
                <div class="plant-card">
                    <h2>${plant.fields.name}</h2>
                    <p>${plant.fields.description}</p>
                </div>
            </div>
        `;
    });
    plantListContainer.innerHTML = plantHtml;
}
