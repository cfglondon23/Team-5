import React from "react";

import { Link } from "react-router-dom";

export default function CampaignIndividual({ date, title, description, backgroundColor }) {

  return (
    <div className="campaignbox">
      <Link to="/campaign">
        <div className="box" style={{ "background-color": "#C4F5C3" }}>
          <div className="boxMargin">
            <div className="date">{date}</div>
            <div className="title">{title}</div>
            <div className="description">{description}</div>
          </div>
        </div>
      </Link>
    </div>
  );
}
