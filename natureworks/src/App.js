import logo from './logo.svg';
import './App.css';

import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";



function App() {
  return (
    <Router basename="">
        <div>
          <Switch>
            <Route exact path="/">
              <div>Hello</div>
            </Route>
          </Switch>
        </div>
    </Router>
  );
}

export default App;
