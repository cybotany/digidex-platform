$(document).ready(function() {
    $('#send-btn').click(function() {
        var userInput = $('#chat-input').val();
        if (userInput) {
            // Append user's message to chatbox
            $('#chatbox').append('<p>You: ' + userInput + '</p>');
            
            $.ajax({
                url: '/chatbot/',
                method: 'POST',
                data: JSON.stringify({
                    'input': userInput
                }),
                contentType: 'application/json',
                success: function(data) {
                    // Append chatbot's response to chatbox
                    $('#chatbox').append('<p>Chatbot: ' + data.response + '</p>');
                }
            });
            
            // Clear the input field
            $('#chat-input').val('');
        }
    });
});
