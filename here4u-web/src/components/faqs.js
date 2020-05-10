import React,{Component} from 'react';




class Faqs extends  Component{

    render(){

        const {location} = this.props;

		console.log(this.props)

		const homeStatus = location.pathname==="/" ? "active":"";
		const talkStatus = location.pathname ==="/talk" ? "active":"";
		const sessionsStatus = location.pathname ==="/active-sessions" ? "active":"";
		const faqStatus = location.pathname ==="/faqs" ? "active":"";
        const aboutStatus = location.pathname ==="/about" ? "active":"";


        return(

            <div>
            <div>

        	<header id="header">
				<a href="/" className="logo">Here4U</a>
			</header>

			<nav id="nav">
				<ul className="links">
					<li className = {homeStatus}><a href="/">Home</a></li>
					<li className = {talkStatus}><a href="/talk">Talk to a Counsellor</a></li>
					<li className = {sessionsStatus}><a href="/active-sessions">Active Sessions</a></li>
					<li className = {faqStatus}><a href="/faqs">FAQs</a></li>
					<li className = {aboutStatus}><a href="/about">About Us</a></li>
				</ul>
				
				<ul className="actions">
					<li><a href="/login" className="button">Log in</a></li>
					<li><a href="/signup" className="button">Sign Up</a></li>
				</ul>
				
			</nav>

            </div>

        	<div id="main">

            <h2>Under Construction</h2>



        	</div>
            </div>

        )

    }


}


export default Faqs;