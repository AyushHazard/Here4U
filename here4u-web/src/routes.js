import React from 'react';
import {BrowserRouter,  Route,  Switch} from 'react-router-dom';


import Home from './components/home.js';
import About from './components/about.js';
import Talk from './components/talk-to-counsellor.js';
import Faqs from './components/faqs.js';
import ActiveSessions from './components/active-sessions.js';
import Login from './components/login.js';
import SignUp from './components/signup.js';

const Routes = () => (
  <BrowserRouter >
      <Switch>
          <Route exact path="/" component={Home}/>
          <Route exact path = "/about/" component = {About} />
          <Route exact path = "/talk" component = {Talk}/>
          <Route exact path = "/faqs" component = {Faqs}/>
          <Route exact path = "/active-sessions" component = {ActiveSessions}/>
          <Route exact path = "/login" component = {Login}/>
          <Route exact path = "/signup" component = {SignUp}/>
      </Switch>
  </BrowserRouter>
);

export default Routes;