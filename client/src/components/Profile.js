import React, { useRef } from "react";

const Profile = ({ data, addFile }) => {
  const inputRef = useRef(null);

  const handleAddFile = (event) => {
    event.preventDefault();
    const file = inputRef.current.files[0];
    if (file) {
      console.log(file);
      addFile(file);
    }
  };

  return (
    <div>
      <h1>My Profile</h1>
      <h2>{data?.name || 'User Name'}</h2>

      <h2>New Project</h2>
      <form onSubmit={handleAddFile}>
        <div className="form-row">
          <label htmlFor="audio">Add MP3</label>
          <input type="file" id="audio" name="audio" accept="audio/mpeg" ref={inputRef}/>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Profile;
