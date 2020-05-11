import React,{Component} from 'react';




class Home extends  Component{
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

			<div id="intro">
				<h1>Here4U</h1>
				<p>An online counselling platform designed by the students of <a href="http://www.iitrpr.ac.in">IIT Ropar.</a><br />
				</p>
				<ul class="actions">
					<li><a href="#header" class="button icon solo fa-arrow-down scrolly">Continue</a></li>
				</ul>
			</div>	

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

        	<article className="post featured">
			<header className="major">
				<span className="date">April 25, 2017</span>
				<h2><a href="#">One day<br />
				Or day one<br />you decide</a></h2>
				<p>You don't have to be great to start, but you have to start to be great.</p>
			</header>
			<a href="#" className="image main"><img src="assets/images/moti.png" alt="" /></a>
			<ul className="actions">
				<li><a href="https://motivationgrid.com/best-five-real-life-inspirational-stories/" target="_blank" className="button big">Real Life Motivational Stories</a></li>
			</ul>
		</article>

	
		<section className="posts">
			<article>
				<a href="#" className="image fit"><img src="assets/images/pic1.jpeg" alt="" /></a>
				<p>Every obstacle we come across in life gives us an opportunity to improve our circumstances, and whilst the lazy complain, the others are creating opportunities through their kind hearts, generosity, and willingness to get things done.</p>
				<ul className="actions">
					<li><a href="#" className="button">Full Story</a></li>
				</ul>
			</article>
			<article>
				<a href="#" className="image fit"><img src="assets/images/pic2.jpg" alt="" /></a>
				<p>Our struggles in life develop our strengths. Without struggles, we never grow and never get stronger, so it’s important for us to tackle challenges on our own, and not be relying on help from others.</p>
				<ul className="actions">
					<li><a href="#" className="button">Full Story</a></li>
				</ul>
			</article>
			<article>
				<a href="#" className="image fit"><img src="assets/images/pic3.jpg" alt="" /></a>
				<p>Control your anger, and don’t say things to people in the heat of the moment, that you may later regret. Some things in life, you are unable to take back.</p>
				<ul className="actions">
					<li><a href="#" className="button">Full Story</a></li>
				</ul>
			</article>
			<article>
				<a href="#" className="image fit"><img src="assets/images/pic4.jpg" alt="" /></a>
				<p>People’s words can have a big effect on other’s lives. Think about what you say before it comes out of your mouth. It might just be the difference between life and death.</p>
				<ul className="actions">
					<li><a href="#" className="button">Full Story</a></li>
				</ul>
			</article>
			<article>
				<header>
					<span className="date">April 11, 2017</span>
					<h2><a href="#">Odio magna<br />
					sed consectetur</a></h2>
				</header>
				<a href="#" className="image fit"><img src="assets/images/pic06.jpg" alt="" /></a>
				<p>Donec eget ex magna. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque venenatis dolor imperdiet dolor mattis sagittis magna etiam.</p>
				<ul className="actions">
					<li><a href="#" className="button">Full Story</a></li>
				</ul>
			</article>
			<article>
				<header>
					<span className="date">April 7, 2017</span>
					<h2><a href="#">Augue lorem<br />
					primis vestibulum</a></h2>
				</header>
				<a href="#" className="image fit"><img src="assets/images/pic07.jpg" alt="" /></a>
				<p>Donec eget ex magna. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque venenatis dolor imperdiet dolor mattis sagittis magna etiam.</p>
				<ul className="actions">
					<li><a href="#" className="button">Full Story</a></li>
				</ul>
			</article>
		</section>
		<section>
		<h2>Our Mission</h2>
			<p>We want to provide support to all individuals affected by symptoms of mental health.
			We want to create awareness, reduce stigma and encourage individuals to speak out. Our vision
			is to help individuals overcome the impacts of poor mental health.Our Counselors are ready to hear any problem or 
			grievances that you face via video or audio call. You can also send a video describing your problems or you can express yourself by writing as you feel</p>
		</section>



        	</div>
			</div>

        )

    }


}


export default Home;