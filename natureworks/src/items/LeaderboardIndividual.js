import React from "react";

export default function LeaderboardIndividual({ rank, city, score }) {
let color = "#B4E8C9"

if (rank >= 7) {
    color = "#E3FEE8"
}
else if (rank >= 4) {
    color = "#C4F5C3"
}

  return (
    <div className="leaderboardIndividual" style={{"background-color": color}}>
      <div className="rank">{rank}</div>
      <div className="city">{city}</div>
      <div className="score">{score}</div>
    </div>
  );
}
