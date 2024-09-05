document.addEventListener("DOMContentLoaded", function() {
  const msgerForm = document.querySelector(".msger-inputarea");
  const msgerInput = document.querySelector(".msger-input");
  const msgerChat = document.querySelector(".msger-chat");
  const BOT_IMG = "bot.jpg";
  const PERSON_IMG = "usuario.png";
  const BOT_NAME = "BOT";
  const PERSON_NAME = "Code mo";

  if (!msgerInput) {
    console.error("Elemento .msger-input não encontrado");
    return;
  }

  msgerForm.addEventListener("submit", event => {
    event.preventDefault();
    const msgText = msgerInput.value;
    if (!msgText) return;
    msgerInput.value = "";
    addChat(PERSON_NAME, PERSON_IMG, "right", msgText);
    output(msgText);
  });

  function output(input) {
    const delay = input.length * 40;
    fetch('/home', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: `entrada=${input}`
    })
    .then(response => response.json())
    .then(data => {
      let product = data;
      setTimeout(() => {
        addChat(BOT_NAME, BOT_IMG, "left", product);
      }, delay);
    })
    .catch(error => console.error('Erro:', error));
  }

  

  function addChat(name, img, side, text) {
    const msgHTML = `
      <div class="msg ${side}-msg">
        <div class="msg-img" style="background-image: url(/static/imgs/${img});"></div>
        <div class="msg-bubble">
          <div class="msg-info">
            <div class="msg-info-name">${name}</div>
            <div class="msg-info-time">${formatDate(new Date())}</div>
          </div>
          <div class="msg-text">${text}</div>
        </div>
      </div>
    `;
    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop = msgerChat.scrollHeight;
  }

  function get(selector, root = document) {
    return root.querySelector(selector);
  }

  function formatDate(date) {
    const h = date.getHours().toString().padStart(2, "0");
    const m = date.getMinutes().toString().padStart(2, "0");
    return `${h}:${m}`;
  }
});