$(document).ready(function() {
    $('#species-select').select2({
        ajax: {
            url: 'ajax//species-autocomplete/',
            dataType: 'json',
            delay: 250,
            data: function (params) {
                return {
                    q: params.term,
                };
            },
            processResults: function (data) {
                return {
                    results: data.results
                };
            },
            cache: true
        },
        minimumInputLength: 2,
        placeholder: 'Search for a species',
    }).on('select2:select', function (e) {
        var data = e.params.data;
        $('#id_taxon_id').val(data.id);
    });
});