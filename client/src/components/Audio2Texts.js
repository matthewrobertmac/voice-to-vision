import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Audio2Texts() {
  const [audio2texts, setAudio2texts] = useState([]);

  useEffect(() => {
    // Connecting to your API
    axios.get('http://localhost:7000/audio2texts')
    .then((response) => {
      setAudio2texts(response.data);
    })
    .catch((error) => console.error(`Error: ${error}`));
  }, []);

  return (
    <div>
      <h1>Audio2Texts</h1>
      {audio2texts.map((audio2text) => (
        <div key={audio2text.id}>
          <p>{audio2text.audio_file_path}</p>
          <p>{audio2text.transcript_text}</p>
        </div>
      ))}
    </div>
  );
}

export default Audio2Texts;
