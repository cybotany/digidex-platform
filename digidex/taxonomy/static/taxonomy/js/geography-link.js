$(document).ready(function() {
  $('.geography-link').click(function(e) {
      e.preventDefault();
      const geographyId = $(this).data('geography-id');

      // Construct the base URL dynamically
      const baseUrl = `${window.location.protocol}//${window.location.host}/`;

      // Construct the full URL for the AJAX request
      const requestUrl = baseUrl + `api/get-geography/${geographyId}/`;

      // AJAX request to fetch geography details
      $.ajax({
          url: requestUrl,
          type: 'GET',
          success: function(response) {
              // Handle 'valid_units_by_rank'
              let rankHtml = '<ul>'; // Start an unordered list
              response.valid_units_by_rank.forEach(function(rank) {
                  // For each rank, append a list item with the rank name and valid units count
                  rankHtml += `<li>${rank.rank__rank_name}: ${rank.valid_units_count}</li>`;
              });
              rankHtml += '</ul>'; // Close the unordered list

              let geographyHtml = '<ul>';
              response.valid_units_by_geography.forEach(function(geography) {
                  geographyHtml += `<li>${geography.geography_value}: ${geography.valid_units_count}</li>`;
              });
              geographyHtml += '</ul>';

              let jurisdictionHtml = '<ul>';
              response.valid_units_by_jurisdiction.forEach(function(jurisdiction) {
                  jurisdictionHtml += `<li>${jurisdiction.jurisdiction_value}: ${jurisdiction.valid_units_count}</li>`;
              });
              jurisdictionHtml += '</ul>';
                    
              $('#rank-details').html(rankHtml);
              $('#geography-details').html(geographyHtml);
              $('#jurisdiction-details').html(jurisdictionHtml);
          },
          error: function(xhr, status, error) {
              // Handle errors here
              console.error("Error fetching geography details:", error);
          }
      });
  });
});