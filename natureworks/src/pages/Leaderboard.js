import React from "react";
import FlatList from "flatlist-react";
import axios from 'axios';
import LeaderboardIndividual from "../items/LeaderboardIndividual";

const renderItem = (content) => {
  return (
    <LeaderboardIndividual
      key={content.Rank}
      rank={content.Rank}
      city={content.City}
      score={content.Numofpoints}
    />
  );
  
};

axios
  .get("http://127.0.0.1:5000/userdata")
  .then(function (response) {
    citydata = response.data;
    console.log(response.data[0])
  });

let citydata = [{ City: "Beijing", Rank: "1", Numofpoints: "1000" }];

export default function Leaderboard() {
  return (
    <div className="leaderboard">
      <div className="title">
        <div className="rank">Rank</div>
        <div className="cities">Cities</div>
        <div className="score">Scores</div>
      </div>

      <FlatList list={citydata} renderItem={renderItem} />
    </div>
  );
}
