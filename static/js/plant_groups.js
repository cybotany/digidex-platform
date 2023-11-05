const plantListContainer = document.getElementById('plantListContainer');
const leftArrow = document.getElementById('leftArrow');
const rightArrow = document.getElementById('rightArrow');

// Ensure the leftArrow exists before attaching the event
if (leftArrow) {
    leftArrow.addEventListener('click', function() {
        const prevGroupId = this.getAttribute('data-group-id');
        if (prevGroupId) fetchPlantsForGroup(prevGroupId);
    });
}

// Ensure the rightArrow exists before attaching the event
if (rightArrow) {
    rightArrow.addEventListener('click', function() {
        const nextGroupId = this.getAttribute('data-group-id');
        if (nextGroupId) fetchPlantsForGroup(nextGroupId);
    });
}

function fetchPlantsForGroup(groupId) {
    fetch(`/api/get_group/${groupId}/`)
    .then(response => response.json())
    .then(data => {
        // Check if data is an array before processing
        if (Array.isArray(data)) {
            updatePlantList(data);
        } else {
            console.error("Expected data to be an array but got:", data);
        }
    })
    .catch(error => {
        console.error("There was an error fetching the plants:", error);
    });
}

function updatePlantList(data) {
    let plantHtml = '';
    data.forEach(plant => {
        plantHtml += `
            <div class="col-md-4 mb-4">
                <div class="plant-card">
                    <h2>${plant.name}</h2>
                    <p>${plant.description}</p>
                </div>
            </div>
        `;
    });
    plantListContainer.innerHTML = plantHtml;
}
