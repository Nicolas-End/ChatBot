document.addEventListener("DOMContentLoaded", function() {
  const messages = document.getElementById("messages");
  const messageInput = document.getElementById("message-input");
  const sendButton = document.getElementById("send-button");

  sendButton.addEventListener("click", function() {
    const messageText = messageInput.value.trim();
    if (messageText !== "") {
      addMessage(messageText, 'sent');
      sendMessage(messageText);
      messageInput.value = "";
    }
  });

  messageInput.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
      const messageText = messageInput.value.trim();
      if (messageText !== "") {
        addMessage(messageText, 'sent');
        sendMessage(messageText);
        messageInput.value = "";
      }
    }
  });

  function addMessage(text, type) {
    const message = document.createElement("div");
    message.className = `message ${type}`;
    message.textContent = text;
    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
  }

  function sendMessage(messageText) {
    fetch('/home', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `entrada=${messageText}`
    })
    .then(response => response.json())
    .then(data => {
      addMessage(`CharBot: ${data}`, 'received');
    })
    .catch(error => console.error('Erro:', error));
  }
});