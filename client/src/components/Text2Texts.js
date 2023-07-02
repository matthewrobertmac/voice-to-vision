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
      <table style={{width: "100%", backgroundColor: "#ADD8E6"}}>
        <thead>
          <tr>
            <th>Original Text</th>
            <th>Converted Text</th>
          </tr>
        </thead>
        <tbody>
          {text2texts.map((text2text) => (
            <tr key={text2text.id}>
              <td>{text2text.original_text}</td>
              <td>{text2text.converted_text}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Text2Texts;
