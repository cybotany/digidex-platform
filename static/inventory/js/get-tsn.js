// DOM Elements
const tsnField = document.getElementById('tsnField');

// Configurations for select2
const select2Config = {
    ajax: {
        url: '/api/get/tsn/',
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
    minimumInputLength: 1
};

// Initialize select2
$(document).ready(function() {
    $(tsnField).select2(select2Config);
});
