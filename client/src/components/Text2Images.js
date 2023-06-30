import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Text2Images() {
  const [text2images, setText2images] = useState([]);

  useEffect(() => {
    // Connecting to your API
    axios.get('http://localhost:7000/text2images')
    .then((response) => {
      setText2images(response.data);
    })
    .catch((error) => console.error(`Error: ${error}`));
  }, []);

  return (
    <div>
      <h1>Text2Images</h1>
      {text2images.map((text2image) => (
        <div key={text2image.id}>
          <p>{text2image.text}</p>
          <img src={text2image.image_url} alt={text2image.text} />
        </div>
      ))}
    </div>
  );
}

export default Text2Images;
