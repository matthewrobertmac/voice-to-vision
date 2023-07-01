import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';
import { AudioRecorder } from 'react-audio-voice-recorder';

const UploadOrRecordAudio = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const fileSelectedHandler = event => {
    setSelectedFile(event.target.files[0]);
  };

  const fileUploadHandler = () => {
    const formData = new FormData();
    formData.append('file', selectedFile);

    fetch('http://localhost:7000/uploads', { // Replace with your server endpoint
      method: 'POST',
      body: formData
    }).then(response => {
      console.log(response);
    }).catch(error => {
      console.error(error);
    });
  };

  const addAudioElement = (blob) => {
    setSelectedFile(blob);
    fileUploadHandler();
  };

  return (
    <div>
      <Form>
        <FormGroup>
          <Label for="fileUpload">Upload or Record an MP3 file</Label>
          <Input type="file" name="file" id="fileUpload" accept=".mp3" onChange={fileSelectedHandler} />
          <Button color="primary" onClick={fileUploadHandler}>Upload</Button>
        </FormGroup>
      </Form>

      <AudioRecorder 
        onRecordingComplete={addAudioElement}
        audioTrackConstraints={{
          noiseSuppression: true,
          echoCancellation: true,
        }} 
        downloadOnSavePress={true}
        downloadFileExtension="mp3"
      />
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <UploadOrRecordAudio />
  </React.StrictMode>
);

export default UploadOrRecordAudio;