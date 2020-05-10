import React,{Component} from 'react';
import ReactDOM from 'react-dom';



class Talk extends  Component{

     
    
    constructor(props){
        super(props);
        this.state = {username: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleReset = this.handleReset.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
      }

    handleSubmit(event){

        alert('Description Submitted !!');
        event.preventDefault();
        // const element
        console.log(this.state.value)
        // ReactDOM.render({{"Hey"}}, document.getElementById('problem-description');)
        this.setState({value: ''});
    }

    handleReset(event){
        this.setState({value: ''});
    }


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

            <header className="major">
                <h1>Talk to a counsellor</h1>
                <h4>Please describe how you feel briefly. =) </h4>
            </header>
            <form onSubmit = {this.handleSubmit} onReset = {this.handleReset}>

            <div className = "12u$">
            <textarea id = 'problem-description' placeholder='Write your heart out !!' required = {true} onChange={this.handleChange} value = {this.state.value} rows = "6"></textarea>
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


        	</div>

            </div>

        )

    }


}


export default Talk;