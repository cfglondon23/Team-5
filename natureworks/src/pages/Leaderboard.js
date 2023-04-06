import React from "react";
import FlatList from "flatlist-react";
import axios from "axios";
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

axios.get("http://127.0.0.1:5000/leaderboard").then(function (response) {
  citydata = response.data;
  console.log(response);
});

let citydata = [
  { City: "London", Numofpoints: "1000", Rank: "1" },
  { City: "Beijing", Numofpoints: "900", Rank: "2" },
  { City: "Edinburgh", Numofpoints: "850", Rank: "3" },
  { City: "Ohio", Numofpoints: "600", Rank: "4" },
  { City: "Oxford", Numofpoints: "590", Rank: "5" },
  { City: "Manchester", Numofpoints: "500", Rank: "6" },
  { City: "Singapore", Numofpoints: "400", Rank: "7" },
  { City: "Shanghai", Numofpoints: "400", Rank: "8" },
  { City: "Cardiff", Numofpoints: "300", Rank: "9" },
  { City: "Kent", Numofpoints: "300", Rank: "9" },
];

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
