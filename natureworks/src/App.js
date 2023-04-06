import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Campaign from "./pages/Campaign";
import Details from "./pages/Details";
import Test from "./pages/Test";
import NavBar from "./pages/NavBar";
import ThankYou from "./pages/ThankYou";
import Leaderboard from "./pages/Leaderboard";

function App() {
  return (
    <Router basename="">
      <div>
        <NavBar />
        <Switch>
          <Route exact path="/">
            <Campaign />
          </Route>
          <Route exact path="/test">
            <Test />
          </Route>
          <Route exact path="/details">
            <Details />
          </Route>
          <Route exact path="/thankyou">
            <ThankYou />
          </Route>
          <Route exact path="/leaderboard">
            <Leaderboard />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
