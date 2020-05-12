import React,{Component, useState} from 'react';
import ReactDOM from 'react-dom';



function Talk(props){

     
    
    

    const state = {description: ''};

    function handleChange(event) {
        state.description = event.target.value;
        // console.log(state.description)
      }

      function handleSubmit(event){

        alert('Description Submitted !!');
        // event.preventDefault();
        // const element
        console.log(state.description)
        // ReactDOM.render({{"Hey"}}, document.getElementById('problem-description');)
        state.description = "";
    }

    function handleReset(event){
        state.description = "";
    }


    
        const {location} = props;

        const [recData,setRecData] = useState("");

		

		const homeStatus = location.pathname==="/" ? "active":"";
		const talkStatus = location.pathname ==="/talk" ? "active":"";
		const sessionsStatus = location.pathname ==="/active-sessions" ? "active":"";
		const faqStatus = location.pathname ==="/faqs" ? "active":"";
        const aboutStatus = location.pathname ==="/about" ? "active":"";


        const data = async() =>{
            const apiRes = await fetch("http://hear4u.herokuapp.com/api/list-counsellors/");
            const resJSON = await apiRes.json();
            return resJSON;
        };

        
        console.log(data());

        data().then(res=>{
            setRecData(res);
            const data = Array.from(recData);
            data.map((counsellor)=>console.log(counsellor));
            // console.log(data);
        });


        
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

            <header className="major">
                <h1>Talk to a counsellor</h1>
                <h4>Please describe how you feel briefly. =) </h4>
            </header>
            <form onSubmit = {handleSubmit} onReset = {handleReset}>

            <div className = "12u$">
            <textarea id = 'problem-description' placeholder='Write your heart out !!' required = {true} onChange={handleChange} value = {state.value} rows = "6"></textarea>
            </div>
            
            <div className="12u$">
            <p>{"\n"}</p>
				<ul className="actions">
					
					<li><input type="submit" value="Submit" className="special" /></li>
					<li><input type="reset" value="Reset" /></li>
					<li>
						
						<input id = "extra_data" type="file" name="extra_data"/>
					</li>
					
				</ul>
			</div>



            </form>

            <section class="posts">

            {(Array.from(recData)).map((counsellor)=>{
            return(
                <article>
                    <header>
                        <h2><a href="#">{counsellor.Name}</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="../../static/images/pic02.jpg" alt="" /></a>
                    <p>{counsellor.Summary}</p><p>{"\n"}
                        <a href="#" class="button small icon fa-tag">Stress</a> <a href="#" class="button small icon fa-tag">Anger</a> <a href="#" class="button small icon fa-tag">Expertise tags</a></p>
                    <ul class="actions">
                        <li><a href="#" class="button">Message</a></li>
                        <li><a href="#" class="button">Book an appointment</a></li>

                    </ul>
                </article>
            )
          })}

			
			
			
		    </section>



        	</div>

            </div>

        )

    


}


export default Talk;