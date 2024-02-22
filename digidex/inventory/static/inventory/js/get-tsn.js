// DOM Elements
const taxonomicUnitField = document.getElementById('id_taxon');

// Configurations for select2
const select2Config = {
  ajax: {
    url: '/api/get-tsn/',
    dataType: 'json',
    delay: 250,
    data: function (params) {
      return {
        q: params.term,
        page: params.page
      };
    },
    processResults: function (data) {
      return {
        results: data.items,
      };
    },
    cache: true,
    beforeSend: function(xhr) {
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    },
    xhrFields: {
      withCredentials: true
    },
 },
  minimumInputLength: 3,
  placeholder: 'Start typing to search for taxonomic units',
};

// Initialize select2
$(document).ready(function() {
  $(taxonomicUnitField).select2(select2Config);
});