// DOM Elements
const plantGroupSelector = document.getElementById('plantGroupSelector');
const plantListContainer = document.getElementById('plantListContainer');

// Event Listener for when the plant group is changed
plantGroupSelector.addEventListener('change', function() {
    const selectedGroupId = this.value;

    fetch(`/api/plants_by_group/${selectedGroupId}/`)
    .then(response => response.json())
    .then(data => {
        updatePlantList(data);
    })
    .catch(error => {
        console.error("There was an error fetching the plants:", error);
    });
});

// Update the plant list on the page with new data
function updatePlantList(data) {
    let plantHtml = '';

    data.forEach(plant => {
        // You can customize the HTML structure as needed
        plantHtml += `
            <div class="plant-item">
                <h2>${plant.name}</h2>
                <p>${plant.description}</p>
            </div>
        `;
    });

    plantListContainer.innerHTML = plantHtml;
}

// Fetch plants for the initial group on page load
document.addEventListener('DOMContentLoaded', (event) => {
    const initialGroupId = plantGroupSelector.value;
    if (initialGroupId) {
        fetch(`/api/plants_by_group/${initialGroupId}/`)
        .then(response => response.json())
        .then(data => {
            updatePlantList(data);
        })
        .catch(error => {
            console.error("There was an error fetching the plants:", error);
        });
    }
});
