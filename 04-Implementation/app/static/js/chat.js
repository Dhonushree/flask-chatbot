async function sendMessage() {
    const inputField = document.getElementById('user-input');
    const input = inputField.value;
    const res = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: input})
    });
    const data = await res.json();
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><strong>You:</strong> ${input}</p>`;
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
    inputField.value = '';
}
