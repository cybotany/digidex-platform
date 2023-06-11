$(document).ready(function() {
    $('#chooseImageUpload').click(function() {
        $('#manualEntryForm').fadeOut('slow', function() {
            $('#imageUploadForm').load('/auto_plant_registration/', function() {
                $(this).fadeIn('slow');
            });
        });
    });

    $('#chooseManualEntry').click(function() {
        $('#imageUploadForm').fadeOut('slow', function() {
            $('#manualEntryForm').load('/manual_plant_registration/', function() {
                $(this).fadeIn('slow');
            });
        });
    });
});
