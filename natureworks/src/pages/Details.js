import React from "react";

import { Link } from "react-router-dom";

export default function Details() {
  return (
    <div className="detailBox">
      <div className="detailLeft">
        <div className="title">Earth Hour</div>
        <div className="category">Electricity</div>
        <div className="description">
          This challenge is a one-hour challenge designed to help you disconnect
          from your electronic devices and enjoy the world around you. The goal
          of this challenge is to turn off all electronic devices in your home
          for one hour and use that time to engage in other activities.
        </div>
        <div className="participants">Participants: 45</div>
        <div className="reward">Reward: 3x</div>
        <div className="time">Time: 18:00 - 19:00{/*  */}</div>
        <Link to="/campaign">
          <div className="button">
            <div style={{ "margin-top": "22px" }}>Join now</div>
          </div>
        </Link>
      </div>
      <div className="detailRight">
        <img
          src={require("../assets/images/electrical-energy.png")}
          alt="robot"
          className="image"
        />
      </div>
    </div>
  );
}
