import React,{Component} from 'react';
import { withRouter } from 'react-router-dom'



class Header extends  Component{

	

    render(){

		const location = this.props.location;

		console.log({location});

		const homeStatus = location.pathname==="/" ? "active":"";
		const talkStatus = location.pathname ==="/talk" ? "active":"";
		const sessionsStatus = location.pathname ==="/active-sessions" ? "active":"";
		const faqStatus = location.pathname ==="/faqs" ? "active":"";
		const aboutStatus = location.pathname ==="/about" ? "active":"";
		const activeClientsStatus = location.pathname ==="/active-clients"?"active":"";
		
		console.log(this.props);
		
		let intro = <div></div>;

		let buttons;

		



		if(this.props.extra.logged_in===true)
		{
			buttons = <ul className="actions">
			<li><a href="#" onClick={this.props.extra.handle_logout} className="button">Log Out</a></li>
		</ul>
		}
		else
		{
			buttons = <ul className="actions">
			<li><a href="/login" className="button">Log in</a></li>
			<li><a href="/signup" className="button">Sign Up</a></li>
		</ul>
		}

		let middle;
		console.log(this.props.extra.status)

		if(this.props.extra.user_type==="counsellor")
		{
			middle = <div><li className = {activeClientsStatus}><a href="/active-clients">Active Clients</a></li></div>
		}
		else{
			
			middle = <div><li className = {talkStatus}><a href="/talk">Talk to a Counsellor</a></li><li className = {sessionsStatus}><a href="/active-sessions">Active Sessions</a></li></div>
		}

		console.log({middle});

		if(homeStatus==="active")
		{
			intro = <div id="intro">
			<h1>Here4U</h1>
			<p>An online counselling platform designed by the students of <a href="http://www.iitrpr.ac.in">IIT Ropar.</a><br />
			</p>
			<ul class="actions">
				<li><a href="#header" class="button icon solo fa-arrow-down scrolly">Continue</a></li>
			</ul>
		</div>	
		}

        return(

        	<div>
				{intro}


        	<header id="header">
				<a href="/" className="logo">Here4U</a>
			</header>

			<nav id="nav">
				<ul className="links">
					<li className = {homeStatus}><a href="/">Home</a></li>
					{middle}
					<li className = {faqStatus}><a href="/faqs">FAQs</a></li>
					<li className = {aboutStatus}><a href="/about">About Us</a></li>
				</ul>
				
				{buttons}
				
			</nav>

            </div>


        )

    }


}


export default Header;