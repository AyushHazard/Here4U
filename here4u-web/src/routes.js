import React from 'react';
import {BrowserRouter,  Route,  Switch} from 'react-router-dom';
import PropTypes from 'prop-types';

import Home from './components/home.js';
import About from './components/about.js';
import Talk from './components/talk-to-counsellor.js';
import Faqs from './components/faqs.js';
import ActiveSessions from './components/active-sessions.js';
import Login from './components/login.js';
import SignUp from './components/signup.js';
import Book from './components/book.js';

function Routes(props){

  console.log(props);
  const extra = props;
  return(
  <BrowserRouter {...props} >
      <Switch >
          <Route exact path="/" render = {(props)=><Home {...props} extra = {extra}/>}/>
          <Route exact path = "/about/" render = {(props)=><About {...props} extra = {extra}/>} />
          <Route exact path = "/talk" render = {(props)=><Talk {...props} extra = {extra}/>}/>
          <Route exact path = "/faqs" render = {(props)=><Faqs {...props} extra = {extra}/>}/>
          <Route exact path = "/active-sessions" render = {(props)=><ActiveSessions {...props} extra = {extra}/>} />
          <Route path = "/book/:id" render = {(props)=><Book {...props} extra = {extra}/>} />
          <Route exact path = "/login" render = {(props)=><Login {...props} extra = {extra}/>} />
          <Route exact path = "/signup" render = {(props)=><SignUp {...props} extra = {extra}/>} />
      </Switch>
  </BrowserRouter>
  )

}



export default Routes;

Routes.propTypes = {
  logged_in: PropTypes.bool.isRequired,
  display_form: PropTypes.func.isRequired,
  handle_logout: PropTypes.func.isRequired
}