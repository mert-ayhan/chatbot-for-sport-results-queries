import React, { useState, useRef, useEffect } from "react";

import "./App.css";
import axios from "axios";

type Message = {
  sender: string;
  text: string;
};

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [userInput, setUserInput] = useState("");

  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!userInput.trim()) return;

    const newMessages = [...messages, { sender: "user", text: userInput }];
    setMessages(newMessages);
    setUserInput("");

    try {
      const response = await axios.post("http://localhost:8000/ask", {
        question: userInput,
      });

      const data = await response.data;

      const botMessage = { sender: "bot", text: data.answer };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error("Error fetching bot response:", error);
    }
  };

  return (
    <>
      <div className="flex flex-col h-screen bg-gray-800">
        <div className="container flex flex-col p-4 mx-auto mt-24 bg-gray-900 rounded-lg shadow h-4/5">
          <div className="flex-grow p-4 overflow-auto">
            <div className="flex flex-col space-y-4">
              {messages.map((message, index) => (
                <div
                  key={index}
                  className={`flex items-end ${
                    message.sender === "user" ? "justify-end" : ""
                  }`}
                >
                  <div
                    className={`p-3 text-white ${
                      message.sender === "user"
                        ? "bg-blue-600 rounded-t-lg rounded-l-lg"
                        : "bg-gray-700 rounded-t-lg rounded-r-lg"
                    }`}
                  >
                    {message.text}
                  </div>
                </div>
              ))}
              <div ref={messagesEndRef} />
            </div>
          </div>
        </div>
        <div className="flex items-center justify-center min-w-full p-4">
          <form className="container flex space-x-4" onSubmit={handleSubmit}>
            <input
              type="text"
              placeholder="Write a message..."
              className="flex-grow p-2 border rounded"
              style={{ borderColor: "rgba(255, 255, 255, 0.25)" }}
              value={userInput}
              onChange={(e) => setUserInput(e.target.value)}
            />
            <button
              type="submit"
              className="px-4 py-2 text-white bg-blue-600 rounded"
            >
              Send
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

export default App;
