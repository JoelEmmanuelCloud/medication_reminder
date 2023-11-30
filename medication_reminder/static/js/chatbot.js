// static/js/chatbot.js
document.addEventListener('DOMContentLoaded', function () {
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    sendBtn.addEventListener('click', function () {
        const userMessage = userInput.value;

        // Add user message to the chat container
        chatContainer.innerHTML += `<div class="user-message">${userMessage}</div>`;

        // Send user message to the server
        sendUserMessage(userMessage);

        // Clear the user input field
        userInput.value = '';
    });
});

function sendUserMessage(userMessage) {
    // Send the user message to the server using AJAX
    const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    fetch('/reminder/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ user_message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        // Add chatbot response to the chat container
        const botResponse = data.bot_response;
        chatContainer.innerHTML += `<div class="bot-message">Chatbot: ${botResponse}</div>`;
    })
    .catch(error => console.error('Error:', error));
}
