import React from "react";
import { NavLink } from "react-router-dom";
import NavBar from "./ImageResults";

function Header() {
  return (
    <div id="toy-header">
      {/* <form>
        <label>
          <p>Username</p>
          <input type="text" />
        </label>
        <label>
          <p>Password</p>
          <input type="password" />
        </label>
        <div>
          <button type="submit">Submit</button>
        </div>
      </form>
      <img
        src="https://i.etsystatic.com/5811639/r/il/0c8152/4565700251/il_794xN.4565700251_5532.jpg"
        alt="toy header"
      /> */}

      <NavBar />
    </div>
  );
}

export default Header;