var chatForm = document.getElementById('chat-form');
var chatInput = document.getElementById('chat-input');
var chatbox = document.getElementById('chatbox');

// This function will append the characters one by one
function typeMessage(message, element) {
    var i = 0;
    var typing = setInterval(function() {
        if(i < message.length){
            element.textContent += message.charAt(i);
            i++;
        } else {
            clearInterval(typing);
            // When the bot finishes typing, show the chat input box
            chatInput.style.display = "block";
        }
    }, 50); // This is the typing speed in milliseconds
}

chatForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var message = chatInput.value;
    chatInput.value = '';

    // Add user's message to chatbox
    var userMessageElem = document.createElement('div');
    userMessageElem.innerText = 'You: ' + message;
    chatbox.appendChild(userMessageElem);

    // Create and display "Bot is typing..." message
    var typingMessageElem = document.createElement('div');
    typingMessageElem.innerText = 'Chatbot is typing...';
    chatbox.appendChild(typingMessageElem);

    // Hide the chat input box while the bot is typing
    chatInput.style.display = "none";

    // Make AJAX request to chatbot backend
    $.ajax({
        url: '/api/cybot/',
        method: 'POST',
        data: JSON.stringify({
            'message': message
        }),
        contentType: 'application/json',
        success: function(data) {
            // Remove "Bot is typing..." message
            chatbox.removeChild(typingMessageElem);

            // Append chatbot's response to chatbox
            var chatbotMessageElem = document.createElement('div');
            chatbotMessageElem.innerText = 'Chatbot: ';
            chatbox.appendChild(chatbotMessageElem);

            // Type the chatbot's response progressively
            typeMessage(data.message, chatbotMessageElem);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // Remove "Bot is typing..." message
            chatbox.removeChild(typingMessageElem);

            // Show the chat input box in case of an error
            chatInput.style.display = "block";

            // Append an error message to the chatbox
            var errorMessageElem = document.createElement('div');
            errorMessageElem.innerText = 'Error: ' + errorThrown;
            chatbox.appendChild(errorMessageElem);
        }
    });

    chatbox.scrollTop = chatbox.scrollHeight;
});
