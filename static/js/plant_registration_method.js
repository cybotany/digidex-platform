$(document).ready(function() {
    $('#chooseAutoRegistration').click(function() {
        $('#manualRegistrationForm').fadeOut('slow', function() {
            $('#autoRegistrationForm').load('/botany/auto_plant_registration', function() {
                $(this).fadeIn('slow');
            });
        });
    });

    $('#chooseManualRegistration').click(function() {
        $('#autoRegistrationForm').fadeOut('slow', function() {
            $('#manualRegistrationForm').load('/botany/manual_plant_registration', function() {
                $(this).fadeIn('slow');
            });
        });
    });
});
