$(document).ready(function() {
    $('#chooseImageUpload').click(function() {
        $('#manualEntryForm').fadeOut('slow', function() {
            $('#imageUploadForm').load('/image_upload_form/', function() {
                $(this).fadeIn('slow');
            });
        });
    });

    $('#chooseManualEntry').click(function() {
        $('#imageUploadForm').fadeOut('slow', function() {
            $('#manualEntryForm').load('/manual_entry_form/', function() {
                $(this).fadeIn('slow');
            });
        });
    });
});
