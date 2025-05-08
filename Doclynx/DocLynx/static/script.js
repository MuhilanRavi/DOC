function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;
  
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
    input.value = "";
  
    document.getElementById("loading").style.display = "block";
  
    fetch("/chat", {
      method: "POST",
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message})
    })
    .then(res => res.json())
    .then(data => {
      chatBox.innerHTML += `<div><strong>DocLynx:</strong> ${data.response}</div>`;
      document.getElementById("loading").style.display = "none";
      chatBox.scrollTop = chatBox.scrollHeight;
    });
  }