import React from 'react';
import {BrowserRouter,  Route,  Switch} from 'react-router-dom';


import Home from './components/home.js';


const Routes = () => (
  <BrowserRouter >
      <Switch>
          <Route exact path="/" component={Home}/>
          
      </Switch>
  </BrowserRouter>
);

export default Routes;