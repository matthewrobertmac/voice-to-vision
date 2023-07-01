import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';
import { AudioRecorder } from 'react-audio-voice-recorder';

const UploadForm = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const fileSelectedHandler = event => {
    setSelectedFile(event.target.files[0]);
  };

  const fileUploadHandler = () => {
    const formData = new FormData();
    formData.append('file', selectedFile);

    fetch('http://localhost:7000/upload', { // Replace with your Flask endpoint
      method: 'POST',
      body: formData
    }).then(response => {
      console.log(response);
    }).catch(error => {
      console.error(error);
    });
  };

  const addAudioElement = (blob) => {
    const url = URL.createObjectURL(blob);
    const audio = document.createElement("audio");
    audio.src = url;
    audio.controls = true;
    document.body.appendChild(audio);
  };

  return (
    <div>
      <Form>
        <FormGroup>
          <Label for="fileUpload">Upload an MP3 file</Label>
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
    <UploadForm />
  </React.StrictMode>
);

export default UploadForm;

// import React, { useState } from "react";
// import { Button, Form, FormGroup, Label, Input } from 'reactstrap';

// const UploadForm = () => {
//   const [selectedFile, setSelectedFile] = useState(null);

//   const fileSelectedHandler = event => {
//     setSelectedFile(event.target.files[0]);
//   };

//   const fileUploadHandler = () => {
//     const formData = new FormData();
//     formData.append('file', selectedFile);

//     fetch('http://localhost:7000/upload', { // Replace with your Flask endpoint
//       method: 'POST',
//       body: formData
//     }).then(response => {
//       console.log(response);
//     }).catch(error => {
//       console.error(error);
//     });
//   };

//   return (
//     <Form>
//       <FormGroup>
//         <Label for="fileUpload">Upload an MP3 file</Label>
//         <Input type="file" name="file" id="fileUpload" accept=".mp3" onChange={fileSelectedHandler} />
//         <Button color="primary" onClick={fileUploadHandler}>Upload</Button>
//       </FormGroup>
//     </Form>
//   );
// }

// export default UploadForm;

