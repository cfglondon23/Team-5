import React from "react";

import { Link } from "react-router-dom";

export default function ThankYou() {
  return (
    <div className="thankyou">
      <div className="thankyouLeft">
        <div className="thanksjoin">Thank you for joining!</div>
        <div className="yourcontributions">
          Your contribution to sustainability matters a lot to our Mother Earth
        </div>
        <div className="event">Event: Earth Hour</div>
        <div className="date">Date: 5 Jun 2023</div>
        <div className="time">Time: 1800 - 1900</div>
        <Link to="/leaderboard">
          <div className="button">
            <div style={{ "margin-top": "22px" }}>Leaderboard</div>
          </div>
        </Link>
      </div>
      <div className="thankyouRight">
        <img
          src={require("../assets/images/thankyou.png")}
          alt="thankyou"
          className="image"
        />
      </div>
    </div>
  );
}
