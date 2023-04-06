import React from "react";

import LeaderboardIndividual from "../items/LeaderboardIndividual";

export default function Leaderboard() {
  return (
    <div className="leaderboard">
      <div className="title">
        <div className="rank">Rank</div>
        <div className="cities">Cities</div>
        <div className="score">Score</div>
      </div>
      <LeaderboardIndividual rank={1} city={"London"} score={1000} />
      <LeaderboardIndividual rank={2} city={"London"} score={1000} />
      <LeaderboardIndividual rank={3} city={"London"} score={1000} />
      <LeaderboardIndividual rank={4} city={"London"} score={1000} />
      <LeaderboardIndividual rank={5} city={"London"} score={1000} />
      <LeaderboardIndividual rank={6} city={"London"} score={1000} />
      <LeaderboardIndividual rank={7} city={"London"} score={1000} />
      <LeaderboardIndividual rank={8} city={"London"} score={1000} />
      <LeaderboardIndividual rank={9} city={"London"} score={1000} />
    </div>
  );
}
