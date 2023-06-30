import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Text2Texts() {
  const [text2texts, setText2texts] = useState([]);

  useEffect(() => {
    // Connecting to your API
    axios.get('http://localhost:7000/text2texts')
    .then((response) => {
      setText2texts(response.data);
    })
    .catch((error) => console.error(`Error: ${error}`));
  }, []);

  return (
    <div>
      <h1>Text2Texts</h1>
      {text2texts.map((text2text) => (
        <div key={text2text.id}>
          <p>{text2text.original_text}</p>
          <p>{text2text.converted_text}</p>
        </div>
      ))}
    </div>
  );
}

export default Text2Texts;
