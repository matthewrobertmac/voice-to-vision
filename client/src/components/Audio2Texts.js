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
      <table style={{width: "100%", backgroundColor: "#ADD8E6"}}>
        <thead>
          <tr>
            <th>Audio File Path</th>
            <th>Transcript Text</th>
          </tr>
        </thead>
        <tbody>
          {audio2texts.map((audio2text) => (
            <tr key={audio2text.id}>
              <td>{audio2text.audio_file_path}</td>
              <td>{audio2text.transcript_text}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Audio2Texts;
