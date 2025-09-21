import React, { useState } from "react";

function Chat() {
  const [message, setMessage] = useState("");
  const [conversation, setConversation] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    // Ajouter le message de l'utilisateur à la conversation
    setConversation([...conversation, { role: "user", content: message }]);

    const res = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    if (data.response) {
      // Ajouter la réponse du bot à la conversation
      setConversation([...conversation, { role: "user", content: message }, { role: "assistant", content: data.response }]);
    } else {
      console.error(data.error);
    }

    setMessage(""); // Réinitialiser l'entrée utilisateur
  };

  return (
    <div>
      <div style={{ border: "1px solid #ccc", padding: "10px", height: "300px", overflowY: "scroll" }}>
        {conversation.map((msg, index) => (
          <p key={index} style={{ color: msg.role === "user" ? "blue" : "green" }}>
            <strong>{msg.role === "user" ? "Vous" : "Assistant"}:</strong> {msg.content}
          </p>
        ))}
      </div>
      <textarea value={message} onChange={(e) => setMessage(e.target.value)} placeholder="Écrivez votre message ici..." />
      <button onClick={sendMessage}>Envoyer</button>
    </div>
  );
}

export default Chat;
