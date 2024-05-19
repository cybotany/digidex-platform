document.addEventListener('DOMContentLoaded', function() {
  // Function to show selected inventory content and hide others
  function showInventoryContent(index) {
    // Hide all inventory content
    document.querySelectorAll('.inventory-content').forEach(function(content) {
      content.style.display = 'none';
    });
    // Show the selected inventory content
    const selectedContent = document.getElementById('inventory-content-' + index);
    if (selectedContent) {
      selectedContent.style.display = 'block';
    }
  }

  // Add event listeners to inventory buttons
  document.querySelectorAll('.block-assets .link-asset').forEach(function(button, index) {
    button.addEventListener('click', function(event) {
      event.preventDefault();
      showInventoryContent(index);
    });
  });

  // Show the first inventory by default
  showInventoryContent(0);

  // Add event listener for create group button if exists
  const createGroupButton = document.getElementById('create-group-button');
  if (createGroupButton) {
    createGroupButton.addEventListener('click', function(event) {
      event.preventDefault();
      document.querySelectorAll('.inventory-content').forEach(function(content) {
        content.style.display = 'none';
      });
      const createGroupForm = document.getElementById('create-group-form');
      if (createGroupForm) {
        createGroupForm.style.display = 'block';
      }
    });
  }
});