const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const chatbox = document.getElementById('chatbox');
const sendButton = document.getElementById('send-button');

function typeMessage(message, element) {
    let i = 0;
    const typing = setInterval(() => {
        if (i < message.length) {
            element.textContent += message.charAt(i);
            i++;
        } else {
            clearInterval(typing);
            chatInput.style.display = "block";
            sendButton.style.display = "block";
        }
    }, 50);
}

chatForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const message = chatInput.value;
    chatInput.value = '';

    // User message
    const userMessageElem = document.createElement('div');
    userMessageElem.innerText = message;
    userMessageElem.className = 'message user-message';
    chatbox.appendChild(userMessageElem);

    // Typing message
    const typingMessageElem = document.createElement('div');
    typingMessageElem.className = 'message chatbot-message';
    typingMessageElem.innerText = 'Thinking...';
    chatbox.appendChild(typingMessageElem);
    chatInput.style.display = "none";

    // CSRF Token
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // AJAX Request
    $.ajax({
        url: '/api/get_chat_message/',
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        data: JSON.stringify({'message': message}),
        contentType: 'application/json',
        success: (data) => {
            chatbox.removeChild(typingMessageElem);
            const chatbotMessageElem = document.createElement('div');
            chatbotMessageElem.className = 'message chatbot-message';
            chatbotMessageElem.innerText = '';
            chatbox.appendChild(chatbotMessageElem);
            typeMessage(data.message, chatbotMessageElem);
        },
        error: (jqXHR, textStatus, errorThrown) => {
            chatbox.removeChild(typingMessageElem);
            chatInput.style.display = "block";
            sendButton.style.display = "block";
            const errorMessageElem = document.createElement('div');
            errorMessageElem.innerText = 'Error: ' + errorThrown;
            chatbox.appendChild(errorMessageElem);
        }
    });

    chatbox.scrollTop = chatbox.scrollHeight;
});
