var chatForm = document.getElementById('chat-form');
var chatInput = document.getElementById('chat-input');
var chatbox = document.getElementById('chatbox');

chatForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var message = chatInput.value;
    chatInput.value = '';

    // Add user's message to chatbox
    var userMessageElem = document.createElement('div');
    userMessageElem.innerText = 'You: ' + message;
    chatbox.appendChild(userMessageElem);

    // Make AJAX request to chatbot backend
    $.ajax({
        url: '/api/cybot/',
        method: 'POST',
        data: JSON.stringify({
            'message': message
}),
        contentType: 'application/json',
        success: function(data) {
            // Append chatbot's response to chatbox
            var chatbotMessageElem = document.createElement('div');
            chatbotMessageElem.innerText = 'Chatbot: ' + data.message;
            chatbox.appendChild(chatbotMessageElem);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Append an error message to the chatbox
            var errorMessageElem = document.createElement('div');
            errorMessageElem.innerText = 'Error: ' + errorThrown;
            chatbox.appendChild(errorMessageElem);
        }
    });

    chatbox.scrollTop = chatbox.scrollHeight;
});