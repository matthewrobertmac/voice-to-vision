import React, { useState } from "react";
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';

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

  return (
    <Form>
      <FormGroup>
        <Label for="fileUpload">Upload an MP3 file</Label>
        <Input type="file" name="file" id="fileUpload" accept=".mp3" onChange={fileSelectedHandler} />
        <Button color="primary" onClick={fileUploadHandler}>Upload</Button>
      </FormGroup>
    </Form>
  );
}

export default UploadForm;

