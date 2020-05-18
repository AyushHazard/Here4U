import React,{Component, useState} from 'react';
import ReactDOM from 'react-dom';
import Header from './header.js';
import {NavLink} from 'react-router-dom';

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


    
        

        const [recData,setRecData] = useState("");

		

		


        const data = async() =>{
            const apiRes = await fetch("http://127.0.0.1:8000/api/list-counsellors/");
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
            <Header {...props}/>

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
                        <li><NavLink to = {`/book/${counsellor.User}`}><a class="button">Book an appointment</a></NavLink></li>

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