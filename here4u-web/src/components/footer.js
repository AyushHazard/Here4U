import React,{Component} from 'react';




class Footer extends  Component{
    render(){
        return(

        	<div>

        	<div id = "main"><center><h2> Contact Us </h2></center></div>

        	<footer id="footer">
			
				<section>
				<center>
				<div className="expert_thumb">
                        <img src="assets/images/logo.png" alt="" height="320" width="300"/>
                    </div>
					
					<ul className="actions">
						<li><a href="/login" className="button">Log in</a></li>
						<li><a href="/signup" className="button">Sign Up</a></li>
					</ul>
					
					<p>Use your IIT Ropar Email id to sign up<br />
					</p>
					</center>
					
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
							<textarea name="message" id="message" rows="3"></textarea>
						</div>
						<ul className="actions">
							<li><input type="submit" value="Send Message" /></li>
						</ul>
					</form>
				</section>
				<section className="split contact">
					<section className="alt">
						<h3>Address</h3>
						<p>Indian Institute of Technology Ropar<br />
						Bara Phool,Birla Seed Farms<br />
						Rupnagar,Punjab,INDIA-140001</p>
					</section>
					<section>
						<h3>Contact Us</h3>
						<p><a href="http://www.iitrpr.ac.in/contact-us">IIT Ropar Contact us page</a></p>
					</section>
					<section>
						<h3>Email</h3>
						<p><a href="#">deepak.phogat@iitrpr.ac.in</a></p>
					</section>
					<section>
						<h3>Social</h3>
						<ul className="icons alt">
							<li><a href="https://twitter.com/iitrpr" target="_blank" className="icon fa-twitter"><span className="label">Twitter</span></a></li>
							<li><a href="https://www.facebook.com/iitrpr/" target="_blank" className="icon fa-facebook"><span className="label">Facebook</span></a></li>
							<li><a href="https://www.instagram.com/iitropar/" target="_blank" className="icon fa-instagram"><span className="label">Instagram</span></a></li>
							<li><a href="https://github.com/AyushHazard/Here4U" target="_blank" className="icon fa-github"><span className="label">GitHub</span></a></li>
						</ul>
					</section>
				</section>
			</footer>

		



        	</div>

        )

    }


}


export default Footer;