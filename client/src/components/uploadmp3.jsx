import React, { useState } from 'react';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';

const UploadForm = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const fileSelectedHandler = event => {
    setSelectedFile(event.target.files[0]);
};

  const fileUploadHandler = () => { 
    console.log(selectedFile);
};

  return (
    <Form>
      <FormGroup>
        <Label for="fileUpload">Upload an MP3 file</Label>
        <Input type="file" name="file" id="fileUpload" accept=".mp3" onChange={fileSelectedHandler}>Upload MP3</Input>
        <Button color="primary" onClick={fileUploadHandler}>Upload</Button>
      </FormGroup>
    </Form>
  );
}

export default UploadForm;
