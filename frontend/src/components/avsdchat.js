import React, { useState } from 'react';
import { sendMessageToAVSD } from '../services/api';
import { Input, Button, List } from 'antd';

function AVSDChat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = () => {
    sendMessageToAVSD({ message: input }).then(response => {
      setMessages([...messages, { sender: 'user', text: input }, { sender: 'avsd', text: response.data.response }]);
      setInput('');
    });
  };

  return (
    <div>
      <List
        dataSource={messages}
        renderItem={msg => (
          <List.Item>
            <strong>{msg.sender === 'user' ? 'Você' : 'Assistente'}:</strong> {msg.text}
          </List.Item>
        )}
      />
      <Input
        value={input}
        onChange={e => setInput(e.target.value)}
        onPressEnter={sendMessage}
        placeholder="Digite sua mensagem"
        style={{ marginTop: '10px' }}
      />
      <Button type="primary" onClick={sendMessage} style={{ marginTop: '10px' }}>
        Enviar
      </Button>
    </div>
  );
}

export default AVSDChat;
