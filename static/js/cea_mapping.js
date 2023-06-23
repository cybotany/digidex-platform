fetch('/api/cea_mapping/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ip_address: '192.168.0.1', identifier: 'cea-1'}),
})
.then(response => response.json())
.then(data => {
    // Assuming your response data contains a greenhouse_id key
    var greenhouse_id = data.greenhouse_id;
    
    // Redirect to a page to complete registration.
    // Replace 'complete_registration_url' with the actual URL of your form page
    window.location.href = `/complete_registration_url?greenhouse_id=${greenhouse_id}`;
})
.catch((error) => {
    console.error('Error:', error);
});
