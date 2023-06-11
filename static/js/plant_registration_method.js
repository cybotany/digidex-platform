$(document).ready(function() {
    $('#chooseAutoRegistration').click(function() {
        $('#manualRegistrationForm').fadeOut('slow', function() {
            $('#autoRegistrationForm').load('/auto_plant_registration/', function() {
                $(this).fadeIn('slow');
            });
        });
    });

    $('#chooseManualRegistration').click(function() {
        $('#autoRegistrationForm').fadeOut('slow', function() {
            $('#manualRegistrationForm').load('/manual_plant_registration/', function() {
                $(this).fadeIn('slow');
            });
        });
    });
});
