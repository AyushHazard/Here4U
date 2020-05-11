import React,{Component} from 'react';
import ReactDOM from 'react-dom';
import { withRouter } from 'react-router-dom'


class Login extends  Component{

     
    
    constructor(props){
        super(props);
        console.log(this.props)
        this.state = {username: '', password: ''};

        this.handleChangeUsername = this.handleChangeUsername.bind(this);
        this.handleChangePassword = this.handleChangePassword.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleReset = this.handleReset.bind(this);
    }

   

    handleChangeUsername(event) {
        this.setState({username: event.target.value});
      }
    
      handleChangePassword(event) {
        this.setState({password: event.target.value});
      }

    handleSubmit(event){

        console.log(this.props.location);
        
        event.preventDefault();
        // const element
        console.log(this.state.username)
        console.log(this.state.password)
        // ReactDOM.render({{"Hey"}}, document.getElementById('problem-description');)
        this.setState({username: '',password: ''});
    }

    handleReset(event){
        this.setState({username: '',password: ''});
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
                <h2>Log in</h2>
                
            </header>
            <form onSubmit = {this.handleSubmit} onReset = {this.handleReset}>

            <div className = "12u$">
                <label>Username</label>
            <input type = "text" placeholder = "Username" value = {this.state.username} onChange = {this.handleChangeUsername} required = {true}/>
            </div>

            <div className = "12u$">
                <p>{"\n"}</p>
                <label>Password</label>
            <input type = "password" placeholder = "Password" value = {this.state.password} onChange = {this.handleChangePassword} required = {true}/>
            </div>
            
            <div className="12u$">
            <p>{"\n"}</p>
				<ul className="actions">
					
					<li><input type="submit" value="Submit" className="special" /></li>
					<li><input type="reset" value="Reset" /></li>
					
					
				</ul>
			</div>



            </form>


        	</div>
            </div>

        )

    }


}


export default Login;