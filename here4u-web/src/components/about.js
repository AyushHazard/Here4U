import React,{Component} from 'react';
import Header from './header.js';



class About extends  Component{
    render(){

        

		


        return(

            <div>

                <Header {...this.props}/>
            

            

        	<div id="main">

                

<section className="post">
	<header className="major">
		<span className="date">April 25, 2017</span>
		<h1>About Us</h1>
		<p>COUNSELING IS NOT TO DEGRADE DECISION MAKING SKILL OF AN INDIVIDUAL RATHER THAN TO HELP THE PERSONS RESOLVE WHAT STIFLES THEIR ABILITY TO MANAGE THEIR LIVES.</p>
	</header>
	<div className="image main"><img src="assets/images/iitrpr1.jpeg" alt="" height="600" width="800" /></div>
	<p>Institute Counseling Service is here to support you. Our mission is to promote well-being, aiding to develop better understanding of the self, to grow both intellectually and emotionally, to be more satisfied and productive and improve the depth and quality of your life. To hike sound mental health, We provide help in dealing with emotional and behavioral problems like guilt, anxiety, stress, lack of confidence, low self esteem, depression and internet addiction of any sort, dependency, personal problems in relationship like co-dependency, rejection, separation home-sickness etc. Counseling Cell does fostering and inculcating life skills to make better adjustments and enriching healthy relationships.</p>
	<div className="expert_doctors_area p-0">
        <div className="container">
            <div className="row justify-content-center ">
                <div className="col-lg-6">
                    <div className="section_title mb-55 text-center">
                        <h2 >Our Counselors</h2>
                    </div>
                </div>
            </div>
            <div className="row justify-content-center">
                <div className="col-lg-4 col-md-6">
                    <div className="single_expert">
                        <div className="expert_thumb">
                            <img src="assets/images/ds.jfif" alt="" height="300" width="300"/>
                        </div>
                        <div className="experts_name text-center">
						<center>
                            <h3>Deepak Kr. Phogat</h3>
                            <span>Clinical Psychologist</span>
							</center>
                            <div className="social_links">
                                <ul>
                                    <li>Counselor,IIT Ropar
                                        
                                    </li>
                                    <li>deepak.phogat@iitrpr.ac.in
                                        
                                    </li>
                                    <li>Linkedin
                                        <a href="https://in.linkedin.com/in/deepak-phogat-587639136"> <i className="fa fa-linkedin"></i> </a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="col-lg-4 col-md-6">
                    <div className="single_expert">
                        <div className="expert_thumb">
                            <img src="assets/images/pic08.jpg" alt="" height="300" width="300"/>
                        </div>
                        <div className="experts_name text-center">
						<center>
                            <h3>Bhawna Suri</h3>
                            <span>Counseling Psychologist</span>
							</center>
                            <div className="social_links">
                                <ul>
                                    <li>Counselor, IIT Ropar 
                                        
                                    </li>
                                    <li>bhawna@iitrpr.ac.in
                                        
                                    </li>
                                    <li>Linkedin
                                        <a href="https://in.linkedin.com/in/bhawna-suri-933262120"> <i className="fa fa-linkedin"></i> </a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
	<div className="dsa">
		<h3>Confidentiality</h3>
		<p>Each client has an option to remain anonymous.Nobody is asked to reveal his identity in front of the counselors in normal case.
        Only the counselors mentioned above have the access to information and records of each session.Each session is given full consideration and no information is revealed to anyone, whoever it may be. However, exception may be made in the case of life threatening situation(s).</p>
    </div>
    
    <div className="admin">
        <h3>Administration</h3>
        <p>This site is solely governed by the Administration of IIT Ropar,Counseling Cell</p>
        <ul>
            <li><a href="https://www.facebook.com/iitrpr/">Facebook</a></li>
            <li><a href="https://twitter.com/iitrpr">Twitter</a></li>
            <li><a href="https://www.instagram.com/iitropar/">Instagram</a></li>
            <li><a href="https://www.linkedin.com/company/iitropar">Linkedin</a></li>
        </ul>
    </div>
    <div className="developers">
        <h3>Contributors</h3>
        <ul>
            <li>Ayush Agrawal</li>
            <li>Divyanshu Mathpal</li>
            <li>Shobit Gupta</li>
            <li>Samreet Singh Dhami</li>
            <li>Tanya Gupta</li>
        </ul>
    </div>
	</section>


        	</div>
            </div>

        )

    }


}


export default About;