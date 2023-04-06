import React from "react";

export default function User() {
  return (
    <div className="user">
      <div className="userFlex">
        <div className="greenbox">
          <div className="flex">
            <div className="icon">
              {" "}
              <img
                src={require("../assets/images/user.png")}
                alt="thankyou"
                className="image"
              />
            </div>
            <div className="name">Sam</div>
            <div className="city">City: London</div>
            <div className="score">Personal score: 34 </div>
          </div>
        </div>
        <div className="buttonFlex">
          <div className="button">Logout</div>
        </div>
      </div>
    </div>
  );
}
