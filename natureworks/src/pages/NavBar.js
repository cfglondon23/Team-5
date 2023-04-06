import React, { useState } from "react";
import { Link } from "react-router-dom";

export default function NavBar() {
  return (
    <div className="navbar">
      <nav className="navbarWide">
        <div className="flexbox">
          <div className="title">
            <Link to="/" className="button">
              NatureWorks
            </Link>
          </div>
          <div className="item">
            <Link to="/" className="button">
              Home{" "}
            </Link>
            <Link to="/campaign" className="button">
              Campaign{" "}
            </Link>
          </div>
        </div>
      </nav>
    </div>
  );
}
