import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <div>
        {'{'}% load static %{'}'} 
        {/*
  Here4U by HTML5 UP
  html5up.net | @ajlkn
  Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/}
        {/* Scripts */}
        <title>Here4U</title>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="{%static 'client/css/main.css' %}" />
        <noscript>&lt;link rel="stylesheet" href="{'{'}%static 'client/css/noscript.css' %{'}'}" /&gt;</noscript>
        {/* Wrapper */}
        <div id="wrapper" className="fade-in">
          {/* Intro */}
          {'{'}% block intro %{'}'}{'{'}% endblock %{'}'}
          {/* Header */}
          <header id="header">
            <a href="{%url 'client-home'%}" className="logo">Here4U</a>
          </header>
          {/* Nav */}
          <nav id="nav">
            <ul className="links">
              {'{'}%block home_state%{'}'}{'{'}%endblock%{'}'}<a href="{%url 'client-home'%}">Home</a>
              {'{'}%if client or not user.is_authenticated%{'}'}
              {'{'}%block talk_state%{'}'}{'{'}%endblock%{'}'}<a href="{%url 'talk-to-counsellor'%}">Talk to a Counsellor</a>
              {'{'}%block session_state%{'}'}{'{'}%endblock%{'}'}<a href="{%url 'active-sessions'%}">Active Sessions</a>
              {'{'}%else%{'}'}
              {'{'}%block client_state%{'}'}{'{'}%endblock%{'}'}<a href="{%url 'pick-clients'%}">Pick your clients</a>
              {'{'}%block active_state%{'}'}{'{'}%endblock%{'}'}<a href="{%url 'active-clients'%}">Active clients</a>
              {'{'}%endif%{'}'}
              {'{'}%block about_state%{'}'}{'{'}%endblock%{'}'}<a href="{%url 'client-about'%}">About Us</a>
            </ul>
            {'{'}%if user.is_authenticated%{'}'}
            <ul className="actions">
              <li><a href="{%url 'logout'%}" className="button">Log out</a></li>
            </ul>
            {'{'}%else%{'}'}
            <ul className="actions">
              <li><a href="{%url 'login'%}" className="button">Log in</a></li>
              <li><a href="{%url 'sign-up'%}" className="button">Sign Up</a></li>
            </ul>
            {'{'}%endif%{'}'}
            <ul className="icons">
              <li><a href="https://twitter.com/iitrpr" target="_blank" className="icon fa-twitter"><span className="label">Twitter</span></a></li>
              <li><a href="https://www.facebook.com/iitrpr/" target="_blank" className="icon fa-facebook"><span className="label">Facebook</span></a></li>
              <li><a href="https://www.instagram.com/iitropar/" target="_blank" className="icon fa-instagram"><span className="label">Instagram</span></a></li>
              <li><a href="https://github.com/AyushHazard/Here4U" target="_blank" className="icon fa-github"><span className="label">GitHub</span></a></li>
            </ul>
          </nav>
          {/* Main */}
          <div id="main">
            {'{'}% block content %{'}'}{'{'}% endblock %{'}'}
          </div>
          <div id="main"><center><h2> Contact Us </h2></center></div>
          {/* Footer */}
          <footer id="footer">
            <section>
              <form method="post" action="#">
                <div className="field">
                  <label htmlFor="name">Name</label>
                  <input type="text" name="name" id="name" />
                </div>
                <div className="field">
                  <label htmlFor="email">Email</label>
                  <input type="text" name="email" id="email" />
                </div>
                <div className="field">
                  <label htmlFor="message">Message</label>
                  <textarea name="message" id="message" rows={3} defaultValue={""} />
                </div>
                <ul className="actions">
                  <li><input type="submit" defaultValue="Send Message" /></li>
                </ul>
              </form>
            </section>
            <section className="split contact">
              <section className="alt">
                <h3>Address</h3>
                <p>1234 Somewhere Road #87257<br />
                  Nashville, TN 00000-0000</p>
              </section>
              <section>
                <h3>Phone</h3>
                <p><a href="#">(000) 000-0000</a></p>
              </section>
              <section>
                <h3>Email</h3>
                <p><a href="#">info@untitled.tld</a></p>
              </section>
              <section>
                <h3>Social</h3>
                <ul className="icons alt">
                  <li><a href="#" className="icon alt fa-twitter"><span className="label">Twitter</span></a></li>
                  <li><a href="#" className="icon alt fa-facebook"><span className="label">Facebook</span></a></li>
                  <li><a href="#" className="icon alt fa-instagram"><span className="label">Instagram</span></a></li>
                  <li><a href="#" className="icon alt fa-github"><span className="label">GitHub</span></a></li>
                </ul>
              </section>
            </section>
          </footer>
          {/* Copyright */}
          <div id="copyright">
            <ul><li>© Untitled</li><li>Design: <a href="https://html5up.net">HTML5 UP</a></li><li>Distributor: <a href="https://themewagon.com">ThemeWagon</a></li></ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
