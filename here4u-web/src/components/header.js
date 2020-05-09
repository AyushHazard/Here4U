import React,{Component} from 'react';
import {Link} from 'react-router-dom';



class Header extends  Component{
    render(){
        return(

        	<div>

        	<header id="header">
				<a href="#" className="logo">Here4U</a>
			</header>

			<nav id="nav">
				<ul className="links">
					<li><a href="#">Home</a></li>
					<li><a href="#">Talk to a Counsellor</a></li>
					<li><a href="#">Active Sessions</a></li>
					<li><a href="#">FAQs</a></li>
					<li><a href="#">About Us</a></li>
				</ul>
				
				<ul className="actions">
					<li><a href="#" className="button">Log in</a></li>
					<li><a href="#" className="button">Sign Up</a></li>
				</ul>
				
			</nav>



        	</div>

        )

    }


}


export default Header;