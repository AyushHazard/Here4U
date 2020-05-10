import React,{Component} from 'react';
import { withRouter } from 'react-router-dom'



class Header extends  Component{

	

    render(){

		

        return(

        	<div>

        	<header id="header">
				<a href="/" className="logo">Here4U</a>
			</header>

			<nav id="nav">
				<ul className="links">
					<li id = "home-stat"><a href="/">Home</a></li>
					<li id = "talk-stat"><a href="/talk">Talk to a Counsellor</a></li>
					<li id = "active-stat"><a href="/active-sessions">Active Sessions</a></li>
					<li id = "session-stat"><a href="/faqs">FAQs</a></li>
					<li id = "about-stat"><a href="/about">About Us</a></li>
				</ul>
				
				<ul className="actions">
					<li><a href="/login" className="button">Log in</a></li>
					<li><a href="/signup" className="button">Sign Up</a></li>
				</ul>
				
			</nav>



        	</div>

        )

    }


}


export default Header;