import React, { useState } from 'react';
import './copilotWidget.css';

function CopilotWidget() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");

  const toggleChat = () => setIsOpen(!isOpen);

  const sendMessage = async () => {
    if (!question.trim()) return;

    const newMessages = [...messages, { from: "user", text: question }];
    setMessages(newMessages);
    setQuestion("");

    const res = await fetch("http://localhost:5000/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ page: window.location.pathname, question })
    });

    const data = await res.json();
    setMessages([...newMessages, { from: "bot", text: data.answer }]);
  };

  return (
    <div className="copilot-container">
      {isOpen && (
        <div className="chat-box">
          <div className="chat-header">🤖 Copilot</div>
          <div className="chat-messages">
            {messages.map((msg, i) => (
              <div key={i} className={msg.from === "user" ? "user-msg" : "bot-msg"}>
                {msg.text}
              </div>
            ))}
          </div>
          <div className="chat-input">
            <input
              value={question}
              onChange={e => setQuestion(e.target.value)}
              placeholder="Ask a question..."
              onKeyDown={e => e.key === "Enter" && sendMessage()}
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </div>
      )}
      <button className="chat-toggle" onClick={toggleChat}>💬</button>
    </div>
  );
}

export default CopilotWidget;
